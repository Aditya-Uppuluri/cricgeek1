from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("Sriram, this is all you lol. Generate nice HTML Pages according to your plan. We will look into the animations later!")
    
def home(request):
    return render(request, '/Users/adityauppuluri/Desktop/ProjCricGeek/cricgeek/cricgeek/templates/cricgeek/homepage.html')
