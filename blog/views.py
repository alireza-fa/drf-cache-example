from rest_framework.views import APIView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .models import Post
from .serializers import PostListSerializer
from .paginations import PostPagination


class PostListView(APIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPagination
    cache_timeout = 60

    @method_decorator(cache_page(cache_timeout))
    def get(self, request):
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(self.queryset, request)
        serializer = self.serializer_class(instance=paginated_queryset,  many=True)
        return paginator.get_paginated_response(serializer.data)
