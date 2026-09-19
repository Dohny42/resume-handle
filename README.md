# Resume Update Guide

This folder contains your resume in Markdown (`marek_dohnal_resume.md`).  
Keep the Markdown as the **single source of truth**.

## Recommended Workflow

1. **Edit the Markdown file** whenever you have updates (new job, projects, skills, etc.).
2. Use a Markdown → PDF converter when you need a PDF version (examples below).
3. For the **Projects** section: update it manually or use the helper script once you provide your GitHub username.

### Quick PDF generation

**Pandoc**

```bash
pandoc marek_dohnal_resume.md -o marek_dohnal_resume.pdf --pdf-engine=xelatex -V geometry:margin=1in
```

### Future

Projects section could be semi-automated through pulling my Github repos.