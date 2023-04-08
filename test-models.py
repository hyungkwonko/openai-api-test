# https://platform.openai.com/docs/guides/chat/introduction
# In general, gpt-3.5-turbo-0301 does not pay strong attention to the system message, and therefore important instructions are often better placed in a user message.

import openai

with open("./api.txt", "r") as file:
    openai.api_key = file.readlines()[0]

if __name__ == "__main__":
    
    # original = 'Give me the goddamn info when my product will arrive'
    original = '내 물건 언제 오는지나 빨리 알려달라고 이 자식아'
    request = '다음 요청을 내용은 같지만 좀 더 친절한 말투로 바꿔줘.'

    models = ['gpt-3.5-turbo', 'gpt-3.5-turbo-0301']
    # models = ['text-davinci-003', 'gpt-3.5-turbo', 'gpt-3.5-turbo-0301', 'text-davinci-002']

    messages = [
        {
            "role": "user",
            "content": f"{request}: {original}",
        },
    ]

    print(f"Original sentence: {original.strip()}")
    for model in models:
        response = openai.ChatCompletion.create(model=model, messages=messages)
        print(f"Response_{model}: {response['choices'][0]['message']['content'].strip()}")
