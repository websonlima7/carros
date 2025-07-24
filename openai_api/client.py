from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"

client = OpenAI()

def get_car_ai_bio(model, brand, model_year):
    prompt = (
        f"Escreva uma descrição para um carro {brand} {model} do ano {model_year}."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=60 
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar bio: {e}"
