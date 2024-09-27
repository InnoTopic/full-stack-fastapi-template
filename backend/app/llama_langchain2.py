# llama_langchain.py

# Import necessary libraries from Langchain and Ollama
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model="llama3.1")

prompt_template = PromptTemplate(
    input_variables=["question"],
    template="""
    Express this natural language query as a JSON query format conforming to this TypeScript type:
    ```typescript
    interface Query {{
      foodType?: string;
      maxDistanceKm?: number;
      minRating?: number;
      openWithinMinutes?: number;
      locationName?: number;
    }};
    ```
    Just output the JSON query, no other text.
    
    The User prompt: {question}
    """
)

llm_chain = LLMChain(
    llm=llm,
    prompt=prompt_template
)


######

import json
# import markdown
# from bs4 import BeautifulSoup
# from langchain.schema import Document
import re


def extract_first_code_block_from_markdown(markdown_text):
    # Use regex to find the first code block, ignoring the type (e.g., json, python)
    code_block = re.search(r'```[^\n]*\n(.*?)```', markdown_text, re.DOTALL)

    if code_block:
        code_content = code_block.group(1).strip()  # Extract the first code block content
        try:
            # Parse the extracted code block as JSON
            parsed_json = json.loads(code_content)
            return parsed_json
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return None
    else:
        print("No code block found.")
        return None


# Define your question and run the chain
# question = "Sushi within 10km of my location"
# question = "Italian food open now"
# question = "Italian food open in 20min closeby"
# question = "Italian food open in 20min in Berlin Mitte"
question = "Italian food open in 1&half hours in Berlin Mitte"

# Get the response from the LLaMA model
response = llm_chain.run(question)

print(response)

print ('parsed: ')
print(extract_first_code_block_from_markdown(response))

