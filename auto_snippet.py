#change file name
"""
import os

folder_path = "/path/to/folder"
for filename in os.listdir(folder_path):
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path,filename.replace(" ","_")))

"""
"""
#automated email sending, need to set up app password
#https://support.google.com/accounts/answer/185833?sjid=12518287091242123724-NA
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("catechnix@gmail.com","Twins2009#")

msg = "Hello, this is a test email!"
server.sendmail("catechnix@gmail.com","catechnix@gmail.com",msg)
server.quit()

"""

"""
Data extraction from Excel
"""
import pandas as pd
data = pd.read_excel("example.xlsx")
print(data.head)

"""
Automated web browsing
"""
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://www.python.org")
print(browser.title)
browser.quit() 

"""
Automated image downloading
"""
import urllib.request
urllib.request.urlretrieve("https://www.python.org/static/img/python-logo.png", "python-logo.png")

"""
Data Backup
"""
import shutil
shutil.copy2("/path/to/file.txt","/path/to/destination_folder")

"""

"""
                           
