from __future__ import annotations

import argparse
import json
from pathlib import Path

from markitdown import StreamInfo
from markitdown.converters import PdfConverter


def resolve_source_pdf(explicit_path: str | None) -> Path:
    if explicit_path:
        return Path(explicit_path)

    script_dir = Path(__file__).resolve().parent
    pdf_files = sorted(script_dir.glob("*.pdf"))

    if len(pdf_files) == 1:
        return pdf_files[0]

    raise SystemExit(
        "Provide a PDF path as an argument, or keep exactly one .pdf file next to the script."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a PDF file into JSON.")
    parser.add_argument(
        "pdf_path",
        nargs="?",
        help="Optional path to the PDF file. If omitted, the script uses the only PDF in the script folder.",
    )
    args = parser.parse_args()

    source_pdf = resolve_source_pdf(args.pdf_path)
    output_json = source_pdf.with_suffix(".json")

    print(f"Converting {source_pdf}", flush=True)
    with source_pdf.open("rb") as file_stream:
        result = PdfConverter().convert(
            file_stream,
            StreamInfo(extension=".pdf", mimetype="application/pdf"),
        )
    print("Conversion complete", flush=True)

    payload = {
        "source": str(source_pdf),
        "title": result.title,
        "markdown": result.markdown,
    }

    output_json.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(output_json)


if __name__ == "__main__":
    main()