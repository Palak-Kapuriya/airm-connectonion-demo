# 🧠 AIRM: AI Resource Manager (ConnectOnion Demo)

AIRM (AI Resource Manager) is a command-line system built with ConnectOnion that dynamically creates, executes, and retires AI agents based on user-defined tasks. It simulates a corporate HR model for managing AI agents — hiring agents for specific roles, assigning them tasks, and firing them when their work is complete.

## 🚀 Features

- Task-driven agent orchestration
- Dynamic agent creation using ConnectOnion's Agent class
- Each agent is a standalone Python module with a specific role
- Automatic agent cleanup after task completion
- Support for persistent agents (future-ready)
- Secure configuration using .env for API keys and model selection

## 📦 Project Structure

```

airm-connectonion-demo/
├── airm.py               # Main orchestrator agent (AIRM)
├── agent_factory.py      # Agent creation and deletion logic
├── utils.py              # Helper functions for file operations
├── agents/               # Folder for dynamically generated agents
├── .env                  # API key and model configuration
├── README.md             # Project documentation
```

## ⚙️ Setup

1. Clone the repository

   git clone <https://github.com/your-username/airm-connectonion-demo.git>
   cd airm-connectonion-demo

2. Install dependencies

   pip install -r requirements.txt

   Make sure you have the `connectonion` and `python-dotenv` packages installed.

3. Configure environment variables

   Create a `.env` file in the root directory:

   OPENONION_API_KEY=your-openonion-api-key
   AGENT_EMAIL=<your-agent-email@mail.openonion.ai>
   MODEL=co/o4-mini

## 🧪 Usage

Run the AIRM orchestrator:

   python airm.py

Then describe your task in natural language. Example:

   You: analyze employee data and generate a report

AIRM will:

1. Parse the task
2. Dynamically create agents like `data_analyst` and `report_writer`
3. Execute each agent’s tool
4. Delete agents after task completion

## 🧠 Example Output

🆕 Created agent 'data_analyst'
✅ data_analyst completed: analyze employee data and generate a report
🗑️ Deleted agent 'data_analyst'

🆕 Created agent 'report_writer'
✅ report_writer completed: analyze employee data and generate a report
🗑️ Deleted agent 'report_writer'

## 📌 Notes

- Agents are created as `.py` files in the `agents/` folder.
- Each agent is a ConnectOnion `Agent` with a single tool function.
- You can extend the `parse_roles()` function in `airm.py` to support more roles.
- Persistent agents (e.g., for live data monitoring) can be supported by skipping deletion.

## 📬 Author

Built by Palak Kapuriya  
Demo project for showcasing agent orchestration using ConnectOnion.

## ⭐️ License

This project is open-source and available under the MIT License.
