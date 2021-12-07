from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    path('groups/<slug:pk>/', include('posts.urls', namespace='posts')), 
    path('admin/', admin.site.urls),
]
