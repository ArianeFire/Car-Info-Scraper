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

def getOption(page, name):
	#print(name)
	datas = []
	soup = BeautifulSoup(page)
	tags = soup.find("select", {"id":name})
	if tags != None :
		for tag in tags :
			if tag.string != None and tag.string.strip() != "" :
				datas.append(tag.string)
	return datas;

def getData():
	link = str('http://www.douane.gov.ma/mcv/informationAutomobile.jsf');
	
	#Variable 
	marques = [];
	
	#Data Extraction
	html = urllib.urlopen(link).read();
	soup = BeautifulSoup(html);
	
	tag_car = soup.find("select", {"name":"mcvFrmInfoAuto:marque"});
	for tag in tag_car :
		if tag.string != None and tag.string.strip() != "":
			#print(tag.string);
			marques.append(tag.string.strip())
	return marques

def getDataV0(html):
	#link = str('http://www.douane.gov.ma/mcv/informationAutomobile.jsf');
	
	#Variable 
	marques = [];
	soup = BeautifulSoup(html);
	
	tag_car = soup.find("select", {"id":"mcvFrmInfoAuto:marque"});
	for tag in tag_car :
		if tag.string != None and tag.string.strip() != "":
			#print(tag.string);
			marques.append(tag.string.strip())
	return marques
	
	
getData()