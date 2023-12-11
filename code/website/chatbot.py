from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


class Chatbot:
    def __init__(self):
        print("New Chatbot")
        self.messages = [{"role": "system", "content": "You are a helpful assistant."}, ]

    def input_prompt(self, message):

        self.messages.append({"role": "user", "content": message})
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        r = completion.choices[0].message.content
        self.messages.append({"role": "user", "content": r})
        return r

    def flow(self):
        message = input()

        self.messages.append({"role": "user", "content": message})
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        r = completion.choices[0].message.content
        print(f"Bot: {r}")
        self.messages.append({"role": "user", "content": r})

    def loop(self):
        while True:
            self.flow()


if __name__ == "__main__":
    print("Start chatting with the bot (type 'quit' to stop)!")
    chatbot = Chatbot()
    chatbot.loop()
