# products/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

# GET /products/ - List all products or filter by availability
class ProductListView(APIView):
    def get(self, request):
        # Check if the 'in_stock' query parameter is provided
        in_stock = request.query_params.get('in_stock', None)

        # Filter products based on stock availability if the 'in_stock' query parameter is provided
        if in_stock is not None:
            in_stock = in_stock.lower() == 'true' 
            if in_stock:
                products = Product.objects.filter(stock__gt=0)
            else:
                products = Product.objects.filter(stock__lte=0)
        else:
            # If no filter, return all products
            products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# POST /products/ - Create a new product
class ProductCreateView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT /products/<id>/ - Update an existing product
class ProductUpdateView(APIView):
    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"detail": "Produit non trouvé."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE /products/<id>/ - Delete a product
class ProductDeleteView(APIView):
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"detail": "Produit non trouvé."}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
