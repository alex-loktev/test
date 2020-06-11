from django.urls import path
from .views import *


urlpatterns = [
    path('article/<int:pk>/', ArticleDetail.as_view(), name='detail'),
    path('create/', ArticleCreate.as_view(), name='create'),
    path('update/<int:pk>/', UpdateArcticle.as_view(), name='update'),
]