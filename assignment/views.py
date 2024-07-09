from django.shortcuts import render,redirect
import requests
from .forms import EventForm, UserDataForm
from .models import UserData
import os
from dotenv import load_dotenv

 # Load environment variables from .env file
load_dotenv()

# Create your views here.

def streamlit_view(request):
    return render(request, 'streamlit.html')


def excercise_two_get_req(request):
    # URL of the external API
    api_url = 'https://api.api-ninjas.com/v1/randomuser'
    api_key = os.getenv("API_KEY")
    headers={'X-Api-Key': api_key}
    response = requests.get(api_url,headers=headers)
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
    data = response.json()
    print(data)
    if response.status_code == 200:
        #api_data = response.json() 
        user_info = {
            "username": data["username"],
            "sex": data["sex"],
            "address": data["address"],
            "name": data["name"],
            "email": data["email"],
            "birthday": data["birthday"]
        }
        context = {
            'user_info': user_info,
        }
    else:
        context = {
            'error_message': f"Failed to fetch data from API: {response.status_code}",
        }
    return render(request, 'exercise_two.html', context)

def get_historical_events(request):
    events = []
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            api_url = f'https://api.api-ninjas.com/v1/historicalevents?text={query}'
            api_key = os.getenv("API_KEY")  
            headers = {'X-Api-Key': api_key}
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                events = response.json()
            else:
                events = [{'year': 'N/A', 'event': 'No events found or error fetching events.'}]
    else:
        form = EventForm()
    
    return render(request, 'exercise_two_three.html', {'form': form, 'events': events})

def collect_user_data(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            UserData.objects.create(**form.cleaned_data)
            return redirect('display_user_data')
    else:
        form = UserDataForm()
    return render(request, 'exercise_four.html', {'form': form})

def display_user_data(request):
    users = UserData.objects.all()
    return render(request, 'exercise_five.html', {'users': users})