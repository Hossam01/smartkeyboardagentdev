from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View

from api.models import Advertiser
from .forms import *


class IndexView(View):
    template_name = 'advertiser/dashboard/index.html'

    def get(self, request):
        return render(request, 'advertiser/dashboard/index.html')

    def post(self, request):
        pass

    def logout(self, request):
        del request.session['username']
        return render(request, 'advertiser/login.html')


class DashboardView(View):
    template_name = 'advertiser/dashboard/index.html'

    def get(self, request):
        dash = Advertisement.objects.filter(name="Hossam").count()
        context = {'dash': dash}

        return render(request, 'advertiser/dashboard/index.html', context)


class ContactView(View):
    template_name = 'advertiser/website/contact.html'

    def get(self, request):
        return render(request, 'advertiser/website/contact.html')


def index(request):
    return render(request, 'advertiser/website/index.html', {'username': 'Moamen'})


class FormsView(View):
    template_name = 'advertiser/dashboard/forms.html'

    def get(self, request):
        return render(request, 'advertiser/dashboard/forms.html')

    def post(self, request):
        pass


class ChartsView(View):
    template_name = 'advertiser/dashboard/charts.html'

    def get(self, request):
        stuents = Advertisement.objects.filter(name="Hossam").count()
        context = {'stuents': stuents}
        return render(request, 'advertiser/dashboard/charts.html', context)

    def post(self, request):
        pass


def logout(request):
    del request.session['username']
    return render(request, 'advertiser/login.html')


class HomeView(View):
    template_name = 'advertiser/website/index.html'

    def get(self, request):
        return render(request, 'advertiser/website/index.html')

    def post(self, request):
        pass


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'advertiser/login.html'

    def get(self, request):
        # if request.session['username'] is None:
        form = LoginForm(None)
        context = {'form': form}
        return render(request, 'advertiser/login.html', context)

    # else:
    #   return redirect('home')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            if Advertiser.objects.filter(name=form.cleaned_data['username']).exists():
                advertiser = Advertiser.objects.get(name=form.cleaned_data['username'])
                if check_password(form.cleaned_data['password'], advertiser.password):
                    request.session['username'] = advertiser.pk
                    return redirect('advertiser/dashboard')
                else:
                    form = LoginForm(None)
                    context = {'form': form, 'msg': 'Incorrect password.'}
                    return render(request, 'advertiser/login.html', context)
            else:
                form = LoginForm(None)
                context = {'form': form, 'msg': 'Username does not exist.'}
                return render(request, 'advertiser/login.html', context)
        else:
            form = LoginForm(None)
            return render(request, 'advertiser/login.html', {'form': form, 'msg': 'Invalid form fml'})


class RegistrationFormView(View):
    form_class = RegistrationForm
    template_name = 'advertiser/registration.html'

    def get(self, request):
        form = RegistrationForm(None)
        context = {'form': form}
        return render(request, 'advertiser/registration.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():

            if not Advertiser.objects.filter(name=form.cleaned_data['username']).exists():
                if form.cleaned_data['password'] == form.cleaned_data['confirmpassword']:
                    name = form.cleaned_data['username']
                    email = form.cleaned_data['email']
                    password = make_password(form.cleaned_data['password'])
                    phone = form.cleaned_data['phone']
                    Advertiser.objects.create(name=name, email=email, password=password, phone=phone, budget=50)
                    messages.success(request, "Your account has been registered successfully!")
                    return redirect('advertiser/login')
                else:
                    form = RegistrationForm(None)
                    messages.error(request, 'Password does not match')
                    return render(request, 'advertiser/registration.html',
                                  {'form': form})

            else:
                form = RegistrationForm(None)
                messages.error(request, 'Account with the same username already exists')
                return render(request, 'advertiser/registration.html',
                              {'form': form})


class AdvertisersListView(generic.ListView):
    model = Advertiser
    template_name = 'advertiser/index.html'

    def get_queryset(self):
        return Advertiser.objects.all()


class AdvertisementDetailView(generic.DeleteView):
    model = Advertisement


class AddAdvertisementView(View):
    form_class = AdvertisementForm

    def get(self, request):
        form = AdvertisementForm(None)
        return render(request, 'advertiser/add_advertisement.html', {'form': form})

    def post(self, request):
        pass


class AdvertisementFormView(View):
    form_class = Userinput
    template_name = 'advertiser/dashboard/forms.html'

    def get(self, request):
        form = Userinput(None)
        context = {'form': form}
        return render(request, 'advertiser/dashboard/forms.html', context)


    def post(self, request):
        form = Userinput(request.POST)
        if form.is_valid():
            if 'username' in request.session:
                username = request.session['username']
                hoss = Advertiser.objects.get(id=username)
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            pub_date = form.cleaned_data['pub_date']
            max_age = form.cleaned_data['max_age']
            min_age = form.cleaned_data['min_age']
            category = form.cleaned_data.get('category')
            Advertisement.objects.create(name=name, description=description, pub_date=pub_date, advertiser=hoss)
        if request.POST.get('delete'):
            nameads=form.cleaned_data.get('advertisement')
            Advertisement.objects.get(name=nameads).delete()
        if request.POST.get('update'):
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            pub_date = form.cleaned_data['pub_date']
            nameads = form.cleaned_data.get('advertisement')
            Advertisement.objects.filter(name=nameads).update(name=name,description=description,pub_date=pub_date)
        newform = Userinput(None)
        return render(request, 'advertiser/dashboard/forms.html', {'form': newform})


def Student(request):
    stuents = Advertisement.objects.filter(name="Hossam").count()
    context = {'stuents': stuents}
    return render(request, 'advertiser/dashboard/charts.html', context)

def Index(request):
    stuents = Advertisement.objects.filter(name="Hossam").count()
    context = {'stuents': stuents}
    return render(request, 'advertiser/dashboard/index.html', context)
