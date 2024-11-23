from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from applications.account.serializers import RegisterSerializer

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            "Сиз регистрацияны оттунуз!, Сизге почтага активационный код жиберилди!",
            status=201
        )
    
class ActivationAPIView(APIView):

    def get(self, request, activation_code):
        print(activation_code)
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save(update_fields=['is_active', 'activation_code'])
        return Response(
            "success",
            status=200
        )
    