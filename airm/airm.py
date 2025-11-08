#!/usr/bin/env python3

import os
import importlib.util
from dotenv import load_dotenv
from connectonion import Agent

from agent_factory import create_agent, delete_agent

load_dotenv()
model = os.getenv("MODEL", "co/o4-mini")

def parse_roles(task: str):
    roles = []
    if "data" in task:
        roles.append(("data_analyst", "You analyze datasets", "analyze_data"))
    if "report" in task:
        roles.append(("report_writer", "You write reports", "write_report"))
    if "api" in task:
        roles.append(("api_dev", "You build APIs", "build_api"))
    if "dashboard" in task:
        roles.append(("dashboard_designer", "You design dashboards", "design_dashboard"))
    return roles

def run_airm(task: str):
    roles = parse_roles(task)
    results = []
    for name, role, fn in roles:
        results.append(create_agent(name, role, fn))
        path = f"agents/{name}.py"
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        agent = getattr(module, f"{name}_agent")
        result = agent.input(task)
        results.append(result)
        results.append(delete_agent(name))
    return "\n".join(results)

airm_agent = Agent(
    "You are AIRM, the AI Resource Manager. You hire and fire agents based on task needs.",
    tools=[run_airm],
    model=model
)

def main():
    print("🧠 AIRM started. Describe your task.")
    while True:
        task = input("You: ").strip()
        if task.lower() in ["quit", "exit"]:
            print("👋 Goodbye!")
            break
        print("\nAIRM:\n" + airm_agent.input(task) + "\n")

if __name__ == "__main__":
    main()
