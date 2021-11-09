from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import request
import random


# Home page 
def home(request):
    # return HttpResponse('<h1>Welcome!</h1>')
    return render(request, 'generator/home.html', {'param':'hyjk12K0si'})

# Password generation 
def password(request):
    character = list('abcdefghijklmnopqrstuvwxyz')
    # get the length 
    length =int(request.GET.get('length', 8)) #8 is default length

    # get the Uppercase char  & extend it into character
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    # get the special char & extend  it into character
    if request.GET.get('special'):
        character.extend(list('!@#$&^%*()?'))
    
    # get the numbers & extend it into character
    if request.GET.get('numbers'):
        character.extend(list('0123456789'))        

     
    pswd = ''
    for x in range(length):
        pswd += random.choice(character)
        print(pswd)
    return render(request, 'generator/password.html', {'param':pswd})