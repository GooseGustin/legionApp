from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Legionary

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # Create the user; the signal will handle Legionary creation
        return User.objects.create_user(**validated_data)
    

class LegionarySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta: 
        model = Legionary        
        fields = [
            'user', 
            'status', 
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        # Use UserSerializer to create user instead of directly creating User
        user = UserSerializer().create(user_data)
        Basic_Group, _ = Group.objects.get_or_create(name='Basic_Group')
        user.groups.add(Basic_Group)
        user.save()
        
        # Create Legionary and link it to the created user
        legionary = Legionary.objects.create(user=user, **validated_data)
        return legionary
    # Check the above method in ChatGPT