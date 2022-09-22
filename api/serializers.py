from rest_framework import serializers
from .models import * 


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__'


def address_validation(value):
    ''' Check if a first letter of address street starts with number '''
    first_letter_unicode = ord(value[0])
    if first_letter_unicode < 48 or first_letter_unicode > 57:
        raise serializers.ValidationError("a first letter of address street is not a number")

def zip_code_validation(value):
    ''' Check if a zip code has 5 digits '''
    value = str(value)
    if len(value) < 5:
        raise serializers.ValidationError("zip code must have 5 digits")

def phone_number_validation(value):
    ''' Check if a zip code has 5 digits '''
    value = str(value)
    if len(value) != 10:
        raise serializers.ValidationError("phone number must have 10 digits including area code")


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'
        extra_kwargs = { 'address' : { 'validators' : [address_validation]},
                        'zip_code' : { 'validators' : [zip_code_validation]},
                        'phone_number' : { 'validators' : [phone_number_validation]},} 

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = '__all__'