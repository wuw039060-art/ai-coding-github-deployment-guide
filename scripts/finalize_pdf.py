"""Set the distributable PDF's document properties after Chrome printing."""

from pathlib import Path

from pypdf import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "dist" / "v2.3" / "AI写代码之后-v2.3.0.pdf"


def main() -> None:
    reader = PdfReader(PDF)
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    metadata = {str(key): str(value) for key, value in (reader.metadata or {}).items() if value is not None}
    metadata.update({"/Title": "AI 写代码之后", "/Author": "Stallen"})
    writer.add_metadata(metadata)
    replacement = PDF.with_suffix(".tmp.pdf")
    try:
        with replacement.open("wb") as stream:
            writer.write(stream)
        replacement.replace(PDF)
    finally:
        replacement.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
