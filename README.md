A simple Blog web application built with Django. This app allows users to create, edit, delete, and view blog posts.

Features
Create new blog posts

Edit existing blog posts

Delete blog posts

View blog posts

Installation
Clone the repository:

bash
git clone https://github.com/your_username/django-blog-app.git
cd django-blog-app
Create and activate a virtual environment:

bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
pip install -r requirements.txt
Run migrations:

bash
python manage.py makemigrations
python manage.py migrate
Register the Post model in admin.py:

python
from django.contrib import admin
from .models import Post  # Import the Post model

# Register your models here.
admin.site.register(Post)  # Register the Post model
Create a superuser:

bash
python manage.py createsuperuser --username Tanjim --email admin@example.com
# When prompted, enter the password: 123
Start the development server:

bash
python manage.py runserver
Access the application: Open your web browser and go to http://127.0.0.1:8000/

Admin interface: http://127.0.0.1:8000/admin/

Username: Tanjim

Password: 123

Project Structure
blog_project/: Project settings and configuration.

blog/: Contains the app for managing blog posts.

models.py: Defines the Post model.

views.py: Handles the application logic for posts.

forms.py: Defines the Post form.

admin.py: Registers the Post model with the admin site.

templates/blog/: HTML templates for the app.

Usage
Creating a Post
Go to the main page.

Click on "Create New Post".

Fill out the post form and click "Save".

Viewing a Post
Go to the main page.

Click on the post title to view its details.

Editing a Post
Go to the post detail page.

Click on the "Edit" button.

Update the post details and click "Save".

Deleting a Post
Go to the post detail page.

Click on the "Delete" button.
