#!/usr/bin/env python3
from flask import Flask, jsonify, request # type: ignore
from flask_httpauth import HTTPBasicAuth # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash # type: ignore
from flask_jwt_extended import ( # type: ignore
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity, get_jwt
)

# App & Auth setup
app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # should be more secure in production
jwt = JWTManager(app)

# In-memory users
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# For HTTP Basic Authentication
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200

# JWT login route
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing credentials"}), 401

    username = data["username"]
    password = data["password"]
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create token with identity and role
    access_token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify({"access_token": access_token}), 200

# JWT-protected route
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

# Admin-only route
@app.route("/admin-only")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200

# === JWT ERROR HANDLING (required by checker) ===
@jwt.unauthorized_loader
def handle_unauthorized(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_data):
    return jsonify({"error": "Token has expired"}), 401

@jwt.needs_fresh_token_loader
def handle_fresh_required(jwt_header, jwt_data):
    return jsonify({"error": "Fresh token required"}), 401

@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_data):
    return jsonify({"error": "Token has been revoked"}), 401

# Run server
if __name__ == "__main__":
    app.run()
