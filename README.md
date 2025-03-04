# Bookshop

## Overview
Bookshop is an online platform designed to manage and sell books efficiently. This project provides functionality for book listings, user authentication, and order management.

## Features
- **User Authentication**: Users can sign up, log in, and manage their accounts.
- **Book Management**: Add, edit, and remove books from the store.
- **Order System**: Users can purchase books and track their orders.
- **Admin Panel**: Admin users can manage books, orders, and customers.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Version Control**: Git & GitHub

## Database Configuration
This project uses **PostgreSQL** as the primary database. To configure the database:
1. Install PostgreSQL if you haven't already.
2. Create a new database:
   ```sql
   CREATE DATABASE bookshop;
   ```
3. Update the `settings.py` file with the PostgreSQL configuration:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'bookshop',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

## Managing Books with Django Admin
Django provides a built-in admin panel to manage books efficiently. To use it:
1. Register the `Book` model in `admin.py`:
   ```python
   from django.contrib import admin
   from .models import Book

   @admin.register(Book)
   class BookAdmin(admin.ModelAdmin):
       list_display = ('title', 'author', 'price', 'available')
       search_fields = ('title', 'author')
       list_filter = ('available',)
   ```
2. Log in to the Django admin panel at `/admin/` using your superuser credentials.
3. Navigate to the **Books** section to add, edit, or remove books.

## Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:SHOXAKONG/Bookshop.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Bookshop
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Visit `http://127.0.0.1:8000/` in your browser.
- Register an account or log in.
- Browse available books and add them to your cart.
- Place orders and manage them from your dashboard.
- Admin users can log in at `/admin/` to manage books and orders.

## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or suggestions, feel free to reach out at [your email or GitHub profile].
