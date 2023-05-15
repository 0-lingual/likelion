from rest_framework.serializers import ModelSerializer
from .models import Post

class PostBaseModelserializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostListModelserializer(PostBaseModelserializer):
    class Meta(PostBaseModelserializer.Meta):
        fields = [
            'image',
            'content',
            'created_at',
            'view_count',
            'writer',
        ]
        depth = 1

class PostCreatetModelserializer(PostBaseModelserializer):
    class Meta(PostBaseModelserializer.Meta):
        fields = [
            'image',
            'content',
        ]
        
class PostDeleteModelserializer(PostBaseModelserializer):
        pass
