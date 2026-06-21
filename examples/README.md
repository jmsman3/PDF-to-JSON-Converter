# Example Folder Structure

Use this folder as a simple reference for how to organize your own files when using the converter.

```text
ParasePDF/
├─ extract_pdf_to_json.py
├─ README.md
├─ examples/
│  ├─ sample-output.json
│  └─ README.md
├─ your-document.pdf
└─ your-document.json
```

The sample JSON file is sanitized and is only meant to show the expected output structure.

## Recommended workflow

1. Copy your PDF into the repository folder.
2. Keep only one PDF in the folder if you want to run the script without arguments.
3. Or pass the full PDF path when you run the script.
4. The generated JSON file will appear next to the source PDF.
5. Use the sample JSON file as a format reference, not as production data.

## Example commands

```powershell
python extract_pdf_to_json.py
```

```powershell
python extract_pdf_to_json.py "D:\ParasePDF\your-document.pdf"
```
