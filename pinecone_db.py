import pinecone
from embedding import get_embedding

# API-ключ Pinecone
pinecone.init(api_key="здесь мой ключ", environment="us-west1-gcp")

index = pinecone.Index("telegram-bot")

def add_answer(text, label):
    vector = get_embedding(text)
    index.upsert([(label, vector)])

def find_nearest(text):
    vector = get_embedding(text)
    result = index.query(vector, top_k=1, include_metadata=True)
    return result

if __name__ == "__main__":
    # Добавляем примеры
    add_answer("да", "ДА")
    add_answer("нет", "НЕТ")
    add_answer("не знаю", "НЕОПРЕДЕЛЕНО")

    # Проверяем поиск
    print(find_nearest("не уверен"))
