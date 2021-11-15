"""PostBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from UserApp import views as user_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',user_view.SignUp,name='signup'),
    path('profile/',user_view.Profile,name='profile'),
    path('signin/',auth_views.LoginView.as_view(template_name='UserApp/signIn.html'),name='signin'),
    path('signout/',auth_views.LogoutView.as_view(template_name='UserApp/signOut.html'),name='signout'),
    path('',include('PostApp.urls')),
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
