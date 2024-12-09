from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


class Home(TemplateView):
    template_name = "home.html"

    def get(self, request):
        return render(request, self.template_name)
    

class SignUpView(TemplateView):
    template_name = "signin/register.html"

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        # Process the form submission
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Account created successfully! Please log in."
            )
            return redirect("login")

        return render(request, self.template_name, {"form": form})
    

class LoginView(TemplateView):
    template_name = "signin/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, self.template_name, {"form": form})
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
