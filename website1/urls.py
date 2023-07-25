from django.urls import path
from .views import home_page, login, register, introduction, retrieve, booking,b_status,feed,feedbackhandle

urlpatterns = [
    path('', home_page, name='home'),
    path('login',login, name='login'),
    path('register',register, name='register'),
    path('intro1',introduction, name='intro'),
    path('fetch',retrieve,name='RET'),
    path('room_book',booking,name='book'),
    path('bookingstatus',b_status,name='BST'),
    path('feed',feed,name='FDB'),
    path('fdbhandle',feedbackhandle,name='FDBHNDLE'),
]