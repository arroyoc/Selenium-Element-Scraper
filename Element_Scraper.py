from selenium import webdriver
from help_text import *


output_id = "id = "
output_name = "name = "

print(url_help_text)
user_url = raw_input("URL: " + " ")
print(element_type_help_text)
user_element_type = raw_input("Element Type: ")

user_url = user_url.lower()
user_element_type = user_element_type.lower()


driver = webdriver.PhantomJS()
driver.get(user_url)

id_elements = driver.find_elements_by_xpath("//*[@id]")
name_elements = driver.find_elements_by_xpath("//*[@name]")

if user_element_type == "id":

    for eachElement in id_elements:
        individual_ids = eachElement.get_attribute("id")
        print(output_id + individual_ids)


elif user_element_type == "name":
    for eachElement in name_elements:
        individual_ids = eachElement.get_attribute("name")
        print(output_name + individual_ids)

else:
    print("Invalid element type...")
