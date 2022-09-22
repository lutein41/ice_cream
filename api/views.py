from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .serializers import ProductSerializer, GuestSerializer, OrderSerializer
from rest_framework.renderers import JSONRenderer
from .models import *

@api_view()
def get_products(request):
    
    # get all available products
    products = Product.objects.filter(available=True)
    serializer = ProductSerializer(products, many=True)
    
    return Response(serializer.data)

@api_view(["POST"])
def order(request):

    #deserialization

    product_id_list = request.data['id'].split(',')
    product_quantity_list = request.data['quantity'].split(',')
    product_model_list = Product.objects.filter(id__in=product_id_list)
    
    serializer = GuestSerializer(data=request.data, partial=True);
    serializer.is_valid(raise_exception=True)
    serializer.save()

    guest_model = Guest.objects.last()
    
    for i in range(len(product_model_list)):
        Order.objects.create(guest=guest_model, product=product_model_list[i], quantity=product_quantity_list[i])
 

    #serialization

    order_sets = Order.objects.filter(guest_id=guest_model.guest_id)
    return_data = {
        'order_number': None,
        'products': [],
        'order_date': None,
    }

    return_data['order_number'] = guest_model.guest_id
    return_data['order_date'] = order_sets[0].order_date

    for order in order_sets:
        return_data['products'].append({'name':(Product.objects.get(id=order.product.id)).flavor , 'quantity': order.quantity})    
        
    json = JSONRenderer().render(return_data)

    return Response(json)