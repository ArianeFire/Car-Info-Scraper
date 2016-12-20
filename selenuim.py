from selenium import webdriver
import scrapper
import dbmanager

#print(marques[0])
def getAllData(marques, browser):
	br = '\n';
	xml_data = '<?xml version="1.0" ?>'+br;
	xml_data = xml_data+'<marques>'+br;
	for marque in marques:
		marque = marque.strip('\n\r')
		#print('La Marque : '+marque)
		xml_data = xml_data + '<marque nom="'+marque+'">'+br;
		marque_id = marque+'_id'
		#dbmanager.insertMarque(marque, marque_id)
		try :
			browser.find_element_by_xpath('//*[@id="mcvFrmInfoAuto:marque"]/option[contains(text(), "'+marque+'")]').click()
		except :
			break;
		#print(browser.page_source)
		page = browser.page_source
		modeles = scrapper.getOption(page, "mcvFrmInfoAuto:modele")
		for modele in modeles :
			#print('--->Le Modele'+modele)
			xml_data = xml_data + '<modele nom="'+modele+'">'+br;
			modele_id = modele+'_id'
			#dbmanager.insertModele(modele, marque_id, modele_id)
			try :
				browser.find_element_by_xpath('//*[@id="mcvFrmInfoAuto:modele"]/option[contains(text(), "'+modele+'")]').click()
			except :
				break;
			page = browser.page_source
			types = scrapper.getOption(page, "mcvFrmInfoAuto:type")
			for type in types :
				#dbmanager.insertType(type, modele_id)
				xml_data = xml_data + '<type>'+type+'</type>'+br;
				#print('------>Le Type : '+type)
			xml_data = xml_data + '</modele>'+br;
			
		xml_data = xml_data + '</marque>'+br;
	xml_data = xml_data + '</marques>';
	file = open('douane/nonHybride.xml', 'a+');
	file.write(xml_data);
	file.close();
	print(xml_data);
#===================================MAIN PART================================
path_to_chromedriver = 'C:\Users\SEYDOU BERTHE\PROJETS\AUTO_SCRAPPING\chromedriver' # change path as needed
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
url = 'http://www.douane.gov.ma/mcv/informationAutomobile.jsf'
browser.get(url)

print('=======================Non Hybride====================')
marquess = scrapper.getData()
getAllData(marquess, browser)
print('=======================Hybride=========================')		
#browser.find_element_by_xpath('//input[@id="mcvFrmInfoAuto:genre:1"]').click()
#page = browser.page_source
#print(page)
#page = open("second.html", "a+").read()
#secondCategorie = scrapper.getDataV0(page)
#getAllData(secondCategorie, browser)
#print('=======================Utilitaires=====================')
#browser.find_element_by_xpath('//input[@id="mcvFrmInfoAuto:genre:2"]').click()
#page = browser.page_source
#page = open("third.html", "a+").read()
#thirdCategorie = scrapper.getDataV0(page)
#getAllData(thirdCategorie, browser)