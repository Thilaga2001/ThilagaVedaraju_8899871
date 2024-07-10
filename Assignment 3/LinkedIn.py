from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Log in to LinkedIn
driver.get('https://www.linkedin.com/login')
time.sleep(2)
email_field = driver.find_element(By.ID, 'username')
email_field.send_keys('jekos10812@furnato.com')
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys('thilaga123')
login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
login_button.click()
time.sleep(15)

driver.maximize_window()

# Search for people
search_bar = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
search_bar.send_keys('Data Scientist')
search_bar.send_keys(Keys.RETURN)
time.sleep(5)
assert "results for" in driver.page_source, "Search results not loaded"

save_button = driver.find_element(By.XPATH, '(//span[@class="artdeco-button__text"][normalize-space()="Save"])[1]')
save_button.click()
time.sleep(2)
save_button2= driver.find_element(By.XPATH, '(//span[@class="artdeco-button__text"][normalize-space()="Save"])[1]')
save_button2.click()
save_button3= driver.find_element(By.XPATH, '(//span[@class="artdeco-button__text"][normalize-space()="Save"])[1]')
save_button3.click()


# Navigate to the network page
network_tab = driver.find_element(By.XPATH, '//span[@title="My Network"]')
network_tab.click()
time.sleep(5)
assert "My Network" in driver.page_source, "Network tab not found or not clicked"


manage_mynetwork = driver.find_element(By.XPATH, "//span[@aria-label='Show more in manage my network list']//*[name()='svg']")
manage_mynetwork.click()

connection_button = driver.find_element(By.XPATH,"//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//section[1]//div[1]//div[2]//a[1]//div[1]//div[1]")
connection_button.click()
time.sleep(5)
# Send message
message_button = driver.find_element(By.XPATH,  "//span[normalize-space()='Message']")
message_button.click()
time.sleep(5)
assert "message" in driver.page_source, "Message window not opened"

send_message = driver.find_element(By.XPATH, "//div[@aria-label='Write a message…']//p")
send_message.click()
send_message.send_keys("It's great connecting with you. How have you been?")

send_button = driver.find_element(By.XPATH, "//*[name()='use' and contains(@href,'#send-priv')]")
send_button.click()
time.sleep(5)

assert "Sent" in driver.page_source, "Message not sent successfully"

close_message = driver.find_element(By.XPATH, "//*[name()='use' and contains(@href,'#close-sma')]")
close_message.click()
time.sleep(5)

# Create a new post
# Click the "Start a post" button
home_button=driver.find_element(By.XPATH,"//span[@title='Home']")
home_button.click()
time.sleep(10)
start_post_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'truncate block text-align-left')]")))
start_post_button.click()

# Wait for the post modal to appear
post_modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.ql-editor")))

# Enter the post content
post_content = "Looking for the job position - Automation Tester."
time.sleep(5)
post_modal.send_keys(post_content)

time.sleep(5)

# Close the driver
driver.quit()