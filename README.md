# Welcome Flask App

A simple Flask application that takes your name from the URL and displays a personalized welcome message.

## Features
- Accepts user input through the URL.
- Displays a "Welcome" message along with the provided name.
- Lightweight and easy to set up for Flask beginners.

## Prerequisites

Before running the application, ensure you have the following installed:

- [Python 3.7+](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/) (Python web framework)

## Installation

1. Clone or download the repository:

```bash
$ git clone <repository-url>
$ cd flask-welcome-app
```

2. Install the required dependencies:

```bash
$ pip install flask
```

## Usage

1. Run the Flask app:

```bash
$ python app.py
```

2. Open your browser and navigate to:

```
http://127.0.0.1:5000/<your-name>
```

Replace `<your-name>` with your name to see the welcome message.

Example:

```
http://127.0.0.1:5000/Vaishnavi
```

You will see:

```
Welcome, Vaishnavi!
```

## Code Structure

- `app.py`: Contains the main Flask application code.

Happy coding!
