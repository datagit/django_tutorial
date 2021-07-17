# from django.db import models
# from django.db.models import fields
# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Course
from .serializers import GetAllCourseSerializers

# Create your views here.



class GetAllCoursesApiView(APIView):
  def get(self, request):
    all = Course.objects.all()
    myData = GetAllCourseSerializers(all, many = True)
    return Response(status=status.HTTP_200_OK, data=myData.data)
