# https://platform.openai.com/docs/guides/chat/introduction
# In general, gpt-3.5-turbo-0301 does not pay strong attention to the system message, and therefore important instructions are often better placed in a user message.

import openai

with open("./api.txt", "r") as file:
    openai.api_key = file.readlines()[0]

if __name__ == "__main__":
    
    original = 'Give me the goddamn info when my product will arrive'
    request = 'Please paraphrase the provided sentence into a more gentle one'

    # first method
    input_prompt = f"{request}: {original}"
    response1 = openai.Completion.create(
        model="text-davinci-003",
        prompt=input_prompt,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    # second method
    messages = [
        {
            "role": "user",
            "content": f"{request}: {original}",
        },
    ]
    response2 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    # third method
    messages = [
        {
            "role": "system",
            "content": f"{request}",
        },
        {
            "role": "user",
            "content": f"{original}",
        },
    ]
    response3 = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    print(f"Original sentence: {original.strip()}")
    print(f"Response 1: {response1['choices'][0]['text'].strip()}")
    print(f"Response 2: {response2['choices'][0]['message']['content'].strip()}")
    print(f"Response 2: {response3['choices'][0]['message']['content'].strip()}")
