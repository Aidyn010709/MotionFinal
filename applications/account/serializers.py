from rest_framework import serializers
from django.contrib.auth import get_user_model

from applications.account.tasks import send_activation_code

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')
    
    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.pop('password2')

        if password1 != password2:
            raise serializers.ValidationError('Парольдор окшош эмес!')
        return attrs
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.create_activation_code()
        
        send_activation_code(user.email, user.activation_code)
        return user