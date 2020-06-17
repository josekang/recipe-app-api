from rest_framework import serializers

from core.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ('id', 'name', 'user')
        read_only_fields = ('id', )
    
    
    # def create(self, validated_data):
    #     raise ValueError(validated_data)
    
        

class IngredientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'user')
        read_only_fields = ('id',)
        
    # def create(self, validated_data):
    # #     obj = Ingredient.objects.create(**validated_data)
    # #     obj.save(name=validated_data['name'])
    # #     return obj
    #     raise ValueError(validated_data)

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )
    
    class Meta:
        model = Recipe
        fields = (
                    'id', 'user',
                    'title', 'ingredients', 'tags', 'time_minutes', 'price', 'link'
                )
        read_only_fields = ('id',)
        

class RecipeDetailSerializer(RecipeSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    

class RecipeImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ('id', 'image')
        read_only_fields = ('id',)