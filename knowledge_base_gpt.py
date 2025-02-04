import openai
import json
import os

# Step 1: Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Step 2: Load the selected knowledge base dynamically
def load_knowledge_base(node_name):
    file_path = f"{node_name}_knowledge_base.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        raise FileNotFoundError(f"Knowledge base file '{file_path}' not found.")

# Step 3: Search function for retrieving relevant content
def search_knowledge_base(knowledge_base, query):
    results = []
    for section, content in knowledge_base.items():
        for key, value in content.items():
            if query.lower() in key.lower() or query.lower() in str(value).lower():
                results.append(f"{section} - {key}: {value}")
    return results[:3]  # Return the top 3 matches

# Step 4: Query GPT with the provided context
def gpt_query(node_name, query):
    try:
        # Load the selected knowledge base
        knowledge_base = load_knowledge_base(node_name)
        
        # Retrieve relevant knowledge base content
        search_results = search_knowledge_base(knowledge_base, query)
        
        if search_results:
            # Format the GPT prompt with context
            context = "\n".join(search_results)
            prompt = f"""
            You are an AI assistant specializing in Ericsson's {node_name.upper()}.
            Use the provided knowledge to answer the user's query:

            Context:
            {context}

            User Query:
            {query}
            """
            
            # OpenAI API call
            response = openai.Completion.create(
                engine="text-davinci-003",  # Or use "gpt-4" if available
                prompt=prompt,
                max_tokens=300,
                temperature=0.2
            )
            return response["choices"][0]["text"].strip()
        else:
            return "No relevant information found in the knowledge base."
    except Exception as e:
        return str(e)

# Step 5: User interaction
if __name__ == "__main__":
    print("Welcome to the Ericsson Knowledge Base Chat. Type 'exit' to quit.")
    node_name = input("Enter node name (e.g., pcg, pcc, ccpc): ").lower()
    
    while True:
        user_input = input("\nAsk your question: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = gpt_query(node_name, user_input)
        print(f"\nResponse:\n{response}")