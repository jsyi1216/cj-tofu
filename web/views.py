import json

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from prediction_Module.mnist_nn_predict import predict
from .forms import ImageUploadForm
from rest_framework import viewsets
from web.serializers import PredictSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

def index(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_object = form.save(commit=True)

            name = image_object.image.name.split('/')[1]
            path = image_object.image.url

            try:
                label = predict(image_object.image.path)
            except:
                label = '비정상'

            return render(request, 'index.html', locals())
        # else:
            # raise Http404
    return render(request, 'index.html')

# class PredictViewSet(viewsets.ModelViewSet):
#     serializer_class = PredictSerializer
#     http_method_names = ['post']

#     @csrf_exempt
#     def create(self, request):
#         data = JSONParser().parse(request)
#         serializer = PredictSerializer(data=data)
#         results = ''

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'predictions': results}, status=201)
#         return JsonResponse(serializer.errors, status=400)