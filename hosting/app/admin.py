# from django.contrib import admin
# from app.models import register_user,post
# from django.contrib.auth import get_user_model

# # user =  get_user_model()

# # admin.site.register(user) 
# # # Register your models here
# # class UserAdmin(admin.ModelAdmin):
# #     search_fields = ['email']
# #     class Meta:
# #         model = user

# # admin.site.register(user, UserAdmin)

# # class GuestEmailAdmin(admin.ModelAdmin):
# #     search_fields = ['email']
# #     class Meta:
# #         model = GuestEmail 
 
# # admin.site.register(GuestEmail, GuestEmailAdmin)




# admin.site.register(register_user) #before custom auth
# # admin.site.social_media_new(post)







from django.contrib import admin
# from app.models import AppRegisterUser

# # Register your models here

# admin.site.register(AppRegisterUser)

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields =['email', 'username']
    form=UserAdminChangeForm
    add_form = UserAdminCreationForm
# admin.site.unregister(User)

admin.site.register(User, UserAdmin)
