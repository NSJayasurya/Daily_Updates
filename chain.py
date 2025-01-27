
from model import create_chat_groq
import prompt
def generate_poem(topic):
    llm=create_chat_groq()
    prompt_template = prompt.poem_generator_prompt_from_hub()
    chain = prompt_template | llm
    response = chain.invoke({"topic":topic})
    return response.content


"""
Chain that generates Poem

Args:"Hi"

Returns:
Response.content(str)

"""
