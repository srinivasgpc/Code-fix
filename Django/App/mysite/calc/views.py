from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html',{'name':'srinivas'})




def operator(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    Add = val1 + val2
    sub = val1 - val2
    mul = val1 * val2
    div = val1 / val2
    avg = (val1 +val2) //2
    return render(request, 'result.html', {'Addition': Add , 'Subtraction': sub, 'multiply': mul, 'divide' : div, 'avarage' : avg })