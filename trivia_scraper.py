from selenium import webdriver
from time import sleep

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
TRIVIA_PATH = "C:\\Users\\darre\\Desktop\\DronBot\\trivia_qa.txt"

driver = webdriver.Chrome(PATH)

driver.get("https://trivia.fyi/random-trivia-questions/")
sleep(2)

while True:
    try:
        f = open(TRIVIA_PATH,"a")
        question = driver.find_element_by_xpath("/html/body/div/div/div/div/main/article/div/div[2]/div/div/div[1]/div/div/div/div/h2/a")
        answerbtn = driver.find_element_by_xpath("/html/body/div/div/div/div/main/article/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]")
        answerbtn.click()
        sleep(1)
        answer = driver.find_elements_by_xpath("//*[contains(@id,'post-')]")[1]
        post_id = answer.get_attribute("id")
        #answer = driver.find_element_by_xpath(f"//*[@id=\"{post_id}\"]/div/div/div[2]")
        answer = driver.find_element_by_xpath("//*[contains(@class,'su-spoiler-content su-u-clearfix su-u-trim')]")
        newQuestion = f"{question.text}:{answer.text}"
        print(newQuestion, file=f)
        print(newQuestion)
        f.close()
        next = driver.find_element_by_xpath("/html/body/div/div/div/div/main/article/div/div[2]/div/div/div[2]/h1/a")
        next.click()
        sleep(1)
    except Exception as e:
        print(str(e))
        sleep(100)
