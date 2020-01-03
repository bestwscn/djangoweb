from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from apps.blog import models

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        read_only_fields = ["user","slug","timestamp"]
        fields = "__all__"
        extra_kwargs = {
            "title": {"error_messages": {"required": "标题内容不能为空"}},
            "content": {"error_messages": {"required": "文章不能为空"}}
        }


class BlogModelSetView(ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = BlogSerializers

    def pre_save(self, obj):
        obj.user = self.request.user
