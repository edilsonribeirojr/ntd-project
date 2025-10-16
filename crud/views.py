from django.http import JsonResponse
from django.shortcuts import render
import requests
from rest_framework import viewsets

from crud.models import Planets
from crud.serializer import PlanetSerializer


class PlanetsViewSet(viewsets.ModelViewSet):
    queryset = Planets.objects.all()
    serializer_class = PlanetSerializer
def import_data_from_endpoint(request):
    url = "https://swapi-graphql.netlify.app/graphql?query=query+Query+%7BallPlanets%7Bplanets%7Bname+population+terrains+climates%7D%7D%7D"
    try:
        response = requests.get(url)
        response.raise_for_status()
        original_data = response.json()
        data = original_data.get('data', {}).get('allPlanets', {}).get('planets', [])

        for item in data:
            print(item)
            Planets.objects.update_or_create(
                name=item['name'],
                defaults={
                    'population': item['population'],
                    'climates': item['climates'],
                    'terrains': item['terrains']
                }
            )
        return JsonResponse({'message': 'Imported successfully'})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)