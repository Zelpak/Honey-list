# Honey List 🐝

[![Python Version](https://img.shields.io/badge/Python-%3E%3D%203.6-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Issues](https://img.shields.io/github/issues/Zelpak/honey-list.svg)](https://github.com/Zelpak/honey-list/issues)
[![Forks](https://img.shields.io/github/forks/Zelpak/honey-list.svg?style=social&label=Fork)](https://github.com/Zelpak/honey-list/forks)
[![Stars](https://img.shields.io/github/stars/Zelpak/honey-list.svg?style=social&label=Star)](https://github.com/Zelpak/honey-list/stargazers)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-v5.0-blue.svg)](https://customtkinter.tomschimansky.com/)

Honey List is a simple yet powerful to-do list application built with Python. It allows users to manage tasks, save them locally, and customize the theme of the app. With features like data persistence and a user-friendly interface, Honey List makes task management easy and enjoyable.

## Features

- **Task Management**: Add, edit, and delete tasks.
- **Data Persistence**: Tasks are saved to a local file, ensuring data isn't lost between sessions.
- **Customizable Themes**: Choose from light and dark themes to personalize your app.
- **Simple GUI**: Built using Tkinter for a smooth and intuitive user experience.
- **Cross-platform**: Works on any operating system with Python support.

## Tech Stack

- **Frontend**: Python with CustomTkinter (GUI)
- **Storage**: Local file system (JSON format for task storage)
- **Themes**: Light & Dark

## Installation

### Prerequisites

Make sure Python 3.6+ is installed on your machine. If not, download and install Python from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. Clone the repository:
    ```bash
    git clone https://github.com/Zelpak/honey-list.git
    ```

2. Navigate to the project directory:
    ```bash
    cd honey-list
    ```

3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python honey_list.py
    ```

## Usage

1. **Add Tasks**: 
    - Click the “Add Task” button, type your task, and press "Save."

2. **Edit Tasks**: 
    - Select a task, click the edit icon, and modify the task description.

3. **Delete Tasks**: 
    - Hover over the task and click the trash icon to delete it.

4. **Switch Themes**: 
    - Toggle between light and dark themes using the theme switcher in the settings.

## Contributing

We welcome contributions! If you'd like to improve Honey List, you can fork the repository and submit a pull request.

### Steps to Contribute:

1. Fork this repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -am 'Add new feature'
    ```
4. Push your branch:
    ```bash
    git push origin feature-branch
    ```
5. Create a pull request.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Tkinter community for providing great resources for GUI development.
- Special thanks to the open-source community for their contributions and tools that make development easier.
