from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .crud import KlasaCRUD
from .serializers import KlasaSerializer

def home_view(request):
    return render(request, 'home_template.html')

class KlasaListCreateAPIView(APIView):
    def get(self, request):
        """Get all records"""
        records = KlasaCRUD.read_all()
        serializer = KlasaSerializer(records, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new record"""
        serializer = KlasaSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            x = serializer.validated_data['x']
            y = serializer.validated_data['y']
            new_record = KlasaCRUD.create(name, x, y)
            return Response(KlasaSerializer(new_record).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KlasaDetailAPIView(APIView):
    def get(self, request, pk):
        """Get a single record by ID"""
        record = KlasaCRUD.read_by_id(pk)
        if record:
            serializer = KlasaSerializer(record)
            return Response(serializer.data)
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        """Update a record"""
        record = KlasaCRUD.read_by_id(pk)
        if record:
            name = request.data.get('name', record.name)
            x = request.data.get('x', record.x)
            y = request.data.get('y', record.y)
            updated_record = KlasaCRUD.update(pk, name, x, y)
            return Response(KlasaSerializer(updated_record).data)
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        """Delete a record"""
        record = KlasaCRUD.delete(pk)
        if record:
            return Response({'detail': 'Deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)