import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Set up Selenium WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the page
driver.get("https://app.cloudqa.io/home/AutomationPracticeForm")

# Find and fill the Name field
name_input = driver.find_element(By.XPATH, '//*[@id="fname"]')
name_input.send_keys("John")

sname_input = driver.find_element(By.XPATH, '//*[@id="lname"]')
sname_input.send_keys("Doe")

#Find and fill the DOB field
dob_input =driver.find_element(By.XPATH, '//*[@id="dob"]')
dob_input.send_keys("2001-01-03")

# Find and select an option from the Gender dropdown
gender_radio = driver.find_element(By.XPATH, '//*[@id="male"]')
gender_radio.click()

# Find and fill the Mobile field
sname_input = driver.find_element(By.XPATH, '//*[@id="mobile"]')
sname_input.send_keys("785412369")

# Find and fill the Email field
email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
email_input.send_keys("johndoe@example.com")

# Find and fill the Country field
email_input = driver.find_element(By.XPATH, '//*[@id="country"]')
email_input.send_keys("INDIA")

#Select state from dropdowm State
# Find the dropdown element
dropdown = driver.find_element(By.ID, "state")
select = Select(dropdown)
select.select_by_value("India") #selection by value

#FInd and fill the hobbie field
hobbie_chk= driver.find_element(By.XPATH, '//*[@id="Dance"]')
hobbie_chk.click()

#FInd and fill the about yourself field
about=driver.find_element(By.XPATH, '//*[@id="automationtestform"]/div[1]/div[11]/textarea')
about.send_keys("lorem ipsum ")

# Agee and click on checkbox
chk_box=driver.find_element(By.XPATH, '//*[@id="Agree"]') 
chk_box.click()

# Submit the form
submit_button = driver.find_element(By.XPATH, '//*[@id="automationtestform"]/div[4]/button[1]')
submit_button.click()


#!!!!!!!!!!!!!!!!!!!!!! For  IRAME without ID !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

iframe_src = "/Home/IFrame"  # Replace with the actual src value
iframe_element = driver.find_element(By.CSS_SELECTOR, f'iframe[src="{iframe_src}"]')

driver.switch_to.frame(iframe_element)

name_iframe = driver.find_element(By.XPATH, '//*[@id="fname"]')
name_iframe.send_keys("Ronit")

lname_iframe = driver.find_element(By.XPATH, '//*[@id="lname"]')
lname_iframe.send_keys("Sharma")

#Find and fill the DOB field
dob_input =driver.find_element(By.XPATH, '//*[@id="dob"]')
dob_input.send_keys("2001-01-03")

# Find and select an option from the Gender dropdown
gender_radio = driver.find_element(By.XPATH, '//*[@id="male"]')
gender_radio.click()

# Find and fill the Mobile field
sname_input = driver.find_element(By.XPATH, '//*[@id="mobile"]')
sname_input.send_keys("785412369")

# Find and fill the Email field
email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
email_input.send_keys("johndoe@example.com")

# Find and fill the Country field
email_input = driver.find_element(By.XPATH, '//*[@id="country"]')
email_input.send_keys("INDIA")

#Select state from dropdowm State
# Find the dropdown element
dropdown = driver.find_element(By.ID, "state")
select = Select(dropdown)
select.select_by_value("India") #selection by value

#FInd and fill the hobbie field
hobbie_chk= driver.find_element(By.XPATH, '//*[@id="Dance"]')
hobbie_chk.click()

# Find and fill the about yourself section
about=driver.find_element(By.XPATH, '//*[@id="automationtestform"]/div[1]/div[11]/textarea')
about.send_keys("lorem ipsum ")
# Agee and click on checkbox
chk_box=driver.find_element(By.XPATH, '//*[@id="Agree"]') 
chk_box.click()

# Submit the form
submit_button = driver.find_element(By.XPATH, '//*[@id="automationtestform"]/div[4]/button[1]')
submit_button.click()

driver.switch_to.default_content()


#!!!!!!!!!!!!!!!!!!!!!! For  IRAME without ID !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

iframe_src = "/Home/InnerNestedIFrame"  # Replace with the actual src value
iframe_element = driver.find_element(By.CSS_SELECTOR, f'iframe[src="{iframe_src}"]')

driver.switch_to.frame(iframe_element)

name_iframe = driver.find_element(By.XPATH, '//*[@id="fname"]')
name_iframe.send_keys("Mohit")

lname_iframe = driver.find_element(By.XPATH, '//*[@id="lname"]')
lname_iframe.send_keys("Gupta")

#Find and fill the DOB field
dob_input =driver.find_element(By.XPATH, '//*[@id="dob"]')
dob_input.send_keys("2001-01-25")

# Find and select an option from the Gender dropdown
gender_radio = driver.find_element(By.XPATH, '//*[@id="female"]')
gender_radio.click()

# Find and fill the Mobile field
sname_input = driver.find_element(By.XPATH, '//*[@id="mobile"]')
sname_input.send_keys("7452412369")

# Find and fill the Email field
email_input = driver.find_element(By.XPATH, '//*[@id="email"]')
email_input.send_keys("james@example.com")

# Find and fill the Country field
email_input = driver.find_element(By.XPATH, '//*[@id="country"]')
email_input.send_keys("INDIA")

#Select state from dropdowm State
# Find the dropdown element
dropdown = driver.find_element(By.ID, "state")
select = Select(dropdown)
select.select_by_value("India") #selection by value

#FInd and fill the hobbie field
hobbie_chk= driver.find_element(By.XPATH, '//*[@id="Dance"]')
hobbie_chk.click()

#FInd and fill the about yourself field
about=driver.find_element(By.XPATH, '//*[@id="automationtestform"]/div[1]/div[11]/textarea')
about.send_keys("lorem ipsum ")

# Agee and click on checkbox
chk_box=driver.find_element(By.XPATH, '//*[@id="Agree"]') 
chk_box.click()

# Submit the form
submit_button = driver.find_element(By.XPATH, '//*[@id="automationtestform"]/div[4]/button[1]')
submit_button.click()

driver.switch_to.default_content()

# Close the browser
driver.quit()
