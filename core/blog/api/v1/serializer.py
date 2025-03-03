from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id", "name"
        ]

class PostSerializer(serializers.ModelSerializer):
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    snippet = serializers.ReadOnlyField(source='get_snippet')

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet',None)
            rep.pop('relative_url',None)
            rep.pop('absolute_url',None)
        else:
            rep.pop('content', None)
        rep['category'] = CategorySerializer(instance.category,context={'request':request}).data
        return rep
    
    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)
    
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'category', 'content', 'snippet', 'relative_url', 'status', 'created_date', 'published_date']
        read_only_fields = ['author']