from django.contrib import admin
from .models import User
from .models import Contact
from .models import Data
# Register your models here.

admin.site.register(User)

admin.site.register(Contact)

admin.site.register(Data)
