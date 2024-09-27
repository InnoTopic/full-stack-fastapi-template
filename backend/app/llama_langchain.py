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
    You are LLaMA 3.1, a powerful language model. Please answer the following question clearly and concisely:
    Question: {question}
    """
)

# Initialize a Langchain chain with the LLM and prompt template
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt_template
)

# Define your question and run the chain
question = "What is the future of AI in education?"

# Get the response from the LLaMA model
response = llm_chain.run(question)

# Output the response
print(response)
