from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from .models import Assignment, GradedAssignment
from .serializers import AssignmentSerializer, GradedAssignmentSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    # queryset = Assignment.objects.all()
    permission_classes = [AssignmentPermission]

    def get_queryset(self):
        return AssignmentQuerySet(self.request)

    def create(self, request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            assignment = serializer.create(request)
            if assignment:
                return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)


class GradedAssignmentListView(ListAPIView):
    serializer_class = GradedAssignmentSerializer
    permission_classes = [GradedAssignmentPermission]

    def get_queryset(self):
        return GradedAssignmentQuerySet(self.request)
        # queryset = GradedAssignment.objects.all()
        # username = self.request.query_params.get('username', None)
        # if username is not None:
        #     queryset = queryset.filter(student__username=username)
        # return queryset


class GradedAssignmentCreateView(CreateAPIView):
    serializer_class = GradedAssignmentSerializer
    queryset = GradedAssignment.objects.all()
    permission_classes = [GradedAssignmentPermission]
    def get_queryset(self):
        return GradedAssignmentQuerySet(self.request)

    def post(self, request):
        serializer = GradedAssignmentSerializer(data=request.data)
        serializer.is_valid()
        graded_assignment = serializer.create(request)
        if graded_assignment:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)