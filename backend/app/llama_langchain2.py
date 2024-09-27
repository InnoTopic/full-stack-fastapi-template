# llama_langchain.py

# Import necessary libraries from Langchain and Ollama
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the LLaMA 3.1 model through Ollama
llm = Ollama(model="llama3.1")  # Use 'llama2' or ensure the correct model is installed locally in Ollama

# Define a template for your prompt
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
    
    The User prompt: {question}
    """
)

# Initialize a Langchain chain with the LLM and prompt template
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt_template
)

# Define your question and run the chain
# question = "Sushi within 10km of my location"
# question = "Italian food open now"
# question = "Italian food open in 20min closeby"
question = "Italian food open in 20min in Berlin Mitte"

# Get the response from the LLaMA model
response = llm_chain.run(question)

# Output the response
print(response)
