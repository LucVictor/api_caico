from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product_Damaged
from .serializer import Product_DamagedSerializer



@api_view(['GET'])
def get_products(request):
    if request.GET.get('date_start') and request.GET.get('date_end'):
        date_start = request.GET.get('date_start')
        date_end = request.GET.get('date_end')
        products_filted = Product_Damaged.objects.filter(date__range=(date_start, date_end))
        serielizer = Product_DamagedSerializer(products_filted, many=True)
        return Response(serielizer.data, status=status.HTTP_200_OK)
    products = Product_Damaged.objects.all()
    serializer = Product_DamagedSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_product(request):
    serializer = Product_DamagedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def mod_product(request, pk):
    try: 
        product = Product_Damaged.objects.get(pk=pk)
        serializer = Product_DamagedSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_product(request, pk):
    try: 
        product = Product_Damaged.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_200_OK)
    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def filter_product(request):
    date_start = request.GET.get('date_start')
    date_end = request.GET.get('date_end')
    products_filted = Product_Damaged.objects.filter(shelflife__range=(date_start, date_end))
    serielizer = Product_DamagedSerializer(products_filted, many=True)
    Response(serielizer.data, status=status.HTTP_200_OK)