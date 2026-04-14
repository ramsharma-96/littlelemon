# Little Lemon Restaurant API

A Django REST API for managing restaurant operations including menu items and table bookings.

## Features

- **Menu Management**: Create, read, update, and delete menu items with pricing and inventory tracking
- **Booking System**: Manage restaurant table reservations with guest information
- **Authentication**: Token-based authentication for secure API access
- **Admin Interface**: Django admin panel for administrative tasks
- **RESTful API**: Full CRUD operations via REST endpoints

## Tech Stack

- **Backend**: Django 6.0.3
- **API Framework**: Django REST Framework
- **Authentication**: Djoser + Token Authentication
- **Database**: MySQL

## Installation

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Setup

1. **Clone the repository** (if applicable) or navigate to the project directory

2. **Create a virtual environment**:
   ```bash
   python -m venv env_littlelemon
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     env_littlelemon\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source env_littlelemon/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install django djangorestframework djoser
   ```

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication

- `POST /auth/users/` - Register a new user
- `POST /auth/token/login/` - Login and get authentication token
- `POST /auth/token/logout/` - Logout (requires authentication)

### Menu Items

- `GET /api/restaurant/menu-items/` - List all menu items (requires authentication)
- `POST /api/restaurant/menu-items/` - Create a new menu item (requires authentication)
- `GET /api/restaurant/menu-items/{id}/` - Get a specific menu item (requires authentication)
- `PATCH /api/restaurant/menu-items/{id}/` - Update a menu item (requires authentication)
- `DELETE /api/restaurant/menu-items/{id}/` - Delete a menu item (requires authentication)

### Bookings

- `GET /api/restaurant/bookings/table/` - List all bookings (requires authentication)
- `POST /api/restaurant/bookings/table/` - Create a new booking (requires authentication)
- `GET /api/restaurant/bookings/table/{id}/` - Get a specific booking (requires authentication)
- `PATCH /api/restaurant/bookings/table/{id}/` - Update a booking (requires authentication)
- `DELETE /api/restaurant/bookings/table/{id}/` - Delete a booking (requires authentication)

### Admin Interface

- Access the Django admin at `http://127.0.0.1:8000/admin/`

## Usage Examples

### Authentication

1. **Register a user**:
   ```bash
   curl -X POST http://127.0.0.1:8000/auth/users/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass123"}'
   ```

2. **Login to get token**:
   ```bash
   curl -X POST http://127.0.0.1:8000/auth/token/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass123"}'
   ```

   Response will include a token like: `{"auth_token": "your-token-here"}`

3. **Use the token for authenticated requests**:
   ```bash
   curl -H "Authorization: Token your-token-here" \
     http://127.0.0.1:8000/api/restaurant/menu-items/
   ```

### Menu Items

**Create a menu item**:
```bash
curl -X POST http://127.0.0.1:8000/api/restaurant/menu-items/ \
  -H "Authorization: Token your-token-here" \
  -H "Content-Type: application/json" \
  -d '{"title": "Margherita Pizza", "price": "12.99", "inventory": 50}'
```

**Get all menu items**:
```bash
curl -H "Authorization: Token your-token-here" \
  http://127.0.0.1:8000/api/restaurant/menu-items/
```

### Bookings

**Create a booking**:
```bash
curl -X POST http://127.0.0.1:8000/api/restaurant/bookings/table/ \
  -H "Authorization: Token your-token-here" \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "no_of_guests": 4, "booking_date": "2024-12-25"}'
```

## Data Models

### MenuItem
- `title` (string): Name of the menu item
- `price` (decimal): Price of the item
- `inventory` (integer): Quantity available

### Booking
- `name` (string): Name of the person making the booking
- `no_of_guests` (integer): Number of guests
- `booking_date` (date): Date of the booking

## Development

### Running Tests

```bash
python manage.py test
```

### Code Style

This project follows Django's coding standards and best practices.
