from django.shortcuts import render
from django.http import HttpResponse, response
# Create your views here.
def index(request):
  response = HttpResponse()
  response.writelines('<h1>xin chào<h1>')
  response.write('<h1>Đay là app home<h1>')
  return response