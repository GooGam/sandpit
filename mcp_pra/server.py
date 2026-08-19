from datetime import datetime
from fastmcp import FastMCP


# --- Server initialization ---
mcp = FastMCP("Task Manager")  # register as MCP-compliant endpoint


# --- In-memory task store ---
tasks = []
task_counter = 0


# --- Tool 1: add_task ---
@mcp.tool()
def add_task(title: str, description: str = "") -> dict:
    """Add a new task to the task manager. Returns the created task."""
    global task_counter
    task_counter += 1
    task = {
        "id": task_counter,
        "title": title,
        "description": description,
        "status": "pending",
        "created_at": datetime.now().isoformat(),
    }
    tasks.append(task)
    return task


# --- Tool 2: complete_task ---
@mcp.tool()
def complete_task(task_id: int) -> dict:
    """Mark a task as completed by its ID.
    Returns the updated task or an error."""
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            task["completed_at"] = datetime.now().isoformat()
            return task
    return {"error": f"Task with ID {task_id} not found."}


# --- Resource: list_tasks ---
@mcp.resource("tasks://all") # URI the AI uses to request this resource
def list_tasks() -> str:
    """Returns all tasks as a formatted string."""
    if not tasks:
        return "No tasks yet."
    lines = []
    for task in tasks:
        icon = "✅" if task["status"] == "completed" else "⏳"
        lines.append(
            f"{icon} [{task['id']}] {task['title']} - {task['status']}"
        )
    return "\n".join(lines)


# --- Prompt: task_summary_prompt ---
# Prompts are reusable instructions for the AI to perform specific tasks.
@mcp.prompt()
def task_summary_prompt() -> str:
    """A reusable prompt for summarizing pending tasks."""
    return (
        "You are a productivity assistant. "
        "Read the tasks://all resource and "
        "provide a concise summary of all PENDING tasks. "
        "Group them by priority if possible. "
        "End with a recommended next action."
    )


# --- Entry point ---
if __name__ == "__main__":
    mcp.run()
