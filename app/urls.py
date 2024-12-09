from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Home, SignUpView, LoginView, LogoutView


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),    


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )