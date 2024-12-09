from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Task, Comment


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", max_length=200, required=True)

    class Meta:
        fields = ["username", "password"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "detail",
            "due_date",
            "status",
            "priority",
            "assigned_by",
            "assigned_to",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["id", "text", "task"]