"""Volume-aware progress checks for the v2.3 editorial reduction."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path

from .audit import audit_source


@dataclass(frozen=True)
class VolumeTarget:
    id: int
    baseline: int
    minimum: int
    maximum: int


@dataclass(frozen=True)
class EditorialPlan:
    version: str
    baseline_visible_chars: int
    minimum_total: int
    maximum_total: int
    volumes: tuple[VolumeTarget, ...]


@dataclass(frozen=True)
class VolumeProgress:
    target: VolumeTarget
    current: int
    status: str

    @property
    def reduction_percent(self) -> float:
        return (self.target.baseline - self.current) / max(self.target.baseline, 1) * 100


@dataclass(frozen=True)
class EditorialReport:
    volumes: tuple[VolumeProgress, ...]
    current_total: int
    errors: tuple[str, ...]


def load_editorial_plan(path: Path) -> EditorialPlan:
    data = json.loads(path.read_text(encoding="utf-8"))
    targets = tuple(
        VolumeTarget(
            id=int(item["id"]),
            baseline=int(item["baseline"]),
            minimum=int(item["minimum"]),
            maximum=int(item["maximum"]),
        )
        for item in data["volumes"]
    )
    ids = [item.id for item in targets]
    if len(ids) != len(set(ids)):
        raise ValueError("editorial plan contains duplicate volume ids")
    for target in targets:
        if target.minimum > target.maximum:
            raise ValueError(f"volume {target.id} minimum exceeds maximum")
    total = data["target_total"]
    minimum_total = int(total["minimum"])
    maximum_total = int(total["maximum"])
    if minimum_total > maximum_total:
        raise ValueError("target total minimum exceeds maximum")
    return EditorialPlan(
        version=str(data["version"]),
        baseline_visible_chars=int(data["baseline_visible_chars"]),
        minimum_total=minimum_total,
        maximum_total=maximum_total,
        volumes=tuple(sorted(targets, key=lambda item: item.id)),
    )


def evaluate_editorial(
    book_dir: Path,
    plan: EditorialPlan,
    completed_volumes: frozenset[int],
) -> EditorialReport:
    known_ids = {item.id for item in plan.volumes}
    unknown = sorted(completed_volumes - known_ids)
    if unknown:
        raise ValueError(
            "unknown completed volume ids: " + ", ".join(map(str, unknown))
        )

    audit = audit_source(book_dir)
    current_by_volume = audit.volume_chars
    errors: list[str] = []
    progress: list[VolumeProgress] = []
    for target in plan.volumes:
        current = current_by_volume.get(target.id, 0)
        if target.id not in completed_volumes:
            status = "PENDING"
        elif target.minimum <= current <= target.maximum:
            status = "PASS"
        else:
            status = "FAIL"
            errors.append(
                f"volume {target.id} visible characters {current} "
                f"outside {target.minimum}-{target.maximum}"
            )
        progress.append(VolumeProgress(target, current, status))

    if completed_volumes == known_ids:
        if not plan.minimum_total <= audit.total_chars <= plan.maximum_total:
            errors.append(
                f"total visible characters {audit.total_chars} outside "
                f"{plan.minimum_total}-{plan.maximum_total}"
            )
    return EditorialReport(tuple(progress), audit.total_chars, tuple(errors))
