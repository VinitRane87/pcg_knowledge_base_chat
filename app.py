import streamlit as st
import openai
import json

# Set OpenAI API Key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Load the knowledge base
with open("updated_gpt_ready_pcg_1_25_with_pcfw.json", "r") as file:
    knowledge_base = json.load(file)

# Search the knowledge base for relevant content
def search_knowledge_base(query):
    results = []
    for section, content in knowledge_base.items():
        for key, value in content.items():
            if query.lower() in key.lower() or query.lower() in str(value).lower():
                results.append(f"{section} - {key}: {value}")
    return results[:3]  # Return top 3 matches

# Query GPT using OpenAI API
def gpt_query(query):
    search_results = search_knowledge_base(query)
    if search_results:
        context = "\n".join(search_results)
        prompt = f"""
        You are an AI assistant specializing in Ericsson's Packet Core Gateway (PCG) 1.25 with PCFW.
        Use the following knowledge to answer the user's query:

        Context:
        {context}

        User Query:
        {query}
        """
        # OpenAI API call
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.2
        )
        return response["choices"][0]["text"].strip()
    else:
        return "No relevant information found in the knowledge base."

# Streamlit UI
st.title("Ericsson Knowledge Base Chatbot")
st.write("Ask questions about PCG 1.25 with PCFW")

user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    response = gpt_query(user_input)
    st.write("Response:")
    st.write(response)
