from rest_framework import routers

from apps.blog.views import BlogModelSetView

router = routers.DefaultRouter()

router.register("blogs",BlogModelSetView)