from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product_Shelflife
from .serializer import Product_ShelflifeSerializer



@api_view(['GET'])
def get_products(request):
    if request.GET.get('date_start') and request.GET.get('date_end'):
        date_start = request.GET.get('date_start')
        date_end = request.GET.get('date_end')
        products_filted = Product_Shelflife.objects.filter(shelflife__range=(date_start, date_end))
        serielizer = Product_ShelflifeSerializer(products_filted, many=True)
        return Response(serielizer.data, status=status.HTTP_200_OK)
    products = Product_Shelflife.objects.all()
    serializer = Product_ShelflifeSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product(request, pk):
    try:
        product = Product_Shelflife.objects.get(pk=pk)
    except Product_Shelflife.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = Product_ShelflifeSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_product(request):
    serializer = Product_ShelflifeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def mod_product(request, pk):
    try:
        print(pk)
        product = Product_Shelflife.objects.get(pk=pk)
        serializer = Product_ShelflifeSerializer(product, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except Product_Shelflife.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product = Product_Shelflife.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_200_OK)
    except product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def filter_product(request):
    date_start = request.GET.get('date_start')
    date_end = request.GET.get('date_end')
    products_filted = Product_Shelflife.objects.filter(shelflife__range=(date_start, date_end))
    serielizer = Product_ShelflifeSerializer(products_filted, many=True)
    Response(serielizer.data, status=status.HTTP_200_OK)
