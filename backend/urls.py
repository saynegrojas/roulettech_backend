from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('api-auth/', include('rest_framework.urls')),
    
    # include the urls from api/urls.py
    path('api/', include('api.urls'))

]


# Mirgrations
# When you make changes to your data models, you need to run migrations to update your database schema. 
# python manage.py makemigrations --> creates the file that specifies the migrations that need to be performed
# python manage.py migrate --> after making the migrations, we need to apply the migrations