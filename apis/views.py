from rest_framework.response import Response
from apis.models import Student
from django.shortcuts import render
from.serializers import StudentSerializer
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def index(request):
    students = Student.objects.all()
    serialstudents = StudentSerializer(students,many=True)
    return Response(serialstudents.data)

@api_view(['GET'])
def studentview(request,pk):
    student = Student.objects.get(id=pk)
    serialStudent = StudentSerializer(student,many=False)
    return Response(serialStudent.data)

@api_view(['POST'])
def studentadd(request):
    serialdata = StudentSerializer(data=request.data)
    if serialdata.is_valid():
        serialdata.save()

    return Response(serialdata.data)

@api_view(['POST'])
def studentupdate(request,pk):
    student = Student.objects.get(id=pk)
    serialStudent = StudentSerializer(instance=student,data=request.data)
    if serialStudent.is_valid():
        serialStudent.save()

    return Response(serialStudent.data)


@api_view(['DELETE'])
def studentdelete(request,pk):
    student = Student.objects.get(id=pk)
    student.delete()

    students = Student.objects.all()
    serialStudents = StudentSerializer(students,many=True)
    return Response(serialStudents.data)
