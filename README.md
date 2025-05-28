# Library Management System API Documentation

## Authentication
All endpoints require authentication. Include the JWT token in the Authorization header:
```
Authorization: Bearer your_jwt_token
```

## Books API Endpoints

### List/Create Books
- **Method**: GET, POST
- **URL**: `/api/books/`
- **Headers**:
  ```
  Content-Type: application/json
  Authorization: Bearer your_jwt_token
  ```
- **GET Response**:
  ```json
  [
    {
      "id": 1,
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "category": 1,
      "status": "available",
      "date_added": "2024-03-19T10:00:00Z"
    }
  ]
  ```
- **POST Request Body**:
  ```json
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "category": 1,
    "status": "available"
  }
  ```

### Get/Update/Delete Book
- **Method**: GET, PUT, DELETE
- **URL**: `/api/books/<id>/`
- **Headers**:
  ```
  Content-Type: application/json
  Authorization: Bearer your_jwt_token
  ```
- **GET Response**:
  ```json
  {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "category": 1,
    "status": "available",
    "date_added": "2024-03-19T10:00:00Z"
  }
  ```
- **PUT Request Body**:
  ```json
  {
    "title": "Updated Title",
    "status": "borrowed"
  }
  ```

## Categories API Endpoints

### List/Create Categories
- **Method**: GET, POST
- **URL**: `/api/categories/`
- **Headers**:
  ```
  Content-Type: application/json
  Authorization: Bearer your_jwt_token
  ```
- **GET Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Fiction",
      "description": "Fictional literature"
    }
  ]
  ```
- **POST Request Body**:
  ```json
  {
    "name": "Fiction",
    "description": "Fictional literature"
  }
  ```

### Get/Update/Delete Category
- **Method**: GET, PUT, DELETE
- **URL**: `/api/categories/<id>/`
- **Headers**:
  ```
  Content-Type: application/json
  Authorization: Bearer your_jwt_token
  ```

## Borrow Logs API Endpoints

### List/Create Borrow Logs
- **Method**: GET, POST
- **URL**: `/api/borrow-logs/`
- **Headers**:
  ```
  Content-Type: application/json
  Authorization: Bearer your_jwt_token
  ```
- **GET Response**:
  ```json
  [
    {
      "id": 1,
      "book": 1,
      "borrower_name": "John Doe",
      "date_borrowed": "2024-03-19T10:00:00Z",
      "is_returned": false,
      "date_returned": null
    }
  ]
  ```
- **POST Request Body**:
  ```json
  {
    "book": 1,
    "borrower_name": "John Doe",
    "is_returned": false
  }
  ```

### Get/Update/Delete Borrow Log
- **Method**: GET, PUT, DELETE
- **URL**: `/api/borrow-logs/<id>/`
- **Headers**:
  ```
  Content-Type: application/json
  Authorization: Bearer your_jwt_token
  ```
- **GET Response**:
  ```json
  {
    "id": 1,
    "book": 1,
    "borrower_name": "John Doe",
    "date_borrowed": "2024-03-19T10:00:00Z",
    "is_returned": false,
    "date_returned": null
  }
  ```
- **PUT Request Body** (for returning a book):
  ```json
  {
    "is_returned": true
  }
  ```

## Query Parameters

### Books
- `?category=Fiction` - Filter by category name
- `?status=available` - Filter by status
- `?author=Smith` - Filter by author
- `?title=Python` - Filter by title

### Borrow Logs
- `?borrower=John` - Filter by borrower name
- `?is_returned=true` - Filter by return status

## Status Codes
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Server Error

## Error Responses
```json
{
  "error": "Error message description"
}
```
