from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.mixins import (
    UpdateModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    ListModelMixin,
)
from .models import Task
from rest_framework.generics import GenericAPIView
from error_logger.utils import CustomPagination
from .serializers import TaskSerializer

# Create your views here.


class TaskView(
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    GenericAPIView,
):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        many, queryset = True, self.filter_queryset(self.get_queryset())
        if "pk" in kwargs and kwargs["pk"]:
            many, queryset = False, self.get_object()
        serializer = self.get_serializer(queryset, many=many)
        data = serializer.data
        if many==True:
            data = self.paginate_queryset(data)
            return self.get_paginated_response(data)
        return Response(
            {"data": data, "error": ""}, status=status.HTTP_200_OK
        )


    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
