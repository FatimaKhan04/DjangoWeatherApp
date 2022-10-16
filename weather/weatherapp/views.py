from django.shortcuts import render
import urllib.request
import json
# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        #source will contain all json data from api
        source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+ city 
                                      +'&units=metric&appid=28e808e0d0e4661efebc1de431d578a6').read()
        list_of_data=json.loads(source)
        data={
            'country_code':str(list_of_data['sys']['country']),
            'coordinates':str(list_of_data['coord']['lat'])+str(list_of_data['coord']['lon']),
            'temp':str(list_of_data['main']['temp'])+ ' °C',
            'pressure':str(list_of_data['main']['pressure']),
            'humidity':str(list_of_data['main']['humidity']),
            'main':str(list_of_data['weather'][0]['main']),
            'description':str(list_of_data['weather'][0]['description']),
            'icon':list_of_data['weather'][0]['icon'],
        }
        
    else:
        data={}
    print(data)    
    return render(request,'index.html',data)