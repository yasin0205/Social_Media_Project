from django.contrib import admin
from django.urls import path, include

from App_Posts import views

# for media files
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('App_Login.urls')),
    path('post/', include('App_Posts.urls')),
    path('', views.Home, name='home'),
]
#for media files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)