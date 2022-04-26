from rest_framework import serializers
from testing.models import User, TestClass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ["u_id", "u_name"]


class TestClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestClass
        fields = ['user', 'test_id', 'u_name']
