from pathlib import Path


def read_document(filename: str):

    text = Path(filename).read_text(encoding="utf-8")

    return {
        "content": text,
        "metadata": {
            "filename": filename
        }
    }