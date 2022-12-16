from django.shortcuts import render
import requests
import json
from .models import Person
from django.template import RequestContext
# Create your views here.




#https://api.dictionaryapi.dev/api/v2/entries/en/<word>




def index(request):
   
   return render(request, 'index.html')
   
   
def output(request):
    word = request.GET['word']
    words = word
    
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'  + word
    r = requests.get(url).json()

    #its another method but i had not used .
    #print(r)
   #  data1= r[0]['word']
   #  data2 = r[0]['meanings']
   #  data3 = data2[0]['partOfSpeech']
   #  data4 = data2[0]['definitions'][0]['definition']
   #  data5 = data2[0]['definitions'][1]['definition']
   #  data6 = data2[0]['synonyms']
   #  data7 = data2[0]['antonyms']
   #  data8 = data2[0]['definitions'][2]['definition']
   #  data9 = data2[0]['definitions'][0]['synonyms']
   #  data10 = data2[0]['definitions'][1]['synonyms']
   #  data11 = data2[0]['definitions'][2]['synonyms']
   #  data12 = data2[0]['definitions'][0]['antonyms']
   #  data13 = data2[0]['definitions'][1]['antonyms']
   #  data14 = data2[0]['definitions'][2]['antonyms']

    
    
   #  dict1 ={
   #    'word':data1,'partofSpeech':data3, 'defination':[data4,data5,data8],'synonyms':[data9,data10,data11,data6,data7],'antonyms':[data12,data13,data14]

   #  }

    return render(request, 'output.html',{'r':r})




def error_500(request):
   return render(request,'500.html')