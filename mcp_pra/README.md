# MCP Pra - Task Manager Server

A simple Model Context Protocol (MCP) server for managing tasks.

## Setup

1. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

2. Activate the Poetry environment:
   ```bash
   poetry shell
   ```

## Running the Server

You can run the server in several ways:

### Using VS Code (Recommended)
1. Open the folder in VS Code
2. Press F5 or go to Run → Start Debugging
3. Select "Run MCP Server" configuration

### Using Poetry directly
```bash
poetry run python server.py
```

### Activating the Poetry shell first
```bash
poetry shell
python server.py
```

## Features

- Add tasks with titles and descriptions
- Mark tasks as completed
- List all tasks
- Get a summary prompt for pending tasks

## API Endpoints

### Tools
- `add_task(title: str, description: str = "")` - Add a new task
- `complete_task(task_id: int)` - Mark a task as completed

### Resources
- `tasks://all` - Get all tasks as a formatted string

### Prompts
- `task_summary_prompt()` - Get a prompt for summarizing pending tasks

## Dependencies

- fastmcp (>=3.4.7,<4.0.0)

## Notes

This project requires Python 3.13 or higher but less than 4.0.