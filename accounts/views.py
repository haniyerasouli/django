from django.shortcuts import render

# Create your views here.
def ViewRegistration(request):
    return render(request,'accounts/register_page.html')