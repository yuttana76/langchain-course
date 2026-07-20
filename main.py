import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
# from langchain_google import GoogleSearchAPIWrapper

load_dotenv()

def main():
    print("Hello from langchain-course!")
    print(f"OpenAI API Key: {os.getenv('OPENAI_API_KEY')}")
    print(f"Google API Key: {os.getenv('GOOGLE_API_KEY')}")


    information = """ 
    Elon Reeve Musk (/ˈiːlɒn/ ⓘ EE-lon; born June 28, 1971) is a businessman and former public official who is the CEO and largest shareholder of Tesla and SpaceX. Musk has been the wealthiest person in the world since 2025, and became the only trillionaire in terms of US dollars in June 2026; as of July 10, 2026, Forbes estimates his net worth to be US$917 billion.
    """

    summary_template = """
    given the informatioln {information} about a person I want you to create:
    1. Ashort summary
    2. two interesting facts about them
    3. How old is he.
    """

    summary_prompt_template = PromptTemplate(
        input_variables =["information"],template=summary_template
    )

    llm = ChatOpenAI(temperature=0,model="gpt-5")
    # llm = ChatOllama(temperature=0,model="gemma3:1b")

    chain = summary_prompt_template | llm

    response = chain.invoke(input ={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
