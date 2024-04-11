from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def login_index(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username = username, password = password)

    if user is not None:
      login(request, user=user)
      return redirect("lessons")
    else:
      messages.info(request, "L'identifiant ou le mot de passe incorrect !")

  form = AuthenticationForm()
  return render(request, "auth_login_index.html", context={"form": form})

def register_index(request):

  if request.method == 'POST':
    form = UserCreationForm(request.POST)

    if form.is_valid:
      form.save()
      return redirect("lessons")
  else:
    form = UserCreationForm()

  return render(request, "auth_register_index.html", context={"form": form})

def logout_index(request):
  logout(request)
  return redirect("home")
