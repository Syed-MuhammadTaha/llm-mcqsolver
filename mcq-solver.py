from bs4 import BeautifulSoup
import selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.testpreppractice.net/practice-tests/mcat-practice-tests/physical-sciences-practice-tests/physical-sciences-practice-test-1/")

soup = BeautifulSoup(driver.page_source,features="html.parser")
mcq = soup.find_all("div", class_="mcq-item")
print(mcq[0])

for i in mcq:
    prompt = i.find("div", class_="question-body").text
    option = i.find_all("li", class_="option")
    answer = i.find_all("li", class_="answer")
    print(f"Question: {prompt}\n")
    print(f"Answer: \n")
    for j in option:
        print(j.text.replace("\n",""))
    print("\n")

    





