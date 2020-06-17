from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views


# router = DefaultRouter()
# router.register('tags', views.TagListCReateAPIView)
# # router.register('ingredients', views.IngredientViewSet)
# # router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    
    path('tags/', views.TagListCreateAPIView.as_view()),
    path('tags/<int:pk>/', views.TagRetrieveUpdateDestroyAPIView.as_view()),
    path('ingredients/', views.IngredientListCreateAPIView.as_view()),
    path('ingredients/<int:pk>/', views.IngredientRetrieveUpdateDestroyAPIView.as_view()),
    path('recipes/', views.RecipeListCreateAPIView.as_view()),
    path('recipes/<int:pk>/', views.RecipeRetrieveUpdateDestroyAPIView.as_view()),

]
