# Social Media API

## Authentication Features 
- User Registration
- User Login with Token Authentication
- User Profile Management
- Token Retrieval for Authenticated Users


## API Endpoints

### 1️⃣ **User Registration**
- **Endpoint:** `/api/accounts/register/`
- **Method:** `POST`
- **Description:** Creates a new user account and returns an authentication token.

#### **Request Body:**
```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "securepassword"
}
```

#### **Response:**
```json
{
    "message": "User testuser registered successfully",
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "bio": "",
        "profile_picture": null
    },
    "token": "your_auth_token_here"
}
```

---

### 2️⃣ **User Login**
- **Endpoint:** `/api/accounts/login/`
- **Method:** `POST`
- **Description:** Authenticates a user and returns a token.

#### **Request Body:**
```json
{
    "username": "testuser",
    "password": "securepassword"
}
```

#### **Response:**
```json
{
    "message": "User logged in successfully",
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "bio": "",
        "profile_picture": null
    },
    "token": "your_auth_token_here"
}
```

---

### 3️⃣ **User Profile** (Retrieve & Update)
- **Endpoint:** `/api/accounts/profile/`
- **Methods:** `GET`, `PATCH`
- **Authentication:** `Token`
- **Description:** Allows authenticated users to retrieve or update their profile.

#### **Request Headers:**
```http
Authorization: Token your_auth_token_here
```

#### **GET Response:**
```json
{
    "id": 1,
    "username": "testuser",
    "email": "test@example.com",
    "bio": "Hello, this is my bio!",
    "profile_picture": null
}
```

#### **PUT Request Body (Update Profile):**
```json
{
    "bio": "Updated bio info",
    "profile_picture": "image_url"
}
```

#### **Response:**
```json
{
    "id": 1,
    "username": "testuser",
    "email": "test@example.com",
    "bio": "Updated bio info",
    "profile_picture": "image_url"
}
```

---

### 4️⃣ **Token Retrieval** (Get Token for Authenticated Users)
- **Endpoint:** `/api/accounts/get-token/`
- **Method:** `GET`
- **Authentication:** `Token`
- **Description:** Retrieves the token of the authenticated user.

#### **Request Headers:**
```http
Authorization: Token your_auth_token_here
```

#### **Response:**
```json
{
    "token": "your_auth_token_here"
}
```

---

## Authentication Instructions

All endpoints (except registration and login) require authentication via **Token Authentication**.

### **How to Authenticate Requests**

For endpoints that require authentication, include the **Authorization** header in your requests:
```http
Authorization: Token your_auth_token_here
```

Example using **Postman or cURL:**
```bash
curl -H "Authorization: Token your_auth_token_here" \
     -H "Content-Type: application/json" \
     -X GET http://127.0.0.1:8000/api/accounts/profile/
```

