from urllib import response
#JsonResponse
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.


# Biometric appointment

def capture_id(request):
    
    result = request.GET['result']
    result1 = request.GET['result1']
    print(result, result1)
    # print(finger_print)
    
    return HttpResponse(200)
