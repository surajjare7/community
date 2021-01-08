from django.contrib import admin
from .models import Post
from . models import Query
from .models import Solution

# Register your models here.
admin.site.register(Post)
admin.site.register(Query)
# admin.site.register(Services)
# admin.site.register(Contact)
admin.site.register(Solution)