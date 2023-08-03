
# Python Flask Contacts App

Python Project with Flask and MySQL

## Description

This project is a web application built in Python using the Flask framework and MySQL database. The application demonstrates how to create a simple web app and connect to a MySQL database for storing and retrieving data. Based on [Python Flask and Mysql Web Application | Practical Example](https://www.youtube.com/watch?v=IgCfZkR8wME) tutorial video.

## Requirements

Before you begin, ensure you have met the following requirements:

- **Python**: Make sure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/).

- **Pip**: Pip is a package manager for Python. It should be installed with your Python distribution. You can check if you have pip installed by running `pip --version` in your terminal.

- **Virtual Environment (optional but recommended)**: While not strictly required, it's highly recommended to use a virtual environment for managing your project's dependencies. You can create a virtual environment using `python -m venv venv` (for Python 3) or `virtualenv venv` (for Python 2). Activate the virtual environment with `source venv/bin/activate` on Linux/Mac or `venv\Scripts\activate` on Windows.

## Installation

Follow these steps to get your project up and running:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-project.git
   cd your-project
   ```

2. (Optional) Activate your virtual environment if you're using one.

3. Install the required dependencies:

	```bash
	pip install -r requirements.txt
	```

## Usage

1. Configure your project settings, such as database connection, keys, etc., by creating a config.yml file in the root directory. Use the provided config.yml.example as a template.

2. Ensure you have a running MySQL instance.

3. Run the application:

	```bash
	python app.py
	```

4. Open your web browser and navigate to `http://localhost:5000` to interact with the application.

## Notes

It might be needed to download a Mysqlclient Python wheel from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python
You will need to verify Python version with the CP version in the file. For example, if we are using **Python 3.8** in a **Win32** platform, you will download `mysqlclient-1.4.6-cp38-cp38-win32` because **cp38** means **CPython 3.8**

