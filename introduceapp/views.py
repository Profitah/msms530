from django.shortcuts import render

# Create your views here.
def 시간표(request):
    return render(request,'시간표.html' )
def 실험용(request):
    return render(request,'실험용.html' )
def department(request):
    return render(request,'department.html' )
def flexgrid(request):
    return render(request,'flexgrid.html' )
def footer(request):
    return render(request,'footer.html' )