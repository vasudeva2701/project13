from django.shortcuts import render

# Create your views here.
def condition(request):
    d={ 'a':100}
    return render(request,'jinja.html',context=d)
def condition(request):
    a={'a':501,'b':601,'c':1006}
    return render(request,'jinja.html',context=a)

