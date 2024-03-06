import openllm

client = openllm.client.HTTPClient('http://localhost:3000')
response = client.query("Give me Course Structure for Machine learning which topic wise and chaper wise")

print(response)


# import streamlit as st
#
# # Define option outside of functions
# option = None
#
# #hell
# # Main content
# def main():
#     st.title("Make Your Own Notes 🤷‍♂️🧑‍💻👩‍🎓")
#
#     st.write(f"You've selected: {option}")
#
# # Sidebar content
# def sidebar():
#     global option
#     st.sidebar.title("Select Subject 👇")
#     user_input = st.sidebar.text_input("Enter your notes here:")
#
#     select_container = st.sidebar.empty()
#
#     # Check if user_input is not empty
#     if user_input:
#         st.sidebar.write("You entered the following notes:")
#         st.sidebar.write(user_input)
#         option = user_input
#
#         # If user has entered notes, disable the selectbox
#         # st.sidebar.markdown("<hr>", unsafe_allow_html=True)
#         # st.sidebar.markdown("**Selecting Subject Disabled**")
#         select_container.empty()
#
#     else:
#         # If user hasn't entered notes, enable the selectbox
#         st.sidebar.write("Or you can Select any subject")
#         option = st.sidebar.selectbox("Select Option", ["Machine_learning", "Modern_AI", "C language", "C++ language",
#                                                         "Python_language", "Oprating System", "Digital Electronics",
#                                                         "Computer Networks", "Java Programming", "Computer Architecture and Organization",
#                                                         "Database Management Systems", "Software Engineering", "Object-Oriented Programming (OOP)",
#                                                         "Data structures & Algorithm", "Discrete mathematics","Theory of computation"])
#
# # Run the app
# if __name__ == "__main__":
#     sidebar()
#     main()



# import streamlit as st
# import requests
# import json
#
# # Set up the Streamlit app
# st.title("Drosinees Detection System")
#
# # API endpoint URL
# url = "http://localhost:11434/api/generate"
#
# # Set up conversation history
# conversation_history = []
#
# # Function to generate responses
# def generate_response(prompt):
#     # Append user prompt to conversation history
#     conversation_history.append(prompt)
#
#     # Construct full prompt
#     full_prompt = "\n".join(conversation_history)
#
#     # Prepare data for the API request
#     data = {
#         "model": "llama2",
#         "stream": False,
#         "prompt": full_prompt,
#     }
#
#     # Send a POST request to the API
#     response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
#
#     if response.status_code == 200:
#         # Extract and append the actual response from the model's output
#         actual_response = json.loads(response.text)["response"]
#         conversation_history.append(actual_response)
#         return actual_response
#     else:
#         # Display error message
#         st.error(f"Error: {response.status_code}, {response.text}")
#         return None
#
# # Streamlit UI components
# user_prompt = st.text_area("Enter your prompt here...", key="user_prompt")
# if st.button("Generate Response"):
#     if user_prompt:
#         # Call the function and display the response
#         response = generate_response(user_prompt)
#         if response:
#             st.text_area("Model Response:", value=response, key="model_response")
#
# # Display conversation history
# st.text("Conversation History:")
# for entry in conversation_history:
#     st.text(entry)


# import streamlit as st
# import requests
# import json
#
# # Set up the Streamlit app
# st.title("Drosinees Detection System")
#
# # API endpoint URL
# url = "http://localhost:11434/api/generate"
#
# # Set up conversation history
# conversation_history = []
#
# # Function to generate responses
# def generate_response(prompt):
#     # Append user prompt to conversation history
#     conversation_history.append(prompt)
#
#     # Construct full prompt
#     full_prompt = "\n".join(conversation_history)
#
#     # Prepare data for the API request
#     data = {
#         "model": "llama2",
#         "stream": False,
#         "prompt": full_prompt,
#     }
#
#     # Send a POST request to the API
#     response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
#
#     if response.status_code == 200:
#         # Extract and append the actual response from the model's output
#         actual_response = json.loads(response.text)["response"]
#         conversation_history.append(actual_response)
#         return actual_response
#     else:
#         # Display error message
#         st.error(f"Error: {response.status_code}, {response.text}")
#         return None
#
# # Streamlit UI components for Drosinees Detection System
# user_prompt = st.text_area("Enter your prompt here...", key="user_prompt")
# if st.button("Generate Response"):
#     if user_prompt:
#         # Call the function and display the response
#         response = generate_response(user_prompt)
#         if response:
#             st.text_area("Model Response:", value=response, key="model_response")
#
# # Display conversation history
# st.text("Conversation History:")
# for entry in conversation_history:
#     st.text(entry)
#
# # Separate section for Make Your Own Notes
# st.title("Make Your Own Notes 🤷‍♂️🧑‍💻👩‍🎓")
#
# # Define option outside of functions
# option = None
#
# # Main content for Make Your Own Notes
# def main():
#     st.write(f"You've selected: {option}")
#
# # Sidebar content for Make Your Own Notes
# def sidebar():
#     global option
#     st.sidebar.title("Select Subject 👇")
#     user_input = st.sidebar.text_input("Enter your notes here:")
#
#     select_container = st.sidebar.empty()
#
#     # Check if user_input is not empty
#     if user_input:
#         st.sidebar.write("You entered the following notes:")
#         st.sidebar.write(user_input)
#         option = user_input
#
#         # If user has entered notes, disable the selectbox
#         # st.sidebar.markdown("<hr>", unsafe_allow_html=True)
#         # st.sidebar.markdown("**Selecting Subject Disabled**")
#         select_container.empty()
#
#     else:
#         # If user hasn't entered notes, enable the selectbox
#         st.sidebar.write("Or you can Select any subject")
#         option = st.sidebar.selectbox("Select Option", ["Machine_learning", "Modern_AI", "C language", "C++ language",
#                                                         "Python_language", "Oprating System", "Digital Electronics",
#                                                         "Computer Networks", "Java Programming", "Computer Architecture and Organization",
#                                                         "Database Management Systems", "Software Engineering", "Object-Oriented Programming (OOP)",
#                                                         "Data structures & Algorithm", "Discrete mathematics","Theory of computation"])
#
# # Run the app
# if __name__ == "__main__":
#     sidebar()
#     main()