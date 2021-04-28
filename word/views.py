from django.shortcuts import render
import operator
# Create your views here.

def home(request):
    return render(request, "word/home.html")

def count(request):
    fulltext = request.GET['textarea']
    fulltx = len(fulltext)
    wordlist = fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+= 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'word/count.html' , {'text' : fulltext, 'count': len(wordlist), 'worddictionary': sortedwords, 'fulltx':fulltx})