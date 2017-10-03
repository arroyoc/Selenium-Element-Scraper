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


# Browser of choice.. Use whichever webdriver you have available. Example: "webdriver.PhantomJS()", "webdriver.Chrome()"
driver = webdriver.PhantomJS()
driver.get(user_url)

# Using selenium to find elements by xpath.
id_elements = driver.find_elements_by_xpath("//*[@id]")
name_elements = driver.find_elements_by_xpath("//*[@name]")

# The following choice will print all id elements
if user_element_type == "id":
    for eachElement in id_elements:
        individual_ids = eachElement.get_attribute("id")
        print(output_id + individual_ids)

# The following choice will print all name elements
elif user_element_type == "name":
    for eachElement in name_elements:
        individual_ids = eachElement.get_attribute("name")
        print(output_name + individual_ids)

# The following choice will print all of the options
elif user_element_type == "all":
    for eachElement in id_elements:
        individual_ids = eachElement.get_attribute("id")
        print(output_id + individual_ids)
    for eachElement in name_elements:
        individual_ids = eachElement.get_attribute("name")
        print(output_name + individual_ids)

else:
    print("Invalid element type...")
