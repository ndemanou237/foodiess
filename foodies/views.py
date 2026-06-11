from django.shortcuts import render

def HomeView(request):
    return render(request,'home.html')

def MenuView(request):
    return render(request,'menu.html')

def ProposView(request):
    return render(request,'propos.html')

def ReservationView(request):
    return render(request,'reservation.html')

def ContactView(request):
    return render(request,'contact.html')

def PanierView(request):
    return render(request,'panier.html')

def ConnexionView(request):
    return render(request,'connexion.html')

def InscriptionView(request):
    return render(request,'inscription.html')
