# Advanced API Project

## API Endpoints

### Books
- `GET /api/books/` - List all books
- `POST /api/books/` - Create a new book (Admin only)
- `GET /api/books/<id>/` - Retrieve a single book
- `PUT /api/books/<id>/` - Update a book (Admin only)
- `DELETE /api/books/<id>/` - Delete a book (Admin only)

### Authors
- `GET /api/authors/` - List all authors

## Permissions
- Read operations are allowed for all users
- Write operations require admin privileges

## Customizations
- Books can be filtered by publication year using the `year` query parameter
  Example: `/api/books/?year=2020`