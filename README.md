# tasc

A simple, fast command-line task manager.

## What it does

`tasc` lets you manage your to-do list directly from the terminal — no app, no browser, no distractions. Add tasks, list them, and mark them as done in seconds.

## Installation

```bash
pip install tasc
```

Once installed, the `tasc` command is available globally from anywhere on your system.

## Usage

```bash
tasc add "Buy groceries"     # Add a new task
tasc list                    # Show all tasks
tasc complete <id>           # Mark a task as done
```

### Example

```bash
$ tasc add "Write project report"
Added: Write project report

$ tasc list
[ ] 0: Write project report
[ ] 1: Buy groceries

$ tasc complete 0
Done!

$ tasc list
[x] 0: Write project report
[ ] 1: Buy groceries
```

## Requirements

- Python 3.10+

## License

MIT
