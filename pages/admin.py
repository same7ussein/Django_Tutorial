from itertools import product
from django.contrib import admin
from .models import Female,Male,User,Product,UserName,Video,Login
# one to one 
admin.site.register(Female)
admin.site.register(Male)

# one to many
admin.site.register(User)
admin.site.register(Product)

# many to many
admin.site.register(UserName)
admin.site.register(Video)

# login
admin.site.register(Login)
