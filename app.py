from flask import Flask, render_template, request,jsonify

app = Flask(__name__)
API_KEY = "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"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    print("1")
    # Get JSON data from the request
    data = request.get_json()
    
    # Extract username and password
    username = data.get('username')
    password = data.get('password')
    print(username)
    print(password)
    # Validate input
    if not username or not password:
        return jsonify({
            'success': False, 
            'message': 'Username and password are required'
        }), 400
    
    # Add your authentication logic here
    # For example, check against a database
    if username == 'admin' and password == 'password':
        return jsonify({
            'success': True, 
            'message': 'Login successful'
        })
    else:
        return jsonify({
            'success': False, 
            'message': 'Invalid credentials'
        }), 401
@app.route('/chat')
def fun():
    return render_template('g.html')

@app.route('/chat')
def chat_page():
    return render_template('g.html')

# New API Example: Using API Key for Authorization
@app.route('/api/send-message', methods=['POST'])
def send_message():
    # Get the API key from headers
    provided_api_key = request.headers.get('X-API-Key')
    
    # Check if the API key is valid
    if provided_api_key != API_KEY:
        return jsonify({
            'success': False,
            'message': 'Invalid API Key'
        }), 403
    
    # Get the message from request data
    data = request.get_json()
    message = data.get('message')
    
    if not message:
        return jsonify({
            'success': False,
            'message': 'Message content is required'
        }), 400
    
    # Process the message (e.g., store in a database, broadcast, etc.)
    return jsonify({
        'success': True,
        'message': 'Message received',
        'data': message
    })

if __name__ == '__main__':
    app.run(debug=True)