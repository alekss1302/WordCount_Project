from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    wordDictionary = {}

    for word in wordlist:
        if word in wordDictionary:
            #increase
            wordDictionary[word] += 1
        else:
            #add to the dictionary
            wordDictionary[word] = 1
    
    SortedWords = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'SortedWords':SortedWords})

def about(request):
    return render(request, 'about.html')