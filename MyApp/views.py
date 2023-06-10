from django.http import Http404
from .models import Student
from .S1 import StudentSerializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

class StudentViews(APIView):
    def get(self, request):
        x = Student.objects.all()
        y = StudentSerializers(x, many=True)
        return Response(y.data, status=status.HTTP_200_OK)

    def post(self, request):
        x = StudentSerializers(data=request.data)
        if x.is_valid():
            x.save()
            return Response(x.data, status=status.HTTP_201_CREATED)
        return Response(x.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentSingle(APIView):
    def get_id_by_pk(self, pk):
        try:
            x = Student.objects.get(pk=pk)
            return x
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        x = self.get_id_by_pk(pk)
        y = StudentSerializers(x)
        return Response(y.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        x = self.get_id_by_pk(pk)
        y = StudentSerializers(x, data=request.data)
        if y.is_valid():
            y.save()
            return Response(y.data, status=status.HTTP_200_OK)
        return Response(y.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        x = self.get_id_by_pk(pk)
        y = StudentSerializers(x, data=request.data, partial=True)
        if y.is_valid():
            y.save()
            return Response(y.data, status=status.HTTP_200_OK)
        return Response(y.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        x = self.get_id_by_pk(pk)
        x.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
