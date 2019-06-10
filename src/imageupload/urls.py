from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from authentication import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/register/', views.signup, name='register'),
    url(r'^~update/$', views.UserUpdateView.as_view(), name='update'),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
