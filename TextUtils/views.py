#my views
#from django.http import HttpResponse

#def index(request):
#    return  HttpResponse('<h1>Rupok Bhai</h1>')

#def about(request):
#    return HttpResponse('<h1>About Rupok Bhai</h1>')

from django.http import HttpResponse
from django.shortcuts import render
#code for video 6
#def index(request):
 #   return HttpResponse('''<h1>hello rupok bhai</h1> <a href ="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9"> Django Code</a> ''')

#def about(request):
 #   return HttpResponse("<h1>About rupok bhai</h1>")

#code for video 7
def index(request):
    #params = {
     #   'name':'rupok',
      #  'place':'Mars'
    #}
    return render(request, 'index.html')
    #return HttpResponse("<h1>Hello!!</h1>")

def about(request):
    return HttpResponse("<h1>About Rupok Bhai!!!!!</h1>")

def analyze(request):
    #get text
    djtext=request.POST.get('text','default')

    #check checkbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover',"off")
    charcount=request.POST.get('charcount','off')


    #print(removepunc)
    #print(fullcaps)
    #print(newlineremover)
    #print(extraspaceremover)
    #print(charcount)
    #print(djtext)
    #return HttpResponse("<h1>remove punc!!!!!!</h1>")
    #analyzed=djtext

    #check which checkbox on
    if removepunc=="on":
        #print(removepunc)
        #print(djtext)
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            'purpose':'Remove Pauncuation',
            'analyzed_text': analyzed
        }
        #return render(request, 'analyze.html', params)
        djtext=analyzed
    if fullcaps=="on":
        #print(fullcaps)
        #print(djtext)
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params = {
            'purpose': 'Change to Uppercase',
            'analyzed_text': analyzed
        }
        #return render(request, 'analyze.html', params)
        djtext = analyzed
    if newlineremover=="on":
        #print(newlineremover)
        #print(djtext)
        analyzed=""
        for char in djtext:
            if char!="\n":
                analyzed = analyzed + char
        params = {
            'purpose': 'Remove New Line',
            'analyzed_text': analyzed
        }
        #return render(request, 'analyze.html', params)
        djtext = analyzed
    if extraspaceremover=="on":
        #print(extraspaceremover)
        #print(djtext)
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {
            'purpose': 'Remove Extra Space',
            'analyzed_text': analyzed
        }
        #return render(request, 'analyze.html', params)
        djtext = analyzed
    if (newlineremover!="on" and fullcaps!="on" and extraspaceremover!="on" and removepunc!="on"):
         return HttpResponse("<h1>PLEASE SELECT THE OPERATIONS AND TRY AGAIN BHAI!!</h1>")
   # if charcount=="on":
   #     analyzed = ""
   #     count = 0
   #     for char in djtext:
   #         if char!=0:
   #             count = count + 1
   #     params = {
   #           'purpose': 'Count Character',
   #         'analyzed_text': count
   #     }
   #     return render(request, 'analyze.html', params)

   # else:
   #     return HttpResponse("<h1>Error!!</h1>")
    return render(request, 'analyze.html', params)