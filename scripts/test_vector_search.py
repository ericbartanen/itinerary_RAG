from app.db.session import SessionLocal
from app.models.document_chunk import DocumentChunk
from app.services.embeddings import embed_text


def main():
    db = SessionLocal()

    try:
        query = "luxury lodge in Patagonia"
        query_embedding = embed_text(query)

        results = (
            db.query(DocumentChunk)
            .order_by(DocumentChunk.embedding.cosine_distance(query_embedding))
            .limit(5)
            .all()
        )

        for chunk in results:
            print("---")
            print(f"Chunk ID: {chunk.id}")
            print(f"Content: {chunk.chunk_content}")

    finally:
        db.close()


if __name__ == "__main__":
    main()