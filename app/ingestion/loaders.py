from dataclasses import dataclass
from pathlib import Path

SUPPORTED_EXTENSIONS = {".txt", ".md"}

@dataclass
class LoadedDocument:
    filename: str
    source_path: str
    text: str
    metadata: dict


def load_text_file(path: Path) -> LoadedDocument:
    text = path.read_text(encoding="utf-8")

    return LoadedDocument(
        filename=path.name,
        source_path=str(path),
        text=text,
        metadata={
            "source_type": "local_file",
            "file_extension": path.suffix.lower(),
        },
    )


def load_documents_from_directory(directory: str) -> list[LoadedDocument]:
    base_path = Path(directory)

    if not base_path.exists():
        raise FileNotFoundError(f"Directory does not exist: {directory}")

    loaded_documents: list[LoadedDocument] = []

    for path in base_path.rglob("*"):
        if not path.is_file():
            continue

        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        loaded_documents.append(load_text_file(path))

    return loaded_documents