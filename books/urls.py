from django.urls import path

from books.views import get_uuids_a, get_uuids_b, get_image, get_button, get_argument_from_path, \
    get_argument_from_query, check_http_query_type, get_headers, raise_error_for_fun, get_search_book, \
    AuthorListBaseView, CategoryListTemplateView, BooksListView, BookDetailsView, CategoryCreateFormView

urlpatterns = [
    path('uuid-a', get_uuids_a),
    path('uuid-b', get_uuids_b),
    path('image', get_image),
    path('button', get_button),
    path('path-args/<int:x>/<str:y>/<slug:z>/', get_argument_from_path, name="get_from_path"),
    path('path-query', get_argument_from_query, name="get_from_query"),
    path('path-type', check_http_query_type, name="check_http_query_type"),
    path('get-headers', get_headers, name="get_headers"),
    path('raise-error', raise_error_for_fun, name="raise_error_for_fun"),
    path('search_book', get_search_book),
    path('author-list', AuthorListBaseView.as_view(), name='author_list'),
    path('category-list', CategoryListTemplateView.as_view(), name='category_list'),
    path('books-list', BooksListView.as_view(), name='books_list'),
    path('book-details/<int:pk>', BookDetailsView.as_view(), name='books_details'),
    path('category-create', CategoryCreateFormView.as_view(), name='category_create'),


]
