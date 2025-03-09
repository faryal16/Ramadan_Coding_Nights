import click  # To create a command-line interface (CLI)
import json  # To save and load tasks from a file
import os  # To check if a file exists

# File where tasks will be stored
todo_file = "todo.json"

def load_tasks():
    """Loads tasks from the todo.json file"""
    if not os.path.exists(todo_file):
        return []  # Return an empty list if the file doesn't exist
    with open(todo_file, "r") as file:
        content = file.read().strip()  # Read file content and remove leading/trailing spaces
        if not content:
            return []  # Return an empty list if the file is empty
        return json.loads(content)  # Load and return tasks

def save_tasks(tasks):
    """Saves tasks to the todo.json file"""
    with open(todo_file, "w") as file:
        json.dump(tasks, file, indent=4)  # Save tasks with indentation for readability

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass  # Placeholder for the command group

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()  # Load existing tasks
    tasks.append({"task": task, "done": False})  # Add new task as not done
    save_tasks(tasks)  # Save updated task list
    click.echo(f"✅ Task added successfully: {task}")

@click.command()
def list():
    """List all the tasks"""
    tasks = load_tasks()  # Load tasks
    if not tasks:
        click.echo("⚠️ No tasks found..")  # If no tasks, show message
        return
    print("📜 Your Todo List:")
    for index, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"  # Mark completed tasks or pending
        click.echo(f"\t{index}. {task['task']} [{status}]")

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True  # Mark task as completed
        save_tasks(tasks)
        click.echo(f"🎉 Task {task_number} marked as completed")
    else:
        click.echo(f"❌ Invalid task number: {task_number}")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)  # Remove selected task
        save_tasks(tasks)
        click.echo(f"🗑️ Removed task: {removed_task['task']}")
    else:
        click.echo(f"❌ Invalid task number: {task_number}")

# Add commands to the CLI
cli.add_command(add)  # Add task
cli.add_command(list)  # List tasks
cli.add_command(complete)  # Mark task as complete
cli.add_command(remove)  # Remove task

if __name__ == "__main__":
    cli()  # Run the CLI
