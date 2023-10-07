from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import (ProfileUpdateView, RulesTemplateView, UserLoginView,
                         UserRegistrationView, basket_add)

app_name = 'users'

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', login_required(ProfileUpdateView.as_view()), name='profile'),
    path('rules/', RulesTemplateView.as_view(), name='rules'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
]
