from rest_framework import generics, permissions, views, status, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import User, ContentItem, Category
from .serializers import UserSerializer, ContentItemSerializer, CategorySerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLoginView(views.APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class ContentItemViewSet(viewsets.ModelViewSet):
    queryset = ContentItem.objects.all()
    serializer_class = ContentItemSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return ContentItem.objects.all()
        return ContentItem.objects.filter(author=user)

class ContentSearchView(generics.ListAPIView):
    serializer_class = ContentItemSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return ContentItem.objects.filter(
            models.Q(title__icontains=query) |
            models.Q(body__icontains=query) |
            models.Q(summary__icontains=query) |
            models.Q(categories__name__icontains=query)
        )
