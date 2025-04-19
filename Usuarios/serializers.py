from rest_framework import serializers
from .models import Role, User,BMI
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 
from decimal import Decimal
from django.utils import timezone
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'password', 'address']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
      
        # 🔥 CIFRAR LA CONTRASEÑA CORRECTAMENTE
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)  # 🔒 Cifrar la contraseña antes de guardar
        user.save()      
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address = validated_data.get('address', instance.address)


        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance

class LogoutSerializer(serializers.Serializer):
    user = serializers.IntegerField()
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['userId'] = self.user.id  # Agrega el ID del usuario a la respuesta
        return data
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
         
class BMISerializer(serializers.ModelSerializer):
    bmi = serializers.ReadOnlyField()  # Campo calculado basado en peso y altura

    class Meta:
        model = BMI
        fields = ['id_bmi', 'user', 'weight', 'height', 'date', 'bmi']
        read_only_fields = ['id_bmi', 'bmi', 'date']  # ID y fecha solo lectura

    def validate(self, data):
        # Validación para asegurar que el peso y la altura son positivos
        if data['weight'] <= 0 or data['height'] <= 0:
            raise serializers.ValidationError('El peso y la altura deben ser positivos.')
        return data