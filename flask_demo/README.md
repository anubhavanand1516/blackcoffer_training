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

## Folder Structure
```
flask_demo_app/
│── main.py                # Main Flask application
│── requirements.txt       # Dependencies (Flask, etc.)
│── README.md             # Project documentation
│── templates/
│   └── index.html         # HTML template for the homepage
│── static/
│   ├── css/
│   │   └── style.css      # Stylesheets
│   ├── js/
│   │   └── script.js      # JavaScript files
│   └── images/            # Images (if needed)
```

## API Endpoints
- `GET /api/data` - Returns a JSON response with a message.

