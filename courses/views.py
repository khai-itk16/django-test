from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]

    @action(methods=["POST"], detail=True, url_path="hide-course")
    def hide_courses(self, request, pk):

        try:
            course = Course.objects.get(pk=pk)
            course.active = False
            course.save()
        except Course.DoesNotExist:
            return Response(data="Not found object course", status=status.HTTP_400_BAD_REQUEST)
        return Response(data=CourseSerializer(course).data, status=status.HTTP_200_OK)
