# Todo CLI 📋

A simple and efficient command-line interface (CLI) for managing your to-do list using Python and Click.

## Features 🚀
- Add tasks to your to-do list 📝
- List all tasks with completion status ✅❌
- Mark tasks as completed ✅
- Remove tasks from the list 🗑️
- Tasks are stored persistently in a JSON file

## Installation 📥
Ensure you have Python installed on your system. Then, install Click using pip:

```sh
pip install click
```

## Usage 🛠️
Run the CLI with the following commands:

### Add a Task ➕
```sh
python todo.py add "Go to the gym"
```

### List All Tasks 📃
```sh
python todo.py list
```

### Mark a Task as Completed ✅
```sh
python todo.py complete 1
```
*(where `1` is the task number)*

### Remove a Task 🗑️
```sh
python todo.py remove 1
```
*(where `1` is the task number)*

## Example Output 🖥️
```sh
$ python todo.py add "Buy groceries"
Task added successfully: Buy groceries

$ python todo.py list
1. Buy groceries [❌]

$ python todo.py complete 1
Task 1 marked as completed

$ python todo.py list
1. Buy groceries [✅]

$ python todo.py remove 1
Removed task: Buy groceries
```

## File Storage 📂
Tasks are stored in `todo.json`, ensuring persistence across sessions.

## Contributing 🤝
Feel free to fork this repository, make improvements, and submit a pull request!

## License 📜
This project is licensed under the MIT License.

---
Enjoy your productive workflow! 🚀

