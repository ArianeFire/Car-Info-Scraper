# coding: utf-8
from __future__ import unicode_literals
import urllib;
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import unicodedata
import re;
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getMarqueImgLink():
	#Variable 
	link = "http://www.piecesauto.fr/marque-automobile.html";
	br = '\n';
	xml_data = '<?xml version="1.0"?>'+br+'<marques>'+br;
	
	#Data Extraction
	html = urllib.urlopen(link).read();
	soup = BeautifulSoup(html);
	#Retrieving the main div
	ulMain = soup.find("ul", {"class":"models"});
	liMarque = ulMain.find_all('li');
	for li in liMarque :
		a = li.find('a');
		img = a.find_all('img')[0];
		marque = a.getText();
		imgLink = img.get('src', None);
		#print("Marque : "+marque);
		#print("--->Lien Img"+imgLink);
		xml_data = xml_data+'<marque nom="'+marque+'">'+br+'<url>'+imgLink+'</url>'+br+'<modeles>'+br;
		
		file_name = marque.lower()+'.txt';
		
		#Download and save image
		#urllib.urlretrieve(imgLink, "marques/marques_img/"+marque+".jpg");
		#MODEL SCRAPPING
		if "CITR" in marque :
			linkToModel = "http://www.piecesauto.fr/marque-automobile/pieces-detachees-citroen.html";
		else :
			linkToModel = "http://www.piecesauto.fr/marque-automobile/pieces-detachees-"+str(marque.lower())+".html";
		#print("Lien Trouve : "+linkToModel);
		html = urllib.urlopen(linkToModel).read();
		soup = BeautifulSoup(html);
		#GET MODEL DIV ITEMS
		allDiv = soup.findAll('div', {'class':'item'});
		
		model_ch = "";
		
		for div in allDiv :
			img = div.find('img');
			nomModel = div.find('p').getText().strip();
			lienImg = img.get('src', None);
			#print("------>Modele "+nomModel);
			#print("--------->Lien"+lienImg);
			if '/' in nomModel :
				nomModel = nomModel.replace('/', '_');
			
			model_ch = model_ch + nomModel.lower() + '.jpg\n';
			
			#urllib.urlretrieve(lienImg, "marques/pieces_img/"+nomModel+".jpg");
			xml_data = xml_data+'<modele>'+br+'<nom>'+nomModel+'</nom>'+br;
			xml_data = xml_data+'<url>'+lienImg+'</url>'+br+'</modele>'+br;
		xml_data = xml_data+'</modeles>'+br;
		xml_data = xml_data + '</marque>'+br;
		
		f = open('marques/files/'+file_name, 'a+');
		f.write(model_ch);
		f.close();
		
	xml_data = xml_data + '</marques>';
	
	file = open('marques/files/marques.xml', 'a+');
	file.write(xml_data);
	file.close();
	print(xml_data);
#Main Call
getMarqueImgLink();