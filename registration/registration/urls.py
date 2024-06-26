from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('contact/', views.ContactPage, name='contact'),
    path('logout/', views.Logout,name='logout'),
    path('chatbot/',views.ChatBot,name='chatbot'),
    path('bitchat/',views.BitChat,name='bitchat'),
    path('dashboard/',views.DashBoard,name='dashboard'),
    path('bit/',views.bit,name='bit'),

    path('home1/',views.HomePage1,name='home1'),
    path('contact1/', views.ContactPage1, name='contact1'),
    path('chatbot1/',views.ChatBot1,name='chatbot1'),
    path('bitchat1/',views.BitChat1,name='bitchat1'),
    path('dashboard1/',views.DashBoard1,name='dashboard1'),
    path('bit1/',views.bit1,name='bit1'),

    path('voicechat/',views.VoiceBot,name='voicechat'),
    path('getResponse', views.getResponse, name='getResponse')
]

# URL patterns for serving static files and admin media files
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
