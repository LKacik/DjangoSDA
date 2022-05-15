from msilib.schema import ListView
from uuid import uuid4

from django.contrib.auth.decorators import login_required
from django.core.exceptions import BadRequest, PermissionDenied
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from books.forms import CategoryForm, AuthorForm, BookForm
from books.models import BookAuthor, Category, Book
import logging

# Create your views here.
logger = logging.getLogger('lukasz')


class AuthorListBaseView(View):
    template_name = "author_list.html"
    queryset = BookAuthor.objects.all()  # type: ignore

    def get(self, request: WSGIRequest, *args, **kwargs):
        logger.debug(f"{request} DUPA!")
        context = {'authors': self.queryset}
        return render(request, template_name=self.template_name, context=context)


class CategoryListTemplateView(TemplateView):
    template_name = 'category_list.html'
    extra_context = {"categories": Category.objects.all()}


class BooksListView(ListView):
    template_name = 'books_list.html'
    model = Book
    paginate_by = 10


class BookDetailsView(DetailView):
    template_name = "book_detail.html"
    model = Book

    def get_object(self, queryset=None):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))


class CategoryCreateFormView(FormView):
    template_name = 'category_forms.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')

    def form_invalid(self, form):
        logger.critical(f"FORM CRITICAL ERROR, MORE INFO {form}.")
        return super().form_invalid(form)

    def form_valid(self, form):
        result = super().form_valid(form)
        logger.info(f"form = {form}")
        logger.info(f"form.cleaned_data = {form.cleaned_data}")  # cleaned means with removed html indicators
        check_entity = Category.objects.create(**form.cleaned_data)
        logger.info(f"check_entity-id={check_entity.id}")
        return result


class AuthorCreateView(CreateView):
    template_name = 'author_form.html'
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')


class AuthorUpdateView(UpdateView):
    template_name = 'author_form.html'
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')

    def get_object(self, **kwargs):
        return get_object_or_404(BookAuthor, id=self.kwargs.get("pk"))


class BookCreateView(CreateView):
    template_name = "book_form.html"
    form_class = BookForm
    success_url =  reverse_lazy("books_list")

# def get_success_url(self):
#     return reverse_lazy("book_list")

class BookUpdateView(UpdateView):
    template_name = "book_form.html"
    form_class = BookForm
    success_url = reverse_lazy("books_list")

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))

class BookDeleteView(DeleteView):
    template_name = "book_delete.html"
    model = Book
    success_url = reverse_lazy("books_list")

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))

@login_required
def get_hello(request: WSGIRequest) -> HttpResponse:
    user: Users = request.user  # type: ignore
    # password = None if user.is_anonymous else user.password
    # email = None if user.is_anonymous else user.email
    # date_joined = None if user.is_anonymous else user.date_joined
    #if not user.is_authenticated:
        # raise PermissionDenied()
        #return HttpResponseRedirect(reverse('login'))
    is_auth: bool = user.is_authenticated
    hello = f'Hello user name {user} your password is {user.password}, your email {user.email} and date joined :{user.date_joined}'

    return render(request, template_name='hello_world.html', context={'hello_var': hello, 'is_auth': is_auth})


def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return render(request, template_name='uuids.html', context={'elements': uuids})
    #return HttpResponse(f"{uuids}")


def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({"uuids": uuids})


def get_image(request: WSGIRequest) -> HttpResponse:
    return HttpResponse('<img src="https://images.pexels.com/photos/9197509/pexels-photo-9197509.jpeg" width="800" '
                        'height="600">')


def get_button(request: WSGIRequest) -> HttpResponse:
    return HttpResponse('<button type="button">Click Me!</button>')


def get_argument_from_path(request: WSGIRequest, x: int, y: str, z: str) -> HttpResponse:
    return HttpResponse(f"x= {x}, y= {y}, z= {z}")


def get_argument_from_query(request: WSGIRequest) -> HttpResponse:
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    print(type(a))
    return HttpResponse(f"a= {a}, b= {b}, c= {c}")


@csrf_exempt
def check_http_query_type(request: WSGIRequest) -> HttpResponse:
    # query_type = 'unknown'
    # if request.method == 'GET':
    #     query_type = 'This is GET'
    # elif request.method == 'POST':
    #     query_type = 'This is POST'
    # elif request.method == 'PUT':
    #     query_type = 'This is PUT'
    # elif request.method == 'DELETE':
    #     query_type = 'This is DELETE'
    # return HttpResponse(query_type)
    return render(request, template_name='methods.html', context={})


def get_headers(request: WSGIRequest) -> JsonResponse:
    our_headers = request.headers
    return JsonResponse({"headers": dict(our_headers)})


@csrf_exempt
def raise_error_for_fun(request: WSGIRequest) -> HttpResponse:
    if request.method != 'GET':
        raise BadRequest('method not allowed')
    return HttpResponse('wszystko ok')


def get_search_book(request: WSGIRequest) -> HttpResponse:
    return HttpResponse('https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes&key=AIzaSyDf4PhS2UH9ql0Pj1ImpGXY5jpddg-ZQ1o')

