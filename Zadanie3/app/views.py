import json
import random

from django.http import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

from .crud import WineDataCRUD
from .models import WineData
from .serializers import WineDataSerializer

def home_view(request):
    return render(request, 'home_template.html')

class KlasaListCreateAPIView(APIView):
    def get(self, request):
        """Get all records"""
        try:
            records = WineDataCRUD.read_all()
            serializer = WineDataSerializer(records, many=True)
            return Response(serializer.data)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        """Create a new record"""
        try:
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
                new_record = WineDataCRUD.create(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality)
                return Response(WineDataSerializer(new_record).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class KlasaDetailAPIView(APIView):
    def get(self, request, pk):
        """Get a single record by ID"""
        try:
            record = WineDataCRUD.read_by_id(pk)
            if record:
                serializer = WineDataSerializer(record)
                return Response(serializer.data)
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        """Update a record"""
        try:
            record = WineDataCRUD.read_by_id(pk)
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

                updated_record = WineDataCRUD.update(pk, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality)
                return Response(WineDataSerializer(updated_record).data)
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        """Delete a record"""
        try:
            record = WineDataCRUD.delete(pk)
            if record:
                return Response({'detail': 'Deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
            return Response({'error': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def delete_record(request, pk):
    try:
        if request.method == "POST":
            record = WineDataCRUD.delete(pk)
            if record:
                return redirect('/')
            return Response({'error': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return HttpResponseNotAllowed(['POST'], content="Method not allowed.")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def add_view(request):
    return render(request, 'add_form.html')

def generate_example_data(request):
    try:
        if request.method == "GET":
            engine = create_engine('sqlite:///python3task.db')
            Session = sessionmaker(bind=engine)
            session = Session()

            if (session.query(WineData).count() < 2):
                raise Exception("Cannot generate random data, database do not have enough data")

            min_max_val = {}

            min_max_val['fixed_acidity'] = session.query(func.min(WineData.fixed_acidity), func.max(WineData.fixed_acidity)).one()
            min_max_val['volatile_acidity'] = session.query(func.min(WineData.volatile_acidity), func.max(WineData.volatile_acidity)).one()
            min_max_val['citric_acid'] = session.query(func.min(WineData.citric_acid), func.max(WineData.citric_acid)).one()
            min_max_val['residual_sugar'] = session.query(func.min(WineData.residual_sugar), func.max(WineData.residual_sugar)).one()
            min_max_val['chlorides'] = session.query(func.min(WineData.chlorides), func.max(WineData.chlorides)).one()
            min_max_val['free_sulfur_dioxide'] = session.query(func.min(WineData.free_sulfur_dioxide), func.max(WineData.free_sulfur_dioxide)).one()
            min_max_val['total_sulfur_dioxide'] = session.query(func.min(WineData.total_sulfur_dioxide), func.max(WineData.total_sulfur_dioxide)).one()
            min_max_val['density'] = session.query(func.min(WineData.density), func.max(WineData.density)).one()
            min_max_val['pH'] = session.query(func.min(WineData.pH), func.max(WineData.pH)).one()
            min_max_val['sulphates'] = session.query(func.min(WineData.sulphates), func.max(WineData.sulphates)).one()
            min_max_val['alcohol'] = session.query(func.min(WineData.alcohol), func.max(WineData.alcohol)).one()
            min_max_val['quality'] = session.query(func.min(WineData.quality), func.max(WineData.quality)).one()

            # Generowanie losowych danych
            random_data = {
                "fixed_acidity": round(random.uniform(min_max_val['fixed_acidity'][0], min_max_val['fixed_acidity'][1]), 2),
                "volatile_acidity": round(random.uniform(min_max_val['volatile_acidity'][0], min_max_val['volatile_acidity'][1]), 2),
                "citric_acid": round(random.uniform(min_max_val['citric_acid'][0], min_max_val['citric_acid'][1]), 2),
                "residual_sugar": round(random.uniform(min_max_val['residual_sugar'][0], min_max_val['residual_sugar'][1]), 2),
                "chlorides": round(random.uniform(min_max_val['chlorides'][0], min_max_val['chlorides'][1]), 3),
                "free_sulfur_dioxide": round(random.uniform(min_max_val['free_sulfur_dioxide'][0], min_max_val['free_sulfur_dioxide'][1]), 3),
                "total_sulfur_dioxide": round(random.uniform(min_max_val['total_sulfur_dioxide'][0], min_max_val['total_sulfur_dioxide'][1]), 3),
                "density": round(random.uniform(min_max_val['density'][0], min_max_val['density'][1]), 5),
                "pH": round(random.uniform(min_max_val['pH'][0], min_max_val['pH'][1]), 2),
                "sulphates": round(random.uniform(min_max_val['sulphates'][0], min_max_val['sulphates'][1]), 2),
                "alcohol": round(random.uniform(min_max_val['alcohol'][0], min_max_val['alcohol'][1]), 2),
                "quality": random.randint(min_max_val['quality'][0], min_max_val['quality'][1])
            }

            return JsonResponse(random_data)

        return JsonResponse({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def predict_quality(request):
    try:
        if request.method == "POST":
            engine = create_engine('sqlite:///python3task.db')
            Session = sessionmaker(bind=engine)
            session = Session()

            if(session.query(WineData).count()==0):
                raise Exception("Cannot predict quality, database is empty")
            if(session.query(WineData.quality).count()<5):
                neighbours = session.query(WineData.quality).count()
            else:
                neighbours = 5

            try:
                data = json.loads(request.body)

                fixed_acidity = float(data['fixed_acidity'])
                volatile_acidity = float(data['volatile_acidity'])
                citric_acid = float(data['citric_acid'])
                residual_sugar = float(data['residual_sugar'])
                chlorides = float(data['chlorides'])
                free_sulfur_dioxide = float(data['free_sulfur_dioxide'])
                total_sulfur_dioxide = float(data['total_sulfur_dioxide'])
                density = float(data['density'])
                pH = float(data['pH'])
                sulphates = float(data['sulphates'])
                alcohol = float(data['alcohol'])
            except Exception as e:
                print("Error:", e)
                return JsonResponse({"error": "All values have to be a numbers - " + str(e)}, status=status.HTTP_400_BAD_REQUEST)

            #predict_X = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]

            records = WineDataCRUD.read_all()
            data = [record.get_train_data()[0] for record in records]

            data.append([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol])

            scaler = MinMaxScaler()
            scaler.fit(data)
            scaled_X = scaler.transform(data)

            print(scaled_X)
            train_y = np.array([record.get_train_data()[1] for record in records]).ravel()
            train_X = np.array(scaled_X[:-1])
            predict_X = np.array(scaled_X[-1]).reshape(1, -1)

            print(train_X)
            print(predict_X)
            print(neighbours)

            knn = KNeighborsClassifier(n_neighbors=neighbours)
            knn.fit(train_X, train_y)

            prediction = knn.predict(predict_X)
            print("Prediction: " + str(prediction))
            return JsonResponse({"prediction": str(prediction[0])})

        return render(request, 'predict_form.html')
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def predict_quality_method(request):
    try:
        if request.method != "GET":
            return JsonResponse({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        engine = create_engine('sqlite:///python3task.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        if (session.query(WineData).count() == 0):
            raise Exception("Cannot predict quality, database is empty")
        if (session.query(WineData.quality).count() < 5):
            neighbours = session.query(WineData.quality).count()
        else:
            neighbours = 5

        try:
            fixed_acidity = float(request.GET.get('fixed_acidity'))
            volatile_acidity = float(request.GET.get('volatile_acidity'))
            citric_acid = float(request.GET.get('citric_acid'))
            residual_sugar = float(request.GET.get('residual_sugar'))
            chlorides = float(request.GET.get('chlorides'))
            free_sulfur_dioxide = float(request.GET.get('free_sulfur_dioxide'))
            total_sulfur_dioxide = float(request.GET.get('total_sulfur_dioxide'))
            density = float(request.GET.get('density'))
            pH = float(request.GET.get('pH'))
            sulphates = float(request.GET.get('sulphates'))
            alcohol = float(request.GET.get('alcohol'))
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # predict_X = np.array([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]).reshape(1, -1)
        #
        # records = WineDataCRUD.read_all()
        # train_X = [record.get_train_data()[0] for record in records]
        # train_X = np.array(train_X)
        # train_y = [record.get_train_data()[1] for record in records]
        # train_y = np.array(train_y).ravel()
        #
        # knn = KNeighborsClassifier(n_neighbors=5)
        # knn.fit(train_X, train_y)
        #
        # prediction = knn.predict(predict_X)
        #
        # return JsonResponse({"prediction": str(prediction[0])})

        records = WineDataCRUD.read_all()
        data = [record.get_train_data()[0] for record in records]

        data.append([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide,
                     total_sulfur_dioxide, density, pH, sulphates, alcohol])

        scaler = MinMaxScaler()
        scaler.fit(data)
        scaled_X = scaler.transform(data)

        print(scaled_X)
        train_y = np.array([record.get_train_data()[1] for record in records]).ravel()
        train_X = np.array(scaled_X[:-1])
        predict_X = np.array(scaled_X[-1]).reshape(1, -1)

        print(train_X)
        print(predict_X)
        print(neighbours)

        knn = KNeighborsClassifier(n_neighbors=neighbours)
        knn.fit(train_X, train_y)

        prediction = knn.predict(predict_X)
        print("Prediction: " + str(prediction))
        return JsonResponse({"prediction": str(prediction[0])})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def result_page(request):
    return render(request, 'prediction_result.html')

def error_page(request):
    return render(request, 'error_occured.html')