from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from web3 import Web3
import json
import os

def index(request):
    return render(request, 'kohl/index.html')