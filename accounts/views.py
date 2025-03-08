from django.shortcuts import render
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import  User
from django.shortcuts import get_object_or_404
# Create your views here.

@login_required
def user_logout(request):
    del request.session['user_id']
    request.session.flush()
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))



def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)

        if registered:
            login(request, user)
            request.session['user_id'] = user.pk

            return HttpResponseRedirect(reverse('predict:predict', kwargs={'pk': user.pk}))

    else:
        user_form = UserForm()

    return render(request, 'register.html',
                  {'user_form': user_form, 'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = user.pk

                return HttpResponseRedirect(reverse('predict:predict', kwargs={'pk': user.pk}))
            else:
                return HttpResponse("Account not active")
        else:
            print("Tried login and failed")
            print("username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request, 'login.html', {})


