# i have created this file ---> Adil

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'harry','place':'Mars'}
    return render(request ,'adil.html' , params)
def analyze(request):
    #get the text 
    djtext = request.POST.get('text','default')
    #cheack the cheackbox values
    removepunc = request.POST.get('removepunc','OFF')
    fullcaps = request.POST.get('fullcaps','OFF') 
    lowercase = request.POST.get('lowercase','OFF') 
    newlineremover = request.POST.get('newlineremover','OFF') 
    extraspaceremover = request.POST.get('extraspaceremover','OFF') 
    charcount = request.POST.get('charcount','OFF') 

    # cheack which cheack box on 
    if removepunc=='on':
        # analyzed=djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext: 
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':"Removed Punctuations",'msg':'Please Smile, Your Analized Text is here.... ', 'Analyzed_text':analyzed}
        djtext=analyzed
        #analyzed the test
        # return render(request,'analyze.html',params)
    if fullcaps=='on':
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':"Change to UPPERCASE",'msg':'Please Smile, Your Analized Text is here.... ', 'Analyzed_text':analyzed}
        djtext=analyzed
        #analyzed the test
        # return render(request,'analyze.html',params)  
    if lowercase=='on':
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.lower()
        params={'purpose':"Change to UPPERCASE",'msg':'Please Smile, Your Analized Text is here.... ', 'Analyzed_text':analyzed}
        djtext=analyzed
        #analyzed the test
        # return render(request,'analyze.html',params)  
    if extraspaceremover=='on':
        analyzed=''
        for index,char in enumerate(djtext):
            if not(djtext[index]==" "and djtext[index+1]==""):
                analyzed=analyzed+char
        params={'purpose':"Removed New line",'msg':'Please Smile, Your Analized Text is here.... ', 'Analyzed_text':analyzed}
        djtext=analyzed
        #analyzed the test
        # return render(request,'analyze.html',params)
    if newlineremover=='on':
        analyzed=''
        for char in djtext:
            if char!="\n" and char!='\r':
                analyzed=analyzed+char 
        params={'purpose':"Removed New line",'msg':'Please Smile, Your Analized Text is here.... ', 'Analyzed_text':analyzed}
        djtext=analyzed
        #analyzed the test
        # return render(request,'analyze.html',params)
    if charcount=='on':
        analyzed=''
        for char in djtext:
            if char!=' ':
                analyzed=analyzed+char
        analyzed=len(analyzed)
        params={'purpose':"Removed New line",'msg':'no. of character in this text is'  ,'Analyzed_text':   analyzed}
        djtext=analyzed
        #analyzed the test
        # return render(request,'analyze.html',params)


    if(removepunc!='on' and  fullcaps!='on' and extraspaceremover!='on' and newlineremover!='on' and charcount!='on' and lowercase!='on'):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char 
        params={'purpose':"Without Any Opration",'msg':"please select any operation and try agin..... \nYour Current Text Is .... \n "  ,'Analyzed_text':   analyzed}
        
        return render(request,'analyze.html',params)
 
    return render(request,'analyze.html',params)