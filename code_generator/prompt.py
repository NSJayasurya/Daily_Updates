from langchain_core.prompts import ChatPromptTemplate
from langchain import hub

def code_generator_prompt_from_hub(template="nsj-code-generator"):
    try:
        prompt_template = hub.pull(template)
        # Ensure the template accommodates both 'topic' and 'language' keys
        return prompt_template
    except Exception as e:
        raise ValueError(f"Failed to pull prompt template: {e}")

# def code_generator_prompt():
#     """
#     Generates Prompt template from the system and user messages
#     Returns:
#         ChatPromptTemplate -> Configured ChatPromptTemplate instance
#     """
#     system_msg = '''
#                Generate a {language} code snippet for the following problem statement:

#     {topic}

#     Ensure that the code is:
#     1. Well-documented with comments.
#     2. Efficient and follows best practices.
#     3. Easy to understand and ready to execute.

#     Output only the code, without additional explanations.'''
#     user_msg = "Write a code on the {topic}"
#     prompt_template = ChatPromptTemplate([
#         ("system", system_msg),
#         ("user", user_msg)
#     ])
#     return prompt_template

