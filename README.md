# Resume – update & generate PDF

## Files

| File | Purpose |
|------|---------|
| `marek_dohnal_resume.md` | **Source of truth** – edit this |
| `generate_resume_pdf.py` | Converts Markdown → PDF (uses markdown-it-py) |
| `marek_dohnal_resume.pdf` | Latest generated PDF |

---

## Setup

1. Make sure uv [uv](https://docs.astral.sh/uv/#installation) installed
2. Clone the repository:

```bash
git clone https://github.com/Dohny42/resume-handle.git
```

3. Sync the environment (deps installation):
```bash
uv sync
```

4. Activate virtual environment:
```bash
.venv/Scripts/activate
```

## Everyday workflow

1. Edit `marek_dohnal_resume.md` or `styles.css`
2. Generate the PDF:

```bash
uv run generate_resume_pdf.py
```

Or with explicit paths:

```bash
uv run generate_resume_pdf.py -i marek_dohnal_resume.md -o resume.pdf
uv run generate_resume_pdf.py --input marek_dohnal_resume.md --output ~/Downloads/Marek_Dohnal.pdf
```