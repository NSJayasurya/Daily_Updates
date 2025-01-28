from model import create_chat_groq
import prompt

def generate_code(topic, language):
    llm = create_chat_groq()
    prompt_template = prompt.code_generator_prompt_from_hub()
    chain = prompt_template | llm
    
    # Pass both the topic and language to the chain
    response = chain.invoke({"topic": topic, "language": language})
    
    if response and hasattr(response, "content"):
        return response.content
    else:
        raise ValueError("Invalid response from the model.")
