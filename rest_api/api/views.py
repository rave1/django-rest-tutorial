from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Person
from api.serializers import PersonSerializer
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.

'''class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('created')
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]

'''

@csrf_exempt
def people_list(request):
    if request.method == 'GET':
        human = Person.objects.all()
        serializer = PersonSerializer(human, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def people_detail(request,pk):
    try:
        human = Person.objects.get(id=pk)
    except Person.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        
        serializer = PersonSerializer(human)
        print("uzywa mojego widoku")
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        
        serializer = PersonSerializer(human, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status = 400)
    
    elif request.method == 'DELETE':
        human.delete()
        return HttpResponse(status=204)

   