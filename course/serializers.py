from rest_framework import serializers
from .models import Course
from django.contrib.auth.models import User, Group
class GetAllCourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']