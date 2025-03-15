# Flask Demo App

This is a simple Flask application with a structured setup.

## Features
- Homepage with a form
- API endpoint returning a JSON response
- Simple Flask routing
- Organized folder structure

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/anubhavanand1516/flask_demo.git
   ```
2. Navigate to the project directory:
   ```sh
   cd flask_demo
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```sh
   python main.py
   ```
5. Open in your browser:
   ```
   http://127.0.0.1:5000/
   ```
   <img width="466" alt="Screenshot 2025-03-15 at 3 05 46 PM" src="https://github.com/user-attachments/assets/17ad90b2-a673-400f-ba51-91a711bd51c1" />

   

## Folder Structure
```
flask_demo/
│── main.py                # Main Flask application
│── requirements.txt       # Dependencies (Flask, etc.)
│── README.md             # Project documentation
│── templates/
│   └── index.html         # HTML template for the homepage
```

## API Endpoints
- `GET /api/data` - Returns a JSON response with a message.

