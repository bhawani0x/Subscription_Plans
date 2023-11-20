from django.contrib.auth.models import User
from rest_framework import serializers
from game.models import Customer
from util.choices import Feature


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}


class CustomerSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = '__all__'

    def get_user_details(self, obj):
        user = obj.user
        user_details = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            # Add more fields as needed
        }
        return user_details

    def to_representation(self, instance):

        data = super().to_representation(instance)
        plan = instance.choice
        features = []

        for feature, included_in_plan in Feature:
            if included_in_plan == plan or included_in_plan == 'Free':
                features.append({'feature_name': feature})

        data['features'] = features
        return data
