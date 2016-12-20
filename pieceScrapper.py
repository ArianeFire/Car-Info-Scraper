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

def getPieceFromLink():
	#Variable 
	link = "http://www.piecesauto.fr/pieces-detachees.html";
	categories = [];
	pieces = [];
	
	#XML FORM VARIABLE
	br = '\n';
	xml_data = '<?xml version="1.0"?>'+br+'<pieces>'+br;
	#Data Extraction
	html = urllib.urlopen(link).read();
	soup = BeautifulSoup(html);
	#Retrieving the main div
	divMain = soup.find("div", {"class":"items"});
	divPieces = divMain.find_all('div');
	for div in divPieces :
		cat = div.find_all('h4')[0].string.strip();
		xml_data = xml_data+'<categorie nom="'+cat+'">'+br;
		cat = cat.encode('utf-8').decode(sys.stdout.encoding);
		#print("Categorie : "+cat);
		pieces = div.find_all('a');
		#print("--->Pieces : ")
		for piece in pieces:
			p = piece.string.strip();
			xml_data = xml_data+'<piece>'+p+'</piece>'+br;
			p = piece.encode('utf-8').decode(sys.stdout.encoding);
			#print("------>"+p);
		xml_data = xml_data+'</categorie>'+br;
	xml_data = xml_data+'</pieces>'+br;
	file = open('marques/files/pieces.xml', 'a+');
	file.write(xml_data);
	file.close();
	print(xml_data.encode('utf-8').decode(sys.stdout.encoding));
#MAIN CALL
getPieceFromLink();