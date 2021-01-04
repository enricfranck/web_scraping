'''
Created on 30 déc. 2020

@author: Enric
'''
from bs4 import BeautifulSoup; 
from django.shortcuts import render
import requests;


def welcome(request):
    #teste si le formulaire a été envoyer
    if len(request.POST)>0:
        
        #teste si l'utilisateur a bien saisir l'url
        if 'text_url' not in request.POST:
            return render(request,'welcome.html');
        else: 
            url=request.POST["text_url"];
            nom=getNom(url);
            if nom != "erreur":
                return render(request,'information.html',{'nom':nom,'version':getVersion(url),
                                                          'nombre':getNbrTelecharge(url),
                                                          'date':getDatePublication(url),
                                                          'description':getDescription(url)});
            else :
                return render(request,'welcome.html');
                
    else:
        return render(request,'welcome.html');

def information(request):
    return render(request,'information.html');

''' Methode pour récuperer le nom de l'application'''
def getNom(url:str)->str:
    try:
        reponse=requests.get(url);
        soup=BeautifulSoup(reponse.text,"html.parser");
        nom=soup.find(class_="header-desktop__AppName-xc5gow-5 fzCqyh")
        return nom.get_text();
    except:
        return "erreur";
    
    
''' Methode pour récuperer le nombre de téléchargement de l'application'''
def getNbrTelecharge(url:str)->str:
    try:
        reponse=requests.get(url);
        soup=BeautifulSoup(reponse.text,"html.parser");
        nbre=soup.find(class_="label-with-icon__LabelWithIcon-sc-162xi5e-0 bZRhOm")
        return nbre.get_text();
    except:
        return "erreur";
    

''' Methode pour récuperer la déscription de l'application'''
def getDescription(url:str)->str:
    try:
        reponse=requests.get(url);
        soup=BeautifulSoup(reponse.text,"html.parser");
        desc=soup.find(class_="description__DescBody-sc-45j1b1-0 gdwZQU")
        return desc.get_text();
    except:
        return "erreur";
    

''' Methode pour récuperer la date de publication de l'application'''
def getDatePublication(url:str)->str:
    try:
        reponse=requests.get(url);
        soup=BeautifulSoup(reponse.text,"html.parser");
        desc=soup.find_all('div',{"class":"sc-AxiKw versions-carrousel-card__CardLeft-sc-1jr23ac-2 ljuySx"})
        return desc;
    except:
        return "erreur"
    

''' Methode pour récuperer la version de l'application'''
def getVersion(url:str)->str:
    try:
        reponse=requests.get(url);
        soup=BeautifulSoup(reponse.text,"html.parser");
        vers=soup.find(class_="information__Value-xn2n41-2 dvSoPl")
        return vers.get_text();
    except:
        return "erreur";