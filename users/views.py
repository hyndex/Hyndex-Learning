from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from .serializers import *
from rest_framework import filters



class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    search_fields = ['user__username','user__email','phone','name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = InstituteSerializer
    permission_classes = [InstitutePermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return InstituteQuerySet(self.request)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    search_fields = ['user__username','user__email','phone','name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ProfileSerializer
    permission_classes = [ProfilePermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return ProfileQuerySet(self.request)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = GroupSerializer
    permission_classes = [GroupPermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return GroupQuerySet(self.request)

class ProfileRoleViewSet(viewsets.ModelViewSet):
    queryset = ProfileRole.objects.all()
    search_fields = ['user__name','user__user__username','user__phone','user__user__email','group__name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ProfileRoleSerializer
    permission_classes = [ProfileRolePermission]
    model=serializer_class().Meta().model
    def get_queryset(self):
        return ProfileRoleQuerySet(self.request)


############################################################################

class ChangePasswordView(UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                return Response("Success.", status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)# if data is not valid then will not proceed forward and return a error msg
        user = serializer.validated_data['user']
        django_login(request,user)
        token, created=Token.objects.get_or_create(user=user)#created = True if token already exist else False
        return Response({"token": token.key },status=200)

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    def post(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        django_logout(request)
        return Response({"msg":"successfully logout"},status=204)