from rest_framework import serializers
from rest_framework.authtoken.models import Token
from contact_list.serializers import ContactSerializer

from .models import (
    UserProfile,
)

class UserProfileSerializer(serializers.ModelSerializer):

    """Foydalanuvchi profilimiz ob'ektlari uchun seriyalilashtiruvchi."""
    class Meta:
        model = UserProfile
        fields = ('id', "full_name","email", "gender", "active", "staff","admin",'phone_numbers', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        """Yangi foydalanuvchi yaratish va qaytarish."""
        user = UserProfile.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return