from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from .models import *
from .serializers import UserSerializer, DiscountSerializer, SupplierSerializer, \
                        CartSerializer, CategorySerializer, CommentsSerializer,ProductSerializer


class ProductAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserView(views.APIView):

    def get(self,request,*args,**kwargs):
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)


class SupplierView(views.APIView):

    def get(self,request,*args,**kwargs):
        supplier = Supplier.objects.all()
        serializer = SupplierSerializer(supplier,many=True)
        return Response(serializer.data)


class DiscountView(views.APIView):

    def get(self, request, *args, **kwargs):
        discount = Discount.objects.all()
        serializer = DiscountSerializer(discount, many=True)
        return Response(serializer.data)


class CategoryView(views.APIView):

    def get(self,request,*args,**kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data)


class CartView(views.APIView):

    def get(self,request,*args,**kwargs):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart,many=True)
        return Response(serializer.data)


class CommentsView(views.APIView):

    def get(self,request,*args,**kwargs):
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments,many=True)
        return Response(serializer.data)
