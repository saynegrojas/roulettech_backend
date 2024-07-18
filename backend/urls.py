"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from api.views import CreateUserView
# Pre-built views that allow us to obtain our access and refresh token and to refresh the token
# Once the user is created, we can use these pre-built views to obtain our access and refresh token for that user and effectively sign in
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    # user register path --> goes to api/user/register/ and call the CreateUserView class to create a new user
    path('api/user/register/', CreateUserView.as_view(), name='register'),
    # implement the view to obtain the access (built-in view), we just need to set up the path
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'),
    # implement the view to refresh the token (built-in view), we just need to set up the path
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    # auth view?
    path('api-auth/', include('rest_framework.urls')),
    
    # include the path to the notes app
    path('api/', include('api.urls'))

]


# Mirgrations
# When you make changes to your data models, you need to run migrations to update your database schema. 
# python manage.py makemigrations --> creates the file that specifies the migrations that need to be performed
# python manage.py migrate --> after making the migrations, we need to apply the migrations