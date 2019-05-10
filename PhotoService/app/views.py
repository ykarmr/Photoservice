from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import Photo

# Create your views here.
def index(request):
    #requestが第一引数,第二引数はtemplatesフォルダからみてどこのファイルを参照するか

    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'app/index.html',{'photos':photos})

def users_detail(request,pk):
    user = get_object_or_404(User, pk=pk)
    photos = user.photo_set.all().order_by('-created_at')
    return render(request, 'app/users_detail.html', {'user': user,'photos':photos})
