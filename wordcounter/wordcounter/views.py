from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,'home.html')

def count(request):
	full = request.GET['fulltext']
	wordcount = full.split()

	worddict = {}

	for word in wordcount:
		if word in worddict:
			#Incerase
			worddict[word] += 1
		else:
			worddict[word] = 1


	sortedword = sorted(worddict.items(),key = operator.itemgetter(1), reverse = True)
	return render(request,'count.html',{'fulltext':full,'count':len(wordcount),'sortedword':worddict.items()})
def about(request):
	return render(request,'about.html')