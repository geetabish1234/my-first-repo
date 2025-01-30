from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Function to validate the strength of a password
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[\W_]', password):  # \W matches any non-word character
        return False
    return True

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Check if the password is strong
    if not is_strong_password(password):
        return jsonify({"error": "Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character."}), 400

    # Here you can add the logic to save the user to the database
    # For example:
    # save_user_to_db(username, password)
    
    return jsonify({"message": "User signed up successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
