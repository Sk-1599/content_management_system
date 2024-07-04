from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, UserLoginView, ContentItemViewSet, ContentSearchView

router = DefaultRouter()
router.register(r'contents', ContentItemViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('search/', ContentSearchView.as_view(), name='content-search'),
    path('', include(router.urls)),
]
