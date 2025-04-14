from django.shortcuts import render

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')  # o como se llame tu template
