from rest_framework.response import Response
from api.serializers import StudenSerializer
from rest_framework.decorators import api_view # this is for "Function" based api view
from rest_framework.views import APIView  # this is for "Class" based api view
from api.models import Student
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from api.throttle import OmkarThrottle


class StudentAPI(APIView):
    authentication_classes = [BasicAuthentication]# we do not need to import "authentication_classes from Decorators since this is Class Based view"
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, OmkarThrottle]

    def get(self, request, format = None):        
        ID = request.data.get('id')  
        if ID is not None:
            stu = Student.objects.get(id=ID)
            serializer = StudenSerializer(stu)
            return Response(serializer.data)    

        else:
            stu = Student.objects.all()
            serializer = StudenSerializer(stu, many = True)
            return Response(serializer.data)

    def post(self, request, format = None): 
        serializer = StudenSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Data created !"}, status= status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors, status= status.HTTP_406_NOT_ACCEPTABLE)
        
    def put(self, request, format = None):     
        ID = request.data.get('id') 
        stu = Student.objects.get(id= ID)
        serializer = StudenSerializer(stu, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data updated"})
        else:
            return Response(serializer.errors) 

    def delete(self, request, format = None):      
        ID = request.data.get('id')     
        stu = Student.objects.get(id= ID)
        stu.delete()
        return Response({"Message":"Data Deleted",})
