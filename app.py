from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

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



if __name__ == '__main__':
    app.run(debug=True)