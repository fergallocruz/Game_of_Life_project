import json
from re import T
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import encoding
from django.utils.safestring import SafeString
from django.utils.encoding import force_str
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import COVIDData
from .serializers import StateSexSerializer, StateSexAgeSerializer, DeadPeopleSerializer, SickPeopleSerializer, SectorSerializer
import pandas as pd
from rest_framework.renderers import JSONRenderer
from django.core.serializers import serialize
# Create your views here.

""" def index(request):
    filtered_data = ListPeople
    context = {'data_json':SafeString('')}
    return render(request, 'covid_app/index.html', context) """

def index(request):
    covid_list = COVIDData.objects.all()
    serializer = StateSexSerializer(covid_list, many=True)
    # Convert the QuerySet to a List
    list_of_dicts = list(serializer.data)
    # Convert List of Dicts to JSON
    data = json.dumps(list_of_dicts, ensure_ascii=False)
    context = {'data_json': SafeString(data)}
    return render(request, 'covid_app/index.html', context)

""" def index01(request):
    covid_list = COVIDData.objects.all()
    serializer = StateSexAgeSerializer(covid_list, many=True)
    # Convert the QuerySet to a List
    list_of_dicts = list(serializer.data)
    # Convert List of Dicts to JSON
    data = json.dumps(list_of_dicts, ensure_ascii=False)
    context = {'data_json': SafeString(data)}
    return render(request, 'covid_app/index.html', context) """

def pie_chart(request):
    # covid_df = pd.DataFrame.from_records(data)
    donut_json = '[ { "region": "East", "fruit": "Apples", "count": "53245" }, { "region": "West", "fruit": ' \
                 '"Apples", "count": "28479" }, { "region": "South", "fruit": "Apples", "count": "19697" }, ' \
                 '{ "region": "North", "fruit": "Apples", "count": "24037" }, { "region": "Central", ' \
                 '"fruit": "Apples", "count": "40245" }, { "region": "East", "fruit": "Oranges", "count": "200" ' \
                 '}, { "region": "South", "fruit": "Oranges", "count": "200" }, { "region": "Central", ' \
                 '"fruit": "Oranges", "count": "200" }] '
    context = {'data_json': SafeString(donut_json)}
    return render(request, 'covid_app/donut.html', context)


def radial(request):
    covid_list = COVIDData.objects.all()
    serializer = DeadPeopleSerializer(covid_list, many=True)
    # Convert the QuerySet to a List
    list_of_dicts = list(serializer.data)
    # Convert List of Dicts to JSON
    data = json.dumps(list_of_dicts, ensure_ascii=False)
    context = {'data_json': SafeString(data)}
    return render(request, 'covid_app/radial.html', context)


def bubble(request):
    covid_list = COVIDData.objects.all()
    serializer = SickPeopleSerializer(covid_list, many=True)
    # Convert the QuerySet to a List
    list_of_dicts = list(serializer.data)
    # Convert List of Dicts to JSON
    data = json.dumps(list_of_dicts, ensure_ascii=False)
    context = {'data_json': SafeString(data)}
    return render(request, 'covid_app/bubble.html', context)

def multiple(request):
    covid_list = COVIDData.objects.all()
    serializer = SectorSerializer(covid_list, many=True)
    # Convert the QuerySet to a List
    list_of_dicts = list(serializer.data)
    # Convert List of Dicts to JSON
    data = json.dumps(list_of_dicts, ensure_ascii=False)
    context = {'data_json': SafeString(data)}
    return render(request, 'covid_app/multiple.html', context)

class ListPeople(APIView):
    """
    View to all infected people, the regirter, sex, state and municipality.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        queryset = COVIDData.objects.all()
        serializer = StateSexSerializer(queryset, many=True)
        print(request)
        return Response(serializer.data)


class StateSexSet(viewsets.ModelViewSet):
    queryset = COVIDData.objects.all()
    serializer_class = StateSexSerializer
    # permission_classes = [permissions.IsAuthenticated]
    filter_fields = ['entidad_res', 'municipio_res']


class StateSexAgeSet(viewsets.ViewSet):
    queryset = COVIDData.objects.all()
    serializer_class = StateSexAgeSerializer

    def list(self, request, *args, **kwargs):
        # age = request.GET['age']
        # covid_df = pd.DataFrame.from_records(COVIDData.objects.filter(edad__gt=age). \
        #                                     values('id_registro', 'sexo', 'entidad_res', 'municipio_res', 'edad'))
        # print(covid_df)
        # df = covid_df["sexo"].value_counts()
        # print(df)
        # return Response(str(covid_df.to_json(orient='records')))
        donut_json = '[ { "region": "East", "fruit": "Apples", "count": "53245" }, { "region": "West", "fruit": ' \
                     '"Apples", "count": "28479" }, { "region": "South", "fruit": "Apples", "count": "19697" }, ' \
                     '{ "region": "North", "fruit": "Apples", "count": "24037" }, { "region": "Central", ' \
                     '"fruit": "Apples", "count": "40245" }, { "region": "East", "fruit": "Oranges", "count": "200" ' \
                     '}, { "region": "South", "fruit": "Oranges", "count": "200" }, { "region": "Central", ' \
                     '"fruit": "Oranges", "count": "200" }] '
        return Response(SafeString(donut_json))
