from rest_framework import viewsets

<<<<<<< HEAD
from .serializers import (
    CategorySerializer, GenreSerializer,
    TitleSerializer
)
from reviews.models import Category, Genre, Title


class CategoryViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Category."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Genre."""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Title."""
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
=======

class CategoryViewSet(viewsets.ModelViewSet):
    pass


class GenreViewSet(viewsets.ModelViewSet):
    pass


class TitleViewSet(viewsets.ModelViewSet):
    pass
>>>>>>> develop
