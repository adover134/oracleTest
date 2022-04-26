import copy

from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from testing.serializers import UserSerializer, TestClassSerializer
from testing.models import User, TestClass
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings


class UserViewSets(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        return super().list(self, request, args, kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, args, kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(self, request, args, kwargs)

    # update는 이상하게도 오버라이드를 하지 않으면 정상 동작하지 않습니다. 코드는 상위 코드와 동일합니다.
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        print(instance)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, args, kwargs)


class UserRetViewSets(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #폼을 이용한 검색 예제입니다. 실행 후, localhost:8000/test/userRet/으로 접속하시면 됩니다.
    def retrieve(self, request, *args, **kwargs):
        print(request.data)
        length = len(request.data['u_name'])
        if (request.data['u_id']==''):
            if (length > 0):
                print(length)
                instance = get_object_or_404(User, u_name=request.data['u_name'])
                print(instance)
                serializer = self.get_serializer(instance)
                return Response(serializer.data)
            instance = get_object_or_404(User, u_id='werwerwe')
            print(instance)
            serializer = self.get_serializer(instance)
            return Response("hello")
        instance = get_object_or_404(User, u_id=request.data['u_id'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class TestClassViewSets(ModelViewSet):
    queryset = TestClass.objects.all()
    serializer_class = TestClassSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, args, kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(self, request, args, kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(self, request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, args, kwargs)
