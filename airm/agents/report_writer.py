from connectonion import Agent

def write_report(description: str) -> str:
    return f" report_writer completed: {description}"

report_writer_agent = Agent(
    "You write reports",
    tools=[write_report],
    model="co/o4-mini"
)
