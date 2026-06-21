# Contributing to ParasePDF

Thanks for your interest in improving this project.

## Ways to contribute

- Improve the PDF parsing workflow
- Add batch conversion support
- Add command-line options
- Improve error handling
- Expand the documentation
- Add OCR or scanned-PDF support
- Test the script with different PDF formats

## Suggested workflow

1. Fork the repository.
2. Create a new branch for your change.
3. Install the dependencies.
4. Run the script with a sample PDF.
5. Make your changes.
6. Verify the output.
7. Open a pull request.

## Local setup

```powershell
pip install -r requirements.txt
```

If you want to use the included virtual environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Pull request tips

Please keep pull requests focused and easy to review.

A good pull request description should include:

- what problem you are solving
- how you tested the change
- whether the output format changed
- any assumptions or limitations

## Code style

- Keep changes small and readable
- Prefer simple Python over heavy abstractions
- Preserve the existing JSON output format unless a change is intentionally requested

## Need an idea?

If you are looking for an easy first contribution, consider adding:

- a `--output-dir` option
- batch processing for folders
- OCR support for scanned PDFs
- richer metadata in the JSON output
