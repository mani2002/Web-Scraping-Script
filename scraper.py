import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'
driver.get(url)
driver.implicitly_wait(6)

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Quest Number', 'Est. Value Notes', 'Description', 'Closing Date'])

    a_tag = driver.find_elements(By.XPATH,"//a[contains(@onclick,'prevnext')]")
    a = a_tag[0]
    a.click()
    for i in range(0,10):
        try:
            Quest_Number = driver.find_element(By.XPATH,'//h4/span/b')
            print(Quest_Number.text,"\n")
            row1 = driver.find_element(By.XPATH,'//table//tr[td[contains(text(), "Est. Value Notes:")]]')
            Est_Value_Notes = row1.find_element(By.XPATH,".//td[2]") # Or any other index of the td element
            print("Est. Value Notes:",Est_Value_Notes.text,"\n")
            row2 = driver.find_elements(By.XPATH,'//table//tr[td[contains(text(), "Description:")]]')
            description = row2[0].find_element(By.XPATH,".//td[2]") # Or any other index of the td element
            print("Description:",description.text,"\n")
            row3 = driver.find_element(By.XPATH,'//table//tr[td[contains(text(), "Closing Date")]]')
            closing_date = row3.find_element(By.XPATH,".//td[2]") # Or any other index of the td element
            print("Closing Date:",closing_date.text,"\n")
            
            writer.writerow([(Quest_Number.text).split(":")[1].strip(), Est_Value_Notes.text, description.text, closing_date.text])
            
        except Exception as e:
            print(e)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@id,'id_prevnext_next')]"))).click()
        time.sleep(2)
driver.quit()