from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json

driver = webdriver.Firefox(executable_path="geckodriver.exe")

with open("list.json") as json_file:
    data = json.load(json_file)

    for p in data["login"]: 
        print(p["name"] + " iniciara sesion")

        driver.get("https://todoist.com/")

        time.sleep(3)

        redBtn = driver.find_element_by_class_name("_2q_cf")
        redBtn.click()

        mail = driver.find_element_by_id("email")
        mail.send_keys(p["name"])

        passw = driver.find_element_by_id("password")
        passw.send_keys(p["pwd"])

        loginBtn = driver.find_element_by_class_name("ist_button")
        loginBtn.click()

        for x in data["articulos"]:
            loginBtn = driver.find_element_by_class_name("plus_add_button")

            tarea = driver.find_element_by_class_name("DraftEditor-editorContainer")
            tarea.send_keys(p["name"])

            addBtn = driver.find_element_by_class_name("dataist_button")
            addBtn.click()

driver.close()