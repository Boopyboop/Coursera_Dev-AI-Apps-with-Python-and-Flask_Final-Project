
# Coursera_Dev-AI-Apps-with-Python-and-Flask_Final-Project

🧪 This repository is my personal workspace for realising the final project of the course **"Developing AI Applications with Python and Flask"** by IBM on Coursera.  
[Course link](https://www.coursera.org/learn/python-project-for-ai-application-development)

---

## Prerequisites

- Python 3.7 or higher installed  
- Git (optional, to clone the repo)  
- (Recommended) Use a virtual environment to manage dependencies  

---

## Setup Instructions

### 1. Clone the repository (if you haven't already)

```bash
git clone https://github.com/Boopyboop/Coursera_Dev-AI-Apps-with-Python-and-Flask_Final-Project.git
```

### 2. Create and activate a virtual environment

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

Make sure you have the `requirements.txt` file in the root directory.

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

Create a `.env` file in the root directory to set environment variables for Flask:

```
FLASK_APP=app
FLASK_ENV=development
```

---

### 5. Run the Flask application

Run the Flask development server with:

```bash
flask --app app --debug run
```

Or simply:

```bash
flask run
```

(if your `.env` is configured properly)

The server will start, and you can access the app at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## Application Routes

- `/`  
  Returns a simple HTML greeting message.

- `/json`  
  Returns a JSON response with a greeting message.

---

## Notes

- Remember to **activate your virtual environment** every time before working on the project.  
- Use the `.env` file to configure environment variables instead of setting them manually.  
- To stop the server, press `Ctrl+C` in the terminal.

---

## License

This project is for educational purposes, based on the IBM Coursera course content.
