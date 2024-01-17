from bs4 import BeautifulSoup
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://ilm.com.pk/online-test/1st-year-math-chapter-1-number-system-mcqs-with-answers/")


main_next = driver.find_element(By.CLASS_NAME, "ays_next")

main_next.click()

for i in range(20):
    soup = BeautifulSoup(driver.page_source,features="html.parser")
    prompt = soup.find("div", class_="ays_quiz_question")
    option = soup.find_all("div", class_="ays-quiz-answers")
    print(f"Question: {prompt.text}\n")
    print(f"Answer: \n")
    for j in option:
        print(j.text.replace("\n",""))
    time.sleep(3)
    next = driver.find_element(By.CLASS_NAME, "ays_next")
    next.click()




time.sleep(100)