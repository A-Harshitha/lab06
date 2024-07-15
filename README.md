# Lab06 Flask Application

Developed a password format checker

## Prerequisites

- Python 3.x installed on your system
- A terminal or command prompt

## Setup Instructions

### 1. Unzip the `lab06` Folder

Unzip the `lab06` folder to your desired location. For example, you might unzip it to `C:\Users\YourUsername\Projects\`.

### 2. Navigate to the `lab06` Directory

Open a terminal or command prompt and navigate to the `lab06` directory:
```bash
cd path\to\lab06
```

### 3. Create a Virtual Environment

Create a virtual environment named `venv` inside your `lab06` directory:
```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```

- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 5. Install Flask

Install Flask using pip:
```bash
pip install Flask
```

### 6. Run the Flask Application

Ensure your application code is in the `lab06` directory, typically in a file named `app.py`. Run the Flask application:
```bash
python app.py
```

This command will start the Flask development server. You should see output indicating the server is running, such as:
```bash
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### 7. Access Your Flask Application

Open a web browser and navigate to:
```
http://127.0.0.1:5000/
```

You should see the sign-in form on the home page.

## Application Overview

### Templates

- `base.html`: Contains the base template with a navigation bar including links to Home and Report pages.
- `index.html`: Contains the sign-in form. The form checks password requirements and stores the data in an SQLite3 database if the password meets the requirements. Upon successful sign-in, the user is redirected to the report page.
- `report.html`: Displays a success message after a successful sign-in. It also includes a "View Users" button to display a list of users stored in the database.
- `view_users.html`: Displays a list of users retrieved from the SQLite3 database.

## Additional Notes

- Ensure that you have Python 3.x installed on your system.
- The `venv` directory contains the virtual environment and should not be modified directly.
- You can add additional dependencies by using pip to install them within the virtual environment.

