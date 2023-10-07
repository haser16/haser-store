from django.contrib.auth.views import LoginView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from products.models import Basket, Products
from users.forms import (UserAuthenticationForm, UserProfileForm,
                         UserRegistrationForm)
from users.models import Rules, User


# Registration page
class UserRegistrationView(TitleMixin, CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    title = 'Registration'


# Login page
class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserAuthenticationForm
    title = 'Login'


# Profile page
class ProfileUpdateView(TitleMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    title = 'Profile'
    form_class = UserProfileForm

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data()

        context['baskets'] = Basket.objects.filter(user=self.request.user)

        return context


# Rules page
class RulesTemplateView(TitleMixin, TemplateView):
    template_name = 'users/rules.html'
    title = 'Rules'

    def get_context_data(self, **kwargs):
        context = super(RulesTemplateView, self).get_context_data()

        context['rules'] = Rules.objects.all()

        return context


# Add product to basket
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
