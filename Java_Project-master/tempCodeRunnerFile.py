from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def compare_prices(product_name):
    # Initialize Chrome WebDriver
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(options=options)

    try:
        # Open Amazon
        driver.get("https://www.amazon.in/")
        time.sleep(2)

        # Search for the product
        search_box_amazon = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box_amazon.send_keys(product_name)
        search_box_amazon.submit()
        time.sleep(2)

        # Get the product name and price from Amazon
        try:
            product_name_amazon = driver.find_element(By.XPATH, "//span[contains(@class, 'a-size-medium')]").text
            price_amazon = driver.find_element(By.XPATH, "//span[@class='a-price-whole']").text
        except:
            product_name_amazon = "Product not found on Amazon"
            price_amazon = "Price not found on Amazon"

        # Open Flipkart
        driver.get("https://www.flipkart.com/")
        time.sleep(2)

        # Close login popup if present
        try:
            close_login_popup = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")
            close_login_popup.click()
        except:
            pass

        # Search for the product
        search_box_flipkart = driver.find_element(By.XPATH, "//input[@title='Search for products, brands and more']")
        search_box_flipkart.send_keys(product_name)
        search_box_flipkart.submit()
        time.sleep(2)

        # Get the product name and price from Flipkart
        try:
            product_name_flipkart = driver.find_element(By.XPATH, "//span[contains(@class, 'B_NuCI')]").text
            price_flipkart = driver.find_element(By.XPATH, "//div[@class='_30jeq3 _1_WHN1']").text
        except:
            product_name_flipkart = "Product not found on Flipkart"
            price_flipkart = "Price not found on Flipkart"

    finally:
        # Close the browser window
        driver.quit()

    return product_name_amazon, price_amazon, product_name_flipkart, price_flipkart

# Example usage
product_name = "iPhone 13"
product_name_amazon, price_amazon, product_name_flipkart, price_flipkart = compare_prices(product_name)
print("Amazon Product Name:", product_name_amazon)
print("Amazon Price:", price_amazon)
print("Flipkart Product Name:", product_name_flipkart)
print("Flipkart Price:", price_flipkart)
