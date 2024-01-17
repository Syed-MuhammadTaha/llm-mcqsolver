for i in range(20):
#     soup = BeautifulSoup(driver.page_source,features="html.parser")
#     prompt = soup.find("div", class_="ays_quiz_question")
#     option = soup.find_all("div", class_="ays-quiz-answers")
#     print(f"Question: {prompt.text}\n")
#     print(f"Answer: \n")
#     for j in option:
#         print(j.text.replace("\n",""))
#     next = driver.find_element(By.CLASS_NAME, "ays_next")
#     next.click()