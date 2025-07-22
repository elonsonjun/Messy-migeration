import json
from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"User Management System" in response.data

def test_create_user():
    client = app.test_client()
    response = client.post('/users', json={
        "name": "Test User",
        "email": "testuser@example.com",
        "password": "password"
    })
    assert response.status_code == 201

def test_login_fail():
    client = app.test_client()
    response = client.post('/login', json={
        "email": "nonexist@example.com",
        "password": "wrongpass"
    })
    assert response.status_code == 401
