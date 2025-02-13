from django.contrib import messages
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import *
from .forms import BookForm, LoginForm, RegistrationForm
from django.contrib.auth.hashers import make_password, check_password
from django.views.generic.detail import DetailView


class BookDetail(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'

class AuthorDetail(DetailView):
    model = Author
    template_name = 'book/book_detail.html'
    context_object_name = 'author'


def list_books(request):
    search = request.GET.get("search", "")
    filter_ = request.GET.get("order", "-id")

    books = Book.objects.all()

    if search:
        books = books.filter(
            Q(title__icontains=search)
        )
    books = books.order_by(filter_)

    return render(request, "book/books.html", {
        "books": books,
        "search": search,
        "filter_": filter_,
    })


def create_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            book = Book.objects.create(
                title=data['title'],
                author=data['author'],
                count=data['count']
            )
            return redirect('books')

    return render(request, 'book/book-create.html', {
        "form": form,
    })


def home(request):
    return render(request, 'main/home.html', )


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):  # Checking password
                    request.session['user_id'] = user.id
                    request.session['username'] = user.username
                    return redirect('home')
                else:
                    messages.error(request, "Invalid username or password")
            except User.DoesNotExist:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {
        "form": form
    })


def register_view(request):
    if request.method == 'GET':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(
                username=data['username'],
                firstname=data['firstname'],
                lastname=data['lastname'],
                password=make_password(data['password'])
            )
            return redirect('login')

    return render(request, 'login/register.html', {
        'form': form
    })

def logout(request):
    request.session.flush()
    return redirect('login')
