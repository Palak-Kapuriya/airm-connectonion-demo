from utils import ensure_folder, write_file, delete_file
import os
from dotenv import load_dotenv

load_dotenv()
model = os.getenv("MODEL", "co/o4-mini")

AGENT_DIR = "agents"

def create_agent(name: str, role: str, function_name: str):
    ensure_folder(AGENT_DIR)
    code = f"""from connectonion import Agent

def {function_name}(description: str) -> str:
    return f" {name} completed: {{description}}"

{name}_agent = Agent(
    "{role}",
    tools=[{function_name}],
    model="{model}"
)
"""
    write_file(f"{AGENT_DIR}/{name}.py", code)
    return f" Created agent '{name}' for role: {role}"

def delete_agent(name: str):
    path = f"{AGENT_DIR}/{name}.py"
    if delete_file(path):
        return f" Deleted agent '{name}'"
    return f" Agent '{name}' not found"
