from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView
from cart import serializers
from rest_framework.response import Response



class CartAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def post(self, request):
        serializer = serializers.CartSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)

    def get(self, request):
        serializer = serializers
        carts = serializers.CartSerializer(carts, many=True).data
        return Response(serializer,status=200)
