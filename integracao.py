import openai

resposta = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {
            "role": "system", #o papel que o chat deve assumir
            "content": "Você é um assessor de investimentos da Messem Investimentos."
        },
        {
            "role": "user",
            "content": "Quero investir em algo seguro, tenho 10mil reais."
        }
    ]

)
print(resposta)