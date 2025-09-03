from rest_framework import serializers
from django.contrib.auth import get_user_model

from blog.models import Post, Category
from accounts.models import Profile

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source="get_snippet")
    relative_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'image',
            'title',
            'snippet',
            'content',
            'status',
            'published_date',
            'author',
            'category',
            'relative_url',
            'absolute_url',
        )
        read_only_fields = ('id', 'author')

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        profile = Profile.objects.get(user=user)
        validated_data['author'] = profile
        return super().create(validated_data)

    # todo: find other way to handle this
    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        request = self.context.get("request")
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('relative_url', None)
            rep.pop('snippet', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content', None)

        rep['category'] = CategorySerializer(obj.category).data
        return rep

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'parent',
        )