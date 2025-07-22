# CHANGES.md

## Major Issues Identified

1. **SQL Injection Vulnerability**
   - Original code used f-strings for SQL queries.
   - Fixed using parameterized queries (`?` placeholders).

2. **Insecure Password Storage**
   - Plaintext passwords were stored in the database.
   - Passwords are now hashed using bcrypt.

3. **Poor Code Structure**
   - All logic was in `app.py`.
   - Refactored into modular structure: `routes/`, `utils/`, `database/`.

4. **Lack of Input Validation and Error Handling**
   - Added try/except and checks for missing fields in requests.

5. **No HTTP Status Codes**
   - Implemented appropriate status codes (e.g., 201, 400, 404, 401).

## Tools Used
- **Flask** for web routing
- **bcrypt** for password security
- **Python's sqlite3** for DB connection

## Trade-offs / Assumptions
- Did not include ORM (like SQLAlchemy) to keep it simple.
- Password hashes were added, but existing plain-text seeds still exist for demo.

## Future Work
- Add full testing suite
- Use environment variables for config
- Use Blueprints for other modules

