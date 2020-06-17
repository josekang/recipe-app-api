from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient, Recipe, User
from .serializers import TagSerializer, IngredientSerializer, RecipeSerializer

# Create your views here.

class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def list(self, request, *args, **kwargs):
        super(TagListCreateAPIView, self).list(request, *args, **kwargs)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        response = {
            'status': status.HTTP_200_OK,
            'message': 'All tags retrieved successfully',
            'data': data
        }
        
        return Response(response)
    
    def create(self, request, *args, **kwargs):
        user = request.user
        
        request.data._mutable = True
        request.data.update({
            'user': user.id
        })
        request.data._mutable = False
        
        super(TagListCreateAPIView, self).create(request, *args, **kwargs)
        
        response = {
            'status': status.HTTP_201_CREATED,
            'message': 'Tag created successfully',
            'data': request.data
        }
        
        return Response(response)
    
    
class TagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def retrieve(self, request, *args, **kwargs):
        super(TagRetrieveUpdateDestroyAPIView, self).retrieve(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Tag detail retrieved successfully',
            'data': data
        }
        
        return Response(response)
    
    def patch(self, request, *args, **kwargs):
        super(TagRetrieveUpdateDestroyAPIView, self).patch(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Tag details upated successfully',
            'data': data
        }
        
        return Response(response)
    
    def delete(self, request, *args, **kwargs):
        super(TagRetrieveUpdateDestroyAPIView, self).delete(request, *args, **kwargs)
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Tag deleted suucessfully'
        }
        
        return Response(response)
 
    
class IngredientListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    
    def list(self, request, *args, **kwargs):
        super(IngredientListCreateAPIView, self).list(request, *args, **kwargs)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        response = {
            'status': status.HTTP_200_OK,
            'message': 'All Ingredients retrieved successfully',
            'data': data
        }
        
        return Response(response)
    
    def create(self, request, *args, **kwargs):
        user = request.user
        
        request.data._mutable = True
        request.data.update({
            'user': user.id
        })
        request.data._mutable = False
        
        super(IngredientListCreateAPIView, self).create(request, *args, **kwargs)
        
        response = {
            'status': status.HTTP_201_CREATED,
            'message': 'Ingredient created successfully',
            'data': request.data
        }
        
        return Response(response)
   
    
class IngredientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def retrieve(self, request, *args, **kwargs):
        super(IngredientRetrieveUpdateDestroyAPIView, self).retrieve(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Ingredient retrieved successfully',
            'data': data
        }
        
        return Response(response)
    
    def patch(self, request, *args, **kwargs):
        super(IngredientRetrieveUpdateDestroyAPIView, self).patch(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Ingredient updated successfully',
            'data': data
        }
        
        return Response(response)
    
    def delete(self, request, *args, **kwargs):
        super(IngredientRetrieveUpdateDestroyAPIView, self).delete(request, *args, **kwargs)
        
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Ingredient deleted successfully',
        }
        
        return Response(response)
  

class RecipeListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def list(self, request, *args, **kwargs):
        super(RecipeListCreateAPIView, self).list(request, *args, **kwargs)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        
        response = {
            'status': status.HTTP_200_OK,
            'message': 'All recipes retrieved suuccessfully',
            'data': data
        }
        
        return Response(response)
    
    def create(self, request, *args, **kwargs):
        user = self.request.user
        
        request.data._mutable = True
        
        request.data.update({
            'user': user.id
        })  
        request.data._mutable = False
              
        super(RecipeListCreateAPIView, self).create(request, *args, **kwargs)
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Recipe create succesfully',
            'data': request.data
        }
        
        return Response(response)
    
    
class RecipeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def retrieve(self, request, *args, **kwargs):
        super(RecipeRetrieveUpdateDestroyAPIView, self).retrieve(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Recipe retrieved successfully',
            'data': data
        }
        
        return Response(response)
        
    def patch(self, request, *args, **kwargs):
        super(RecipeRetrieveUpdateDestroyAPIView, self).patch(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Recipe updated successfully',
            'data': data
        }
        
        return Response(response)
    
    def delete(self, request, *args, **kwargs):
        super(RecipeRetrieveUpdateDestroyAPIView, self).delete(request, *args, **kwargs)
        
        response = {
            'status': status.HTTP_200_OK,
            'message': 'Recipe deleted successfully'
        }
        
        return Response(response)
    
# class BaseRecipeAttrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    
#     permission_classes = (IsAuthenticated,)
#     authentication_classes = (TokenAuthentication,)
    
#     def get_queryset(self):
#         assigned_only = bool(
#             int(self.request.query_params.get('assigned_only', 0))
#         )
#         queryset = self.queryset
#         if assigned_only:
#             queryset = queryset.filter(recipe__isnull=False)
        
#         return queryset.filter(user=self.request.user).order_by('-name').distinct()
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
    

# class TagViewSet(BaseRecipeAttrViewSet):
    
#     queryset = Tag.objects.all()
#     serializer_class = serializers.TagSerializer
         
        
# class IngredientViewSet(BaseRecipeAttrViewSet):
#     queryset = Ingredient.objects.all()
#     serializer_class = serializers.IngredientSerializer
    
    
# class RecipeViewSet(viewsets.ModelViewSet):
#     serializer_class = serializers.RecipeSerializer
#     queryset = Recipe.objects.all()
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
    
#     def _params_to_ints(self, qs):
#         return [int(str_id) for str_id in qs.split(',')]
    
#     def get_queryset(self):
#         tags = self.request.query_params.get('tags')
#         ingredients = self.request.query_params.get('ingredients')
#         queryset = self.queryset
#         if tags:
#             tag_ids = self._params_to_ints(tags)
#             queryset = queryset.filter(tags__id__in=tag_ids)   
#         if ingredients:
#             ingredient_ids = self._params_to_ints(ingredients)
#             queryset = queryset.filter(ingredients__id__in=ingredient_ids)
            
#         return queryset.filter(user=self.request.user)
    
#     def get_serializer_class(self):
#         if self.action == 'retrieve':
#             return serializers.RecipeDetailSerializer
#         elif self.action == 'upload_image':
#             return serializers.RecipeImageSerializer
        
#         return self.serializer_class
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
        
#     @action(methods=['POST'], detail=True, url_path='upload-image')
#     def upload_image(self, request, pk=None):
#         recipe = self.get_object()
#         serializer = self.get_serializer(
#             recipe,
#             data=request.data
#         )
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_200_OK
#             )
            
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )