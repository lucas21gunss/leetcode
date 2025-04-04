import openai

openai.api_key = "SUA_CHAVE_API_OPENAI"  # 🔒 Troque por sua chave da OpenAI

def gerar_solucao(texto_problema):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um especialista em programação. Resolva o problema com código bem comentado."},
            {"role": "user", "content": texto_problema}
        ]
    )
    return response['choices'][0]['message']['content']
