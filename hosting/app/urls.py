"""hosting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views

"""for media"""
from django.conf import settings
from django.conf.urls.static import static



admin.site.site_header = "BlackBoard by Aryan & Aarya"
admin.site.site_title = "Aryan & Aarya's Project"
admin.site.index_title = "Welcome to BlackBoard....aap hi maalik ho"

urlpatterns = [
    path("", views.base, name ="base"),
    path("home", views.home, name="home"),
    path("register", views.register, name="register"),
    path("sstest", views.sstest, name="successful_entry"), #```this is for test only```
    path("search_book",views.search_book, name="search_book"),
    path("pyq", views.pyq, name="pyq"),
    path("sm_pg1", views.sm_pg1, name="sm_pg1"),
    path("sm_pg2", views.sm_pg2, name="sm_pg2"),
    path("sm_post", views.sm_post, name="sm_post"),
    path("succesfull_entry", views.succesfull_entry, name="succesfull_entry"),
    path("todo_fn", views.todo_fn, name="todo_fn"),
    path("addbook",views.addbook, name="addbook"),
    path("book_success",views.book_success, name="book_success"),
    path("books/<int:my_id>/",views.book_url_response),
    path('likes/<int:post_id>/', views.likes, name="likes"),
    path('dislikes/<int:post_id>/', views.dislikes, name="dislikes"),
    path("about_us", views.about_us, name="about_us"),
    path("book_transaction", views.book_transaction, name="book_transaction"),
    path("verification",views.verification, name="verification")
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)