from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    search_url = serializers.SerializerMethodField()
    class Meta:
        fields = ('id', 'title', 'content','search_url','isbn', 'created_at', 'updated_at',)
        model = models.Post
    def get_search_url(self, obj):
        return "http://www.isbnsearch.org/isbn/{}".format(obj.isbn)
