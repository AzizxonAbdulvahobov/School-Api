from rest_framework import viewsets
from . import models
from . import serializers
# from rest_framework import permissions
# from rest_framework.authentication import TokenAuthentication
# Create your views here.

class ClassApiViewSet(viewsets.ModelViewSet):
    queryset = models.Class.objects.all()
    serializer_class = serializers.ClassSerializer


class TeacherApiViewSet(viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer


class StudentApiViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer