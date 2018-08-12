# Selenium-Element-Scraper
Selenium Element Scraper is designed to return to you a list of elements from webpage that you specify.  

When creating selenium test cases some people including myself find it very tidous to inspect each element that was want to retrive. The point of this project is to automate farming web elements and attributes. 


Prerequisites:  
Install python2.7 (Make sure the python exe is in your system PATH)  
Install Selenium Webdriver  
Element_Scraper is using PhantomDriver (Make sure you have PhantomDriver installed and that the exe is in your PATH)  


Make sure prerequisites are completed before starting instructions  

Instructions:

Open cmd or terminal  
git clone https://github.com/arroyoc/Selenium-Element-Scraper  
cd Selenium-element-Scraper  
python Element_Scraper.py  

You will then be prompted for a URL:

URL: http://chrisarroyo.info  

id = navbarNavAltMarkup  
id = learnBtn  
id = githubLnk  
id = facebookLnk  
id = linkedinLnk  

After inputting your url, any element that has an id assigned to it will appear in a list.
