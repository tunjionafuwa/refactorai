from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage


HUMAN_MESSAGE = """
File: {filepath}

Prompt: {prompt}

Code: {code}

Find issues and suggest corrected version of this code
"""

class Client:
    def __init__(self, model: str = "gpt-4o-mini", temperature: float = 0.2) -> None:
        self.llm = init_chat_model(
            model=model,
            model_provider="openai",
            temperature=temperature
        )

    def review_code(self, code: str, filepath: str, prompt: str) -> str:
        """Send code to LLM to identify errors and suggest corrections."""
        messages: list[BaseMessage] = [
            SystemMessage(content="You are an expert Python code reviewer and editor."),
            HumanMessage(
                content=HUMAN_MESSAGE.format(filepath=filepath, prompt=prompt, code=code)
            ),
        ]
        response = self.llm.invoke(messages)
        return response.content
