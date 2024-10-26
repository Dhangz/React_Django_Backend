from rest_framework import serializers
from customers.models import Customers
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):       
        user = User.objects.create(
            username = validated_data['username'],
            password = validated_data['password'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user