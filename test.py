import aisuite as ai
from dotenv import load_dotenv
from pprint import pprint
import os

#Load API KEY
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

#Models: <provider>:<model_name>
models = ["groq:mixtral-8x7b-32768", "groq:llama3-70b-8192", "groq:gemma-7b-it"]
# responses = []

def userQuery(message, system_message="Respond in Shakespearean English."):
    #Initialize aisuite Client
    client = ai.Client()

    messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": message}
    ]

    model_responses = {}

    for model in models:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7
        )
        model_responses[model] = response.choices[0].message.content
    
    return model_responses

def print_responses(responses_dict):
    print("\nModel Responses:")
    print("========================")
    for model, response in responses_dict.items():
        print(f"\nModel: {model}")
        print(f"Response:")
        pprint(response, width=80, indent=2)
        print("-" * 80)

if __name__ == "__main__":
    ask = input("Ask a question: ")
    responses = userQuery(ask)
    print_responses(responses)




