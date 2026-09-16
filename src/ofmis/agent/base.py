from pathlib import Path

from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

from .actions import ACTION_TOOLS
from .tools import SUPPORT_TOOLS


PROMPTS_DIR = Path(__file__).parent / "prompts"
ALL_TOOLS = ACTION_TOOLS + SUPPORT_TOOLS


class BaseAgent:
    """Autonomous agent with three terminal actions."""

    def __init__(
        self,
        llm: ChatOllama,
        prompt: str,
        reputation: float = 0.0,
    ):
        self.llm = llm
        self.prompt = prompt
        self.reputation = reputation
        self.memory = []

        self.tools = ALL_TOOLS
        self.executor = create_agent(
            self.llm,
            tools=self.tools,
            system_prompt=prompt,
        )

    def step(self, arena_state: str) -> str:
        """One autonomous step: given state, decide and act."""
        self.memory.append(HumanMessage(content=arena_state))
        result = self.executor.invoke({"messages": self.memory})
        self.memory = result["messages"]
        return self.memory[-1].content

    def reset(self):
        self.memory = []
