from refactorCli.llm.client import Client
from dotenv import load_dotenv

load_dotenv()



if __name__ == "__main__":
    llm_client = Client()
    print(llm_client.review_code(code="code", filepath="filepath", prompt="prompt"))
