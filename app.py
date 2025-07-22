from flask import Flask
from routes.users import users_bp

app = Flask(__name__)
app.register_blueprint(users_bp)

@app.route('/')
def home():
    return "User Management System"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)
