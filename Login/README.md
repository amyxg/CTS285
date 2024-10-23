# Login Page

- This program logs in users: students, parents, teachers
- Checks and verifies if user is in db 
- Displays error message if username and/or password does not exist
- redirect into an option page for users (answerchecker, memory bank, etc)

# AN notes
- db browser for sqlite can be useful for testing
- you could do login and leave registration for later

# Start Program Instruction in CMD Terminal **note: statements in () are not to be executed in terminal**
- python -m venv env (Create virtual environment)
- source env/bin/activate (Activate virtual environment (Windows), you should see (env) before your @username)
- pip install flask werkzeug
- python userLogin.py (run program)
- deactivate (when done with program)