from django.contrib.auth.models import User
from rest_framework import viewsets, views
from rest_framework import status
from rest_framework.response import Response
from game.models import Customer
from .serializers import UserSerializer, CustomerSerializer

class UserCustomer(views.APIView):
    permission_classes = []

    def get(self, request, format=None):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            # Save the user instance
            user_instance = user_serializer.save()
            customer_data = {
                'user': user_instance.id,
                # 'dob': request.data.get('dob'),
                'choice': request.data.get('choice'),
                # 'phone_number': request.data.get('phone_number')
            }
            customer_serializer = CustomerSerializer(data=customer_data)
            if customer_serializer.is_valid():
                customer_instance = customer_serializer.save()
                response_data = {
                    'user': user_serializer.data,
                    'customer': customer_serializer.data
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            errors = {
                **customer_serializer.errors
            }
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        errors = {
            **user_serializer.errors,
        }
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class UserCustomer_details(views.APIView):
    permission_classes = []

    def get(self, request, pk, format=None):
        queryset = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(queryset)
        return Response(serializer.data)
