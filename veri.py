import time
import  requests
from selenium import webdriver
from bs4 import BeautifulSoup

f=webdriver.Chrome()
a=f.get("https://www.linkedin.com/")
#//*[@id="login-submit"]s
time.sleep(3)
email=f.find_element_by_id("login-email")
password=f.find_element_by_id("login-password")
email.send_keys("")# enter email
password.send_keys("")# enter password
login=f.find_element_by_id("login-submit")
login.click()
response=requests.get("https://www.linkedin.com/feed/")
htmlcontent=response.content# content alımı
soup=BeautifulSoup(htmlcontent,"html.parser")
element=soup.find("span",{"aria-expanded":"true","class":"hoverable-link-text"})#çalıştırabilseyidim benzeri türetip
#  for döngüsüne girip gezdirip parse edicektim fazla hata alınca olmadı
print(element.text.strip())

time.sleep(6)

f.close()