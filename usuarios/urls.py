from django.urls import path
from .views import login_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),          # /login/
    path('logout/', logout_view, name='logout'), # /login/logout/
]
