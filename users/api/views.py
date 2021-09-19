# from users.api.serializers import (
#     RegisterSerializer, UserSerializer
# )
# from utils.permissions import permissions as custom_permissons
# from drf_yasg2 import openapi
# from rest_framework import permissions, status, viewsets
# from rest_framework.authentication import BasicAuthentication, SessionAuthentication
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from utils.helpers import ResponseWrapper
# from django.conf import settings


# class RegisterView(APIView):
#     # permission_classes = (permissions.AllowAny,)

#     logging_methods = ['GET', 'POST', 'PATCH', 'DELETE']

#     def get_serializer_class(self):
#         self.serializer_class = RegisterSerializer
#         return self.serializer_class

#     def get_permissions(self):
#         permission_classes = [custom_permissions.IsStaff]
#         return [permission() for permission in permission_classes]

#     @swagger_auto_schema()
#     def post(self, request, format=None):
#         return ResponseWrapper(data={"Example": "Example Data"})
