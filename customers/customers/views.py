from customers.serializer import CustomerSerializer
from customers.models import Customers
from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def customers(request):
    if request.method == 'GET':
        customers = Customers.objects.all()

        serializer = CustomerSerializer(customers, many=True)

        return Response({'customers': serializer.data})
    elif request.method == 'POST':

        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customers': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def customer(request, id):
    try:
        customer = Customers.objects.get(pk=id)

    except Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response({'customer': serializer.data})
    
    elif request.method == 'POST':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
