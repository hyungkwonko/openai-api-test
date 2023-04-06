# reference: https://www.youtube.com/watch?v=b-QeMi1A2go
import openai

with open("./api.txt", "r") as file:
    openai.api_key = file.readlines()[0]

messages = []

if __name__ == "__main__":
    while True:
        user_content = input("user: ")
        messages.append({"role": "user", "content": f"{user_content}"})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        assistant_content = response["choices"][0]["message"]["content"].strip()
        messages.append({"role": "assistant", "content": f"{assistant_content}"})
        print(f"GPT: {assistant_content}")
