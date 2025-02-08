from django.contrib import admin

# Register your models here.
from .models import Post  # Import the Task model

# Register your models here.
admin.site.register(Post)  # Register the Task model
