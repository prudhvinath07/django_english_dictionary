from django.shortcuts import render
from PyDictionary import PyDictionary
from wordhoard import Antonyms
#from wordhoard import Definitions
from wordhoard import Synonyms

def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()

    antonym = Antonyms(search)
    antonyms = antonym.find_antonyms()

    synonym = Synonyms(search)
    synonyms = synonym.find_synonyms()

    meaning = dictionary.meaning(search)
  
    context = {
        'meaning': meaning, 
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    return render(request, 'word.html', context)
