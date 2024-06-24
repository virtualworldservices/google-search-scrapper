from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Load URLs from the CSV file
urls = pd.read_csv('import.csv')['links'].tolist()

websites = []

for url in urls:
    driver.get(url)
    time.sleep(5)  # Consider using WebDriverWait for better handling of dynamic loading

    try:
        website_element = driver.find_element(By.XPATH, '//span/a[@jsname="UWckNb"]')
        website = website_element.get_attribute("href")
    except Exception as e:
        website = None
    websites.append(website)

    # Print the websites
    print("website")
    for website in websites:
        print(website)

# Create a DataFrame
data = {'Website': websites}
df = pd.DataFrame(data)

# Export to CSV
df.to_csv('output.csv', index=False)

# Close the driver
driver.quit()
