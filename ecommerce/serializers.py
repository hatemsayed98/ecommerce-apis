from rest_framework.serializers import ModelSerializer 
from .models import Product, Cart, Wishlist, User


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class WishlistSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'imageSRC']