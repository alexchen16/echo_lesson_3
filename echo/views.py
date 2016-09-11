from django.shortcuts import render
from .models import Node
# Create your views here.
def list(request):
    data = Node.objects.all()
    print data
    context = {
        'data_template':data,
    }
    return render(request,'lists.html',context)