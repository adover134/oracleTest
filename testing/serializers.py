from rest_framework import serializers
from testing.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ["u_id", "u_name"]