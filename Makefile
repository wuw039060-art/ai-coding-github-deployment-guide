PYTHON ?= python3
VERSION ?= 2.3.0
COMPLETED_VOLUMES ?=
SOURCE_EPUB := AI 写代码之后-v2.2.0.epub
SOURCE_TXT := AI 写代码之后-v2.2.0.txt

.PHONY: source verify verify-recovery audit pilot progress test

source:
	$(PYTHON) scripts/book.py source --epub '$(SOURCE_EPUB)' --output book

verify:
	$(PYTHON) scripts/book.py verify --version $(VERSION) --book book --epub '$(SOURCE_EPUB)' --txt '$(SOURCE_TXT)' --report VERIFICATION.md

verify-recovery:
	$(PYTHON) scripts/book.py verify --version $(VERSION) --book book --epub '$(SOURCE_EPUB)' --txt '$(SOURCE_TXT)' --report VERIFICATION.md --recovery-fidelity

audit:
	$(PYTHON) scripts/book.py audit --version $(VERSION) --book book --report AUDIT-v2.3.md

pilot:
	$(PYTHON) scripts/book.py pilot --book book --report PILOT-v2.3.md

progress:
	$(PYTHON) scripts/book.py progress --book book --plan book/editorial-plan.json --completed-volumes '$(COMPLETED_VOLUMES)' --report EDITORIAL-v2.3.md

test:
	$(PYTHON) -m unittest discover -s tests -v
