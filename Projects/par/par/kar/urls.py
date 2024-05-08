from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.models import User
from .views import OrderView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm
urlpatterns = [
    path('',views.home),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path("category/<slug:val>",views.CategoryView.as_view(),name="category"),
    path("category-title/<val>",views.CategoryTitle.as_view(),name="category-title"),
    path('orders/', OrderView.as_view(), name='orders'),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(),name="product"),
    path("registration/",views.RegistrationView.as_view(),name="registration"),
    path("accounts/login/",auth_view.LoginView.as_view(template_name='kar/login.html',
                                                       authentication_form=LoginForm,name='login')),
    path('passwordchange/',auth_view.PasswordChangeDoneView.as_view(template_name='kar/passwordchange.html',form_class=MyPasswordChangeForm,succes_url='/passowrdchangeddone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangedOneView.as_view(template_name='kar/passwordchangedone.html',),name='passwordchangedone'),
    path('password-reset/',auth_view.PasswordResetView.as_view(templates_name='kar/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(templates_name='kar/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(templates_name='kar/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(templates_name='kar/password_reset_complete.html'),name='password_reset_complete')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 