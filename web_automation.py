from selenium import webdriver
import time
import os

#open in Chrome browser
driver = webdriver.Chrome()

#open the site
driver.get('http://server.poissonboltzmann.org/pdb2pqr')

#click on 'Upload a pdb file'
upload_button = driver.find_element_by_xpath('//*[@id="pdb2pqr"]/section/main/div/form/div[1]/div[2]/div/div/div/label[2]/span[1]')
upload_button.click()

#click on 'select file'
select_file_button = driver.find_element_by_xpath('//*[@id="pdb2pqr"]/section/main/div/form/div[2]/div/div/div[2]/div/div/span/div[1]/span/button/span[2]')
select_file_button.click()

#upload file
os.system('C:/Users/user/Desktop/AutoIt/Fileupload.exe')
#.exe file needs compilation every time

#click on 'No pKa calculation'
pKa_button = driver.find_element_by_xpath('//*[@id="pka_none"]')
pKa_button.click()

#click on 'Charmm'
charmm_button = driver.find_element_by_xpath('//*[@id="pdb2pqr"]/section/main/div/form/div[5]/div[2]/div/div/div/label[2]/span[1]')
charmm_button.click()

#(un)click on 'Remove waters from the output file
remove_water_button = driver.find_element_by_xpath('//*[@id="pdb2pqr"]/section/main/div/form/div[7]/div[2]/div/div/div/div[10]/div/label/span[1]/input')
remove_water_button.click()

#click on 'Start Job'
start_job_button = driver.find_element_by_xpath('//*[@id="pdb2pqr"]/section/main/div/form/div[8]/div/div/div/div/div/div[2]/div/div/button/span')
start_job_button.click()

#wait 20 second
time.sleep(15)

#download .pqr file
download_pqr = driver.find_element_by_xpath('//*[@id="pdb2pqr"]/main/div/div[2]/div[2]/div[2]/div[2]/div/ul/li[4]/ul/li/a')
download_pqr.click()

time.sleep(2)

#click on 'Tools'
tools_button = driver.find_element_by_xpath('//*[@id="root"]/div/section/nav/div/div[2]/aside/div[1]/ul/li[2]/div')
tools_button.click()

#Refresh to start over
refresh = driver.find_element_by_xpath('//*[@id="root"]/div/section/nav/div/div[2]/aside/div[1]/a/img')
refresh.click()

button = driver.find_element_by_xpath('//*[@id="root"]/div/section/section/section/div[1]/div/div[2]/main/div/button[1]/a')
button.click()
