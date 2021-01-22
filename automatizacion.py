from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json

driver = webdriver.Firefox(executable_path="geckodriver.exe")

with open("list.json") as json_file:
    data = json.load(json_file)

    for p in data["login"]: 
        print(p["name"] + " iniciara sesion")

        driver.get("https://todoist.com/users/showlogin")

        time.sleep(3)

        mail = driver.find_element_by_id("data[email]")
        mail.send_keys(p["name"])

        passw = driver.find_element_by_id("data[password]")
        passw.send_keys(p["pwd"])

        loginBtn = driver.find_elements_by_class_name("data[ist_button]")

        for x in data["articulos"]:
            loginBtn = driver.find_elements_by_class_name("data[plus_add_button]")

            tarea = driver.find_element_by_class_name("data[DraftEditor-editorContainer]")
            tarea.send_keys(p["name"])

            AddBtn = driver.find_element_by_class_name("data[ist_button]")

driver.close()