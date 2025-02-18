import openai

openai.api_key = "your-api-key-here"

def translate_text(text, target_language):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Translate this to {target_language}: {text}"}]
    )
    return response["choices"][0]["message"]["content"]

text_input = input("Enter text to translate: ")
language = input("Enter target language: ")
print("Translated Text:", translate_text(text_input, language))
