from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"
    
@app.route('/api/hello')
def hello():
    return "Hello from Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
#http://localhost:5051/ﬁ