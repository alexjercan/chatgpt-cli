import openai

SYSTEM = "You are a helpful AI assistant that can answer questions provided by the user"

prompt = input("User: ")

chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": prompt}
    ]
)

print(f"GPT: {chat_completion.choices[0].message.content}")
