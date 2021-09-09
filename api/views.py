from django.db.models import F, Sum
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer, ProductTotalCostSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    CRUD для модели Product
    return 
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        """
        Переопределяем метод list для вывода oбщeго числа рaзличных тoвaрoв нa склaдe
        :return: {
            "total_cost": 100,
            "prodcuts": [
                {
                    "id": 1,
                    "title": "Помидоры",
                    "stock": 15,
                    "measure": "Килoгрaмм",
                    "price": 100,
                    "updated_at": "2021-09-09T10:38:14.571119+03:00" 
                }
            ]
        }
        """
        # Вычисляем количестов различных товаров
        total_stock = self.queryset.count()
        serializer = self.get_serializer(self.queryset, many=True)
        result = {
            'total_stock': total_stock,
            'products': serializer.data,
        }
        return Response(result)


@api_view(['GET'])
def total_cost(request, *args, **kwargs):
    """
    Общая стоимость всех товаров на складе, а также суммарная стоимость в разрезе товара
    :return: {
        "total_cost": 100,
        "prodcuts": [
            {
                "id": 1,
                "title": "Помидоры",
                "stock": 15,
                "measure": "Килoгрaмм",
                "price": 100,
                "updated_at": "2021-09-09T10:38:14.571119+03:00",
                "amount": 1500
            }
        ]
    }
    """
    # Выборка всех товаров и высисление общей стоимости товара
    queryset = Product.objects.all().annotate(amount=F('stock') * F('price'))

    # Вычисление общей стоимости запасов
    total_cost = queryset.aggregate(Sum('amount'))['amount__sum']
    serializer = ProductTotalCostSerializer(queryset, many=True)
    result = {
        'total_cost': total_cost,
        'products': serializer.data,
    }
    return Response(result)
