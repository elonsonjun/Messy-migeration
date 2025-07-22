🛠 Refactored User Management API

This project is a refactored version of a legacy Flask-based user management API, submitted as part of a company coding assignment.


---

📌 What Was Provided (Original System Overview)

A single file app.py handling all logic

No folder structure or separation of concerns

Passwords stored as plaintext in the DB

Raw SQL queries vulnerable to SQL injection

No data validation or error handling

No testing or security practices in place



---

✅ What I Changed (Refactoring Summary)

1. 🔐 Security Improvements

Before: Passwords stored in plain text

Now: Passwords hashed using bcrypt before storing in DB

Before: Queries like SELECT * FROM users WHERE id = '1' allowed SQL injection

Now: All queries use parameterized inputs, e.g.:

cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))


2. 📦 Code Structure and Modularity

Moved logic into modular folders:

├── routes/        # Flask Blueprints for user-related APIs
├── utils/         # Helper functions (e.g. password hashing)
├── database/      # DB connection handler
├── tests/         # Test cases for endpoints

Easier to maintain and debug by following separation of concerns


3. 🧪 Testing

Added a test file using Flask’s test client:

def test_create_user():
    response = app.test_client().post('/users', json={
        "name": "Test",
        "email": "test@example.com",
        "password": "testpass"
    })
    assert response.status_code == 201

Validates that major endpoints like login, user creation work as expected


4. 🧱 Proper HTTP Status Codes and Validation

Replaced plain text error messages with proper JSON + status codes:

return jsonify({"error": "User not found"}), 404

Added checks for missing parameters and incorrect types


5. 📄 Documentation

Added a detailed CHANGES.md for transparency

This README.md explains functionality and decisions clearly



---

🔄 Application Flow (Diagram)

flowchart TD
  A[User sends API request] --> B[Flask receives request]
  B --> C[Routes defined in routes/users.py]
  C --> D[Database accessed via database/connection.py]
  C --> E[Passwords handled via utils/security.py]
  D --> F[Response returned to client]


---

🚀 Getting Started

🔧 Prerequisites

Python 3.8 or above


▶ Run Locally

pip install -r requirements.txt
python init_db.py
python app.py

Visit: http://localhost:5009


---

🔗 API Endpoints

Method	Endpoint	Description

GET	/	Health check
GET	/users	List all users
GET	/user/<id>	Get user by ID
POST	/users	Create a new user
PUT	/user/<id>	Update a user
DELETE	/user/<id>	Delete a user
GET	/search?name=	Search users by name
POST	/login	User login/authentication



---

✅ Sample API Request (Before vs After)

🔴 Before (Insecure)

cursor.execute(f"SELECT * FROM users WHERE id = '{user_id}'")

✅ After (Secure)

cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))


---

📦 Tech Stack

Flask (Backend Framework)

SQLite (Lightweight DB)

bcrypt (Password Security)

Pytest (Minimal testing)



---

📬 Submission Notes

This project was completed within a 3-hour time window, as required.

Used AI (ChatGPT) as a code assistant for structure planning and error handling tips. All logic, testing, and decisions were personally reviewed and implemented.


---

🧠 Author

Sonjun Murthy
B.Tech – AI & ML Specialization
