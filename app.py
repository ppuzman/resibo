from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User: {username}'

@app.route('/add', methods=['POST'])
def add():
    data = request.form  # Assuming form data is being posted
    return f'Data received: {data}'

if __name__ == '__main__':
    app.run(debug=True)
