from pathlib import Path
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
import re


HUMAN_MESSAGE = """
File: {filepath}

Prompt: {prompt}

Code: {code}

Find issues and suggest corrected version of this code
"""


class Client:
    def __init__(self, model: str = "gpt-4o-mini", temperature: float = 0.2) -> None:
        self.llm = init_chat_model(
            model=model, model_provider="openai", temperature=temperature
        )

    def review_code(self, code: str, filepath: str | Path, prompt: str) -> str:
        """Send code to LLM to identify errors and suggest corrections."""
        messages: list[BaseMessage] = [
            SystemMessage(content="You are an expert Python code reviewer and editor."),
            HumanMessage(
                content=HUMAN_MESSAGE.format(
                    filepath=filepath, prompt=prompt, code=code
                )
            ),
        ]
        response = self.llm.invoke(messages)
        code_only = extract_code_blocks(response.text)

        return code_only


def extract_code_blocks(text: str) -> str:
    """Extract only code from an LLM response."""
    # Match ```python ... ``` or ``` ... ```
    code_blocks = re.findall(r"```(?:python)?\n([\s\S]*?)```", text)
    if code_blocks:
        return "\n\n".join(code_blocks).strip()
    # Fallback: if no fenced code, try to heuristically find code-looking lines
    lines = text.splitlines()
    code_lines = [
        line
        for line in lines
        if line.strip()
        and not line.strip().startswith(("Here", "Explanation", "# Changes"))
    ]
    return "\n".join(code_lines).strip()
