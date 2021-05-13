
from django.http.response import Http404
from rest_framework import viewsets
from rest_framework import permissions

from rest_framework import status
from rest_framework import decorators 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from api.models import Person
from api.serializers import PersonSerializer

# Create your views here.

'''class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('created')
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]

'''

# Class based views
class PeopleList(APIView):
    def get(self, request, format=None):
        human = Person.objects.all()
        serializer = PersonSerializer(human, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = PersonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PeopleDetail(APIView):
    def get_object(self,pk):
        try:
           return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        human = self.get_object(pk)
        serializer = PersonSerializer(human)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        human = self.get_object(pk)
        serializer = PersonSerializer(human, data=reqeust.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        human  = self.get_object(pk)
        human.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##Function based views

# @api_view(['GET', 'POST'])
# def people_list(request, format=None):
#     if request.method == 'GET':
#         human = Person.objects.all()
#         serializer = PersonSerializer(human, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
        
#         serializer = PersonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET','PUT','DELETE'])
# def people_detail(request,pk,format=None):
#     try:
#         human = Person.objects.get(pk=pk)
#     except Person.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
        
#         serializer = PersonSerializer(human)
#         print("uzywa mojego widoku")
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
        
#         serializer = PersonSerializer(human, data=request.data, partial=True)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status = 400)
    
#     elif request.method == 'DELETE':
#         human.delete()
#         return Response(status=204)
