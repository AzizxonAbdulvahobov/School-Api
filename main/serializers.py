from rest_framework import serializers
from . import models
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Class
        fields = '__all__'
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'
        