from django.contrib import admin
from django.urls import path, include
from books.views import BooksViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
