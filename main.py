import openai

SYSTEM = "You are a helpful AI assistant that can answer questions provided by the user"
HISTORY = [{"role": "system", "content": SYSTEM}]

while True:
    prompt = input("User: ")

    if prompt == "exit":
        break

    HISTORY.append({"role": "user", "content": prompt})

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=HISTORY,
    )

    response = chat_completion.choices[0].message.content

    HISTORY.append({"role": "assistant", "content": response})

    print(f"GPT: {response}")
