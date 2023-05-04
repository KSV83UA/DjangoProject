from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.dates import DateMixin

from .models import *
from .forms import *


def manager_cabinet(request):
    print(request)
    if request.method == 'POST':
        form = UpdateOrder(request.POST)
        if form.is_valid():
            value = Clients.objects.get(id=request.POST.get('pk'))
            value.count_of_people = request.POST.get('count_of_people')
            value.status_id = request.POST.get('status')
            value.save()
            return redirect('manager_cabinet')
    form = UpdateOrder()

    order = Clients.objects.all()
    status = Status.objects.all()
    context = {
        'order': order,
        'status': status,
        'form': form
    }

    return render(request, 'main_app/manager_cabinet.html', context=context)


def index(request):

    menu_site = list()
    a = Menu.objects.filter(is_visible=True)
    for i in a:
        item = dict()
        item['menu'] = i
        item['dishes'] = Dishes.objects.filter(menu__title=i.title)
        menu_site.append(item)
    events = Events.objects.filter(is_visible=True)
    chief = Chief.objects.filter(is_visible=True)

    if request.method == 'POST':
        form = AddOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddOrderForm()


   # galery = Galery.objects.filter(is_visible=True)

    context = {
        'menu': menu_site,
        'events': events,
        'chief': chief,
        'form': form
    }
    return render(request, 'main_app/index.html', context=context)



class RegisterUser(CreateView, DateMixin):
    form_class = RegisterUserForm
    template_name = 'main_app/manager_register.html'
    success_url = reverse_lazy('login')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Регистрація")
    #     return dict(list(context.items()) + list(c_def.items()))
    #
    # def get_user_context(self, title):
    #     pass


class LoginUser(DateMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main_app/manager_login.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title="Авторизація")
    #     return dict(list(context.items()) + list(c_def.items()))
    #
    # def get_user_context(self, title):
    #     pass

    def get_success_url(self):
        return reverse_lazy('manager_cabinet')


def logout_user(request):
    logout(request)
    return redirect('home')
