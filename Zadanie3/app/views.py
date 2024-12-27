from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .crud import KlasaCRUD
from .serializers import WineDataSerializer

def home_view(request):
    return render(request, 'home_template.html')

class KlasaListCreateAPIView(APIView):
    def get(self, request):
        """Get all records"""
        records = KlasaCRUD.read_all()
        serializer = WineDataSerializer(records, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Create a new record"""
        serializer = WineDataSerializer(data=request.data)
        if serializer.is_valid():
            fixed_acidity = serializer.validated_data['fixed_acidity']
            volatile_acidity = serializer.validated_data['volatile_acidity']
            citric_acid = serializer.validated_data['citric_acid']
            residual_sugar =serializer.validated_data['residual_sugar']
            chlorides =serializer.validated_data['chlorides']
            free_sulfur_dioxide = serializer.validated_data['free_sulfur_dioxide']
            total_sulfur_dioxide = serializer.validated_data['total_sulfur_dioxide']
            density = serializer.validated_data['density']
            pH =serializer.validated_data['pH']
            sulphates = serializer.validated_data['sulphates']
            alcohol = serializer.validated_data['alcohol']
            quality = serializer.validated_data['quality']
            new_record = KlasaCRUD.create(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality)
            return Response(WineDataSerializer(new_record).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KlasaDetailAPIView(APIView):
    def get(self, request, pk):
        """Get a single record by ID"""
        record = KlasaCRUD.read_by_id(pk)
        if record:
            serializer = WineDataSerializer(record)
            return Response(serializer.data)
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        """Update a record"""
        record = KlasaCRUD.read_by_id(pk)
        if record:
            fixed_acidity = request.data.get('fixed_acidity', record.fixed_acidity)
            volatile_acidity = request.data.get('volatile_acidity', record.volatile_acidity)
            citric_acid = request.data.get('citric_acid', record.citric_acid)
            residual_sugar = request.data.get('residual_sugar', record.residual_sugar)
            chlorides = request.data.get('chlorides', record.chlorides)
            free_sulfur_dioxide = request.data.get('free_sulfur_dioxide', record.free_sulfur_dioxide)
            total_sulfur_dioxide = record.total_sulfur_dioxide('total_sulfur_dioxide', record.total_sulfur_dioxide)
            density = request.data.get('density', record.density)
            pH = request.data.get('pH', record.pH)
            sulphates = request.data.get('sulphates', record.sulphates)
            alcohol = request.data.get('alcohol', record.alcohol)
            quality = request.data.get('quality', record.quality)

            updated_record = KlasaCRUD.update(pk, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality)
            return Response(WineDataSerializer(updated_record).data)
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        """Delete a record"""
        record = KlasaCRUD.delete(pk)
        if record:
            return Response({'detail': 'Deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)