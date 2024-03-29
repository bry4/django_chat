from django.urls import path
from . import views
from .views import chat_view, conversacion_view

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('chat/', chat_view, name='chat'),
    path('conversacion/<int:conversacion_id>/', conversacion_view, name='conversacion'),
]
