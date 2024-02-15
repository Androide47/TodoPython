# Todo List Flask App

This is a simple Todo List application built using Flask, a lightweight web framework for Python. The app allows users to create, update, and delete tasks, helping them stay organized and manage their daily activities effectively.

## Features

- User Registration and Login: Users can create an account and log in to access their personalized Todo List.
- Create Tasks: Users can add new tasks to their list, providing a title and optional description.
- Update Tasks: Users can edit the details of existing tasks, such as the title or description.
- Mark Tasks as Complete: Users can mark tasks as complete once they are finished.
- Delete Tasks: Users can remove tasks from their list when they are no longer needed.
- User Authentication: The app ensures that only authenticated users can access and modify their Todo List.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/todo-list-flask.git
   ```

2. Navigate to the project directory:

   ```bash
   cd todo-list-flask
   ```

3. Create a virtual environment:

   ```bash
   python3 -m venv env
   ```

4. Activate the virtual environment:

   - For Windows:

     ```bash
     env\Scripts\activate
     ```

   - For macOS/Linux:

     ```bash
     source env/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Set up the database:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

7. Start the application:

   ```bash
   flask run
   ```

8. Open your web browser and visit `http://localhost:5000` to access the Todo List app.

## Usage

- Register a new account or log in with your existing credentials.
- Once logged in, you will be redirected to your personalized Todo List.
- Click on the "Add Task" button to create a new task.
- To edit a task, click on the task title or the "Edit" button.
- To mark a task as complete, click on the checkbox next to the task title.
- To delete a task, click on the "Delete" button.
- Log out from your account using the "Logout" button.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository. You can also fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as per the terms of the license.

## Acknowledgements

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Bootstrap: [https://getbootstrap.com/](https://getbootstrap.com/)
- Font Awesome: [https://fontawesome.com/](https://fontawesome.com/)
