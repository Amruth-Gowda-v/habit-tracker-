# Reading Habit Tracker

A small Python desktop application for recording the number of pages read in a day and submitting that quantity to a Pixela graph.

## Features

- Tkinter interface to increase or decrease the page count
- Confirmation of the selected daily quantity
- Sends the quantity and current date to the Pixela API
- Uses a separate module for the quantity-entry window

## Requirements

- Python 3
- `requests`
- Tkinter

Install the external dependency:

```bash
python -m pip install requests
```

## Configuration and security

The current source contains a Pixela user token. Treat it as exposed: revoke or rotate it before using the project again. Store the replacement token outside the source code (for example, in an environment variable) and do not commit it.

## Run

```bash
python main.py
```

The application opens the quantity-entry window and then submits the selected quantity to the configured Pixela graph.

## Notes

- The Pixela user name and graph ID are configured in `main.py`.
- A valid Pixela account, graph, network connection, and API token are required.
