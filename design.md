# Key REST "Standards" or Principles

## 1. Resource-Oriented
Everything is a **resource**, identified by a unique URL.

**Example:**
- `/users` → a collection of users  
- `/users/123` → a specific user with ID 123

---

## 2. Standard HTTP Methods
REST uses the standard HTTP methods to operate on resources:

| Method | Usage               |
|--------|---------------------|
| GET    | Retrieve a resource |
| POST   | Create a new resource |
| PUT    | Replace a resource  |
| PATCH  | Partially update    |
| DELETE | Delete a resource   |

---

## 3. Stateless
Each request must contain **all the information** needed to process it.

The server does **not store session state** — no implicit context.

---

## 4. Use of Standard HTTP Status Codes
RESTful APIs use HTTP status codes to indicate the result of a request:

| Code | Meaning         |
|------|-----------------|
| 200  | OK              |
| 201  | Created         |
| 204  | No Content      |
| 400  | Bad Request     |
| 401  | Unauthorized    |
| 403  | Forbidden       |
| 404  | Not Found       |
| 500  | Server Error    |

---

## 5. Data Format (Usually JSON)
REST APIs often use **JSON** (though technically any format like XML, HTML, etc. is allowed).

Content is negotiated using headers:

```http
Accept: application/json
Content-Type: application/json
