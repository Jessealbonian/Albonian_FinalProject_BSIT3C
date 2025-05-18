# Library Management System - User Authentication API

## API Endpoints

### 1. Register a New User
- **Method:** POST
- **Endpoint:** `/api/auth/register/`
- **Headers:**
  - `Content-Type: application/json`
- **Request Body:**
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "StrongPass123!",
  "password2": "StrongPass123!"
}
```
- **Sample Response:**
```json
{
  "message": "User  registered successfully.",
  "user": {
    "username": "testuser",
    "email": "test@example.com"
  }
}
```

---

### 2. Login (Obtain JWT Token)
- **Method:** POST
- **Endpoint:** `/api/auth/login/`
- **Headers:**
  - `Content-Type: application/json`
- **Request Body:**
```json
{
  "username": "testuser",
  "password": "StrongPass123!"
}
```
- **Sample Response:**
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>"
}
```

---

### 3. Access Protected Route
- **Method:** GET
- **Endpoint:** `/api/auth/protect/`
- **Headers:**
  - `Authorization: Bearer <access_token>`
- **Sample Response (Success):**
```json
{
  "message": "Hello, testuser!"
}
```
- **Sample Response (Unauthorized):**
```json
{
  "detail": "Authentication credentials were not provided."
}
```

---

### 4. Refresh Token
- **Method:** POST
- **Endpoint:** `/api/auth/token/refresh/`
- **Headers:**
  - `Content-Type: application/json`
- **Request Body:**
```json
{
  "refresh": "<refresh_token>"
}
```
- **Sample Response:**
```json
{
  "access": "<new_access_token>"
}
```

---

## Notes
- All endpoints are prefixed with `/api/auth/`.
- Use the `access` token in the `Authorization` header as `Bearer <access_token>` for protected routes.
- Replace `<access_token>` and `<refresh_token>` with the actual tokens received from the login endpoint.
