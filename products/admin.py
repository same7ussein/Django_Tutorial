from itertools import product
from django.contrib import admin
from .models import Products,Test
# Register your models here.
admin.site.register(Products)
admin.site.register(Test)
admin.site.site_header='MyBlog'
admin.site.site_title='MyBlog'