import openai

# Твой API-ключ OpenAI
openai.api_key = "здесь мой ключ"

def get_embedding(text):
    response = openai.Embedding.create(
        model="text-embedding-3-small",
        input=text
    )
    return response["data"][0]["embedding"]

if __name__ == "__main__":
    text = "Привет, как дела?"
    print(get_embedding(text))
