import streamlit as st
import requests
import json
# from langchain.prompts import PromptTemplate


# API endpoint URL
url = "http://localhost:11434/api/generate"

# Set up conversation history
conversation_history = []
user_prompt = ""
option = ""
option2 = ""

# template = PromptTemplate.from_template(
#     '''I am working on one course so I want to build notes and I also want notes for my University exam. Give me well-structured notes with proper chapters and subparts of those chapters for this: {user_input} subject'''
# )
# Function to generate responses
def generate_response(prompt):
    global option
    global option2

    # Append user prompt to conversation history
    conversation_history.append(prompt)

    # full_prompt = template.format(user_input=prompt)
    # Construct full prompt
    full_prompt = "\n".join(conversation_history)

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
        conversation_history.append(actual_response)
        return actual_response
    else:
        # Display error message
        st.error(f"Error: {response.status_code}, {response.text}")
        return None

# Streamlit UI components for Make Your Own Notes
user_prompt = st.sidebar.text_input("Enter your prompt here...", key="user_prompt_sidebar")
if st.sidebar.button("Generate Response"):
    if user_prompt:
        # Call the function and display the response
        response = generate_response(user_prompt)
        if response:
            st.write("Model Response:", value=response)
    else:
        # If the user hasn't entered anything, use option2
        response2 = generate_response(option2)
        if response2:
            st.write("Model Response:", value=response2)

if user_prompt:
    option = user_prompt

    # If the user has entered notes, disable the selectbox
    # select_container.empty()
else:
    # If the user hasn't entered notes, enable the second selectbox with a unique key
    st.sidebar.write("Or you can Select any subject")
    option2 = st.sidebar.selectbox("Select Option", ["Machine_learning", "Modern_AI", "C language", "C++ language",
                                                     "Python_language", "Oprating System", "Digital Electronics",
                                                     "Computer Networks", "Java Programming",
                                                     "Computer Architecture and Organization",
                                                     "Database Management Systems", "Software Engineering",
                                                     "Object-Oriented Programming (OOP)",
                                                     "Data structures & Algorithm", "Discrete mathematics",
                                                     "Theory of computation"], key="option2")



# Rest of the code for Make Your Own Notes
def main():
    st.title("Make Your Own Notes 🤷‍♂️🧑‍💻👩‍🎓")

    st.write(f"You've selected: {option if user_prompt else option2}")

    # Display conversation history in the sidebar
    st.text("Conversation History:")
    for entry in conversation_history:
        st.text(entry)

# Run the app
if __name__ == "__main__":
    main()





