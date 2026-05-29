from app.db.session import SessionLocal
from app.models.document import Document
from app.models.document_chunk import DocumentChunk
from app.services.embeddings import embed_text


def main():
    db = SessionLocal()

    try:
        content = "Explora Torres del Paine is a luxury lodge in Patagonia focused on guided exploration."

        document = Document(
            filename="test_patagonia.txt",
            source_path="manual-test",
            content_hash="test-hash-001",
            content_metadata={"source_type": "manual_test"},
        )

        embedding = embed_text(content)

        chunk = DocumentChunk(
            document=document,
            chunk_index=0,
            chunk_content=content,
            embedding=embedding,
            chunk_metadata={"section": "test"},
        )

        db.add(document)
        db.add(chunk)
        db.commit()

        print("Inserted test document and embedded chunk.")

    finally:
        db.close()


if __name__ == "__main__":
    main()