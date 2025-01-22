import markdown



def markdown_to_html(text):
    """
    This function takes markdown text as input, uses the markdown 
    library to convert it into HTML format, and returns the HTML output.
    """
    to_html= markdown.markdown(text)
    return to_html


def prompts(userquery):
    """
    This function formats the user query into a string template, 
    which can then be used for generating further responses or instructions.
    """
    guide_prompt = f""" 
    User Input: {userquery}

    Response: If the document contains information related to the user's query, provide the relevant answer. If not, respond with:
    "Sorry, the requested data is not available in the document. Please asking those questoion which information are in file which you uploaded."
    """
    return guide_prompt
