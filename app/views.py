from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View

from .forms import LoginForm, SignUpForm, TaskForm
from .models import User, Task


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
            return redirect("home")
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
                return redirect("listsoftask")
        return render(request, self.template_name, {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")


class CreateTaskView(TemplateView):
    template_name = "create_task.html"

    def get(self, request):       
        users = User.objects.exclude(id=request.user.id)
        form = TaskForm()
        return render(
            request, self.template_name, {"form": form, "users": users}
        )

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_by = request.user
            task.save()
            return redirect('listsoftask')
        else:
            return render(request, self.template_name, {"form": form})


class TaskListView(TemplateView):
    template_name = "task_list.html"

    def get(self, request):
        task = Task.objects.all()
        context = {"task": task}
        return render(request, self.template_name, context=context)


class DetailTaskView(TemplateView):
    template_name = "task_detail.html"

    def get(self, request, pk):
        task = Task.objects.filter(id=pk).first()
        context = {"task": task}
        return render(request, self.template_name, context=context)

