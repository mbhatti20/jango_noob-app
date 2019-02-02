from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()

    worddiction={}
    for word in wordlist:
        if word in worddiction:
            worddiction[word]+=1
        else:
            worddiction[word]=1
    
    sortedword=sorted(worddiction.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedword':sortedword})



def about(request):
    return render(request,'about.html')