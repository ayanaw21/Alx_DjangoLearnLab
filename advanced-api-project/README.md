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

  ## API Filtering, Searching and Ordering

### Filtering
- Filter by exact title: `/api/books/?title=Example`
- Filter by publication year: `/api/books/?publication_year=2020`
- Filter by year range: `/api/books/?publication_year__gt=2000&publication_year__lt=2020`
- Filter by author name: `/api/books/?author=John`

### Searching
- Search across title and author fields: `/api/books/?search=Science`

### Ordering
- Order by field: `/api/books/?ordering=title` (ascending)
- Order by field descending: `/api/books/?ordering=-publication_year`
- Multiple fields: `/api/books/?ordering=title,publication_year`