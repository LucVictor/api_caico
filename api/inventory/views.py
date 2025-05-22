from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item_Checked, Inventory_Checked
from .serializer import Item_CheckedSerializer, Inventory_CheckedSerializer



@api_view(['GET'])
def get_inventory(request):
    if request.GET.get('date_start') and request.GET.get('date_end'):
        date_start = request.GET.get('date_start')
        date_end = request.GET.get('date_end')
        products_filted = Inventory_Checked.objects.filter(date__range=(date_start, date_end))
        serielizer = Inventory_CheckedSerializer(products_filted, many=True)
        return Response(serielizer.data, status=status.HTTP_200_OK)
    products = Inventory_Checked.objects.all()
    serializer = Inventory_CheckedSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_items(request):
    if request.GET.get('date_start') and request.GET.get('date_end'):
        date_start = request.GET.get('date_start')
        date_end = request.GET.get('date_end')
        products_filted = Item_Checked.objects.filter(date__range=(date_start, date_end))
        serielizer = Item_CheckedSerializer(products_filted, many=True)
        return Response(serielizer.data, status=status.HTTP_200_OK)
    products = Item_Checked.objects.all()
    serializer = Item_CheckedSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_invetory(request):
    serializer = Inventory_CheckedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_item(request):
    serializer = Item_CheckedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def mod_inventory(request, pk):
    try: 
        inventory = Inventory_Checked.objects.get(pk=pk)
        serializer = Inventory_CheckedSerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except inventory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_inventory(pk):
    try: 
        inventory = Inventory_Checked.objects.get(pk=pk)
        inventory.delete()
        return Response(status=status.HTTP_200_OK)
    except inventory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_item(pk):
    try: 
        item = Item_Checked.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_200_OK)
    except item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
