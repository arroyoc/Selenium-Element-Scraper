from selenium import webdriver


output_id = "id = "

user_url = raw_input("URL: " + " ")
driver = webdriver.PhantomJS()
driver.get(user_url)

id_elements = driver.find_elements_by_xpath("//*[@id]")

for eachElement in id_elements:
    individual_ids = eachElement.get_attribute("id")
    print(output_id + individual_ids)


