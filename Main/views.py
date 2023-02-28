from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.db import IntegrityError
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# Create your views here.

def home(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html",{
            "form": UserCreationForm
        })

    else:
        user=request.POST["username"]
        password_1=request.POST["pass"]
        password_2=request.POST["repeat_pass"]
        mail_1=request.POST["mail"]
        mail_2=request.POST["repeat_mail"]
        if password_1==password_2:
            try:
                validate_password(password_1, user=user)
                if mail_1==mail_2:
                    if mail_1!="":
                        validate_mail=User.objects.filter(email=mail_1).exists()
                        if validate_mail==False:
                            try:
                                user=User.objects.create_user(
                                    email=mail_1,
                                    username=user,
                                    password=password_1
                                )
                                user.save()
                                login(request,user)
                                return redirect("tasks")
                            
                            except IntegrityError:
                                return render(request, "signup.html", {
                                    "form": UserCreationForm,
                                    "error": "El nombre de usuario ya existe."
                                })
                            
                        return render(request, "signup.html", {
                            "form": UserCreationForm,
                            "error": "El mail ya existe."
                        })
                    
                    return render(request, "signup.html", {
                        "form": UserCreationForm,
                        "error": "Por favor ingrese un mail."
                    })

                return render(request, "signup.html", {
                    "form": UserCreationForm,
                    "error": "El mail no coincide."
                    })

            except ValidationError:
                return render(request, "signup.html", {
                    "form": UserCreationForm,
                    "error": "La contraseña no verifica los requisitos mínimos de seguridad."
                    })
    
        return render(request, "signup.html", {
            "form": UserCreationForm,
            "error": "La contraseña no coincide."
        })

def signin(request):
    if request.method=="GET":
        return render(request, "signin.html",{
        "form": AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["pass"])
        if user is None:
            return render(request, "signin.html",{
            "form": AuthenticationForm,
            "error" : "El nombre de usuario o la contrseña son icorrectas",
            })
        
        else:
            login(request, user)
            return redirect("tasks")       