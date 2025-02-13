from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('books/', list_books, name="list_books"),
    path("books_detail/<int:pk>/", BookDetail.as_view(), name="book_detail"),
    path('books/create', create_book, name="book-create"),
    path('home/', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)