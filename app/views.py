from django.shortcuts import render

# Create your views here.
def ashu(request):
    return render(request,'Ashu.html',context={'name':'Ashu','age':2})


def nikky(request):
    return render(request,'nikky.html')