from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('about/', about),
    path('blog/', blog),
    path('maqola/<str:link>/', maqola),
]
