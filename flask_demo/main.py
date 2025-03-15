from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('user_input', '')
    return f"You submitted: {data}"

@app.route('/api/data', methods=['GET'])
def api_data():
    return jsonify({"message": "Hello, Flask!", "status": "success"})

if __name__ == '__main__':
    app.run(debug=True)