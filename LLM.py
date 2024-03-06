import requests
import json
from langchain.prompts import PromptTemplate


url = "http://localhost:11434/api/generate"


template = PromptTemplate.from_template(
    '''I am working on one course so I want to build notes and I also want notes for my University exam. Give me well-structured notes with proper chapters and subparts of those chapters for this: {user_input} subject'''
)

def generate_response(user_input):

    full_prompt = template.format(user_input=user_input)

    # Prepare data for the API request
    data = {
        "model": "llama2",
        "stream": False,
        "prompt": full_prompt,
    }

    # Send a POST request to the API
    response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))

    if response.status_code == 200:
        # Extract and append the actual response from the model's output
        actual_response = json.loads(response.text)["response"]
        # conversation_history.append(actual_response)
        return actual_response
    else:
        # Display error message
        print(f"Error: {response.status_code}, {response.text}")
        return None


def main():
    print("Chat with Ollama using a prompt template. Type 'exit' to end the conversation.")

    while True:
        user_input = input("which subject Note Do you Want :  ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        response = generate_response(user_input)
        print("Ollama:", response)

if __name__ == "__main__":
    main()