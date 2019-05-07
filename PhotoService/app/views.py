from django.shortcuts import render,get_object_or_404

# Create your views here.
def index(request):
    #requestが第一引数,第二引数はtemplatesフォルダからみてどこのファイルを参照するか
    return render(request, 'app/index.html')
