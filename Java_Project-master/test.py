from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def compare_prices(product_name):
    # Initialize Chrome WebDriver
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(options=options)

    # Open Amazon
    driver.get("https://www.amazon.in/")
    time.sleep(2)  # Wait for the page to load

    # Search for the product on Amazon
    search_box_amazon = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box_amazon.send_keys(product_name)
    search_box_amazon.submit()
    time.sleep(2)  # Wait for search results to load

    # Get the price from Amazon
    try:
        for i in range(3, 9):
            price_amazon_element = driver.find_element(By.XPATH, f"/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{i}]")
            price_amazon = price_amazon_element.text
            print(price_amazon)
    except:
        price_amazon = "Price not found on Amazon"

    # Open Flipkart
    driver.get("https://www.flipkart.com/")
    time.sleep(2)  # Wait for the page to load

    # Close login popup if present
    try:
        close_login_popup = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")
        close_login_popup.click()
    except:
        pass

    # Search for the product on Flipkart
    search_box_flipkart = driver.find_element(By.XPATH, "//input[@title='Search for products, brands and more']")
    search_box_flipkart.send_keys(product_name)
    search_box_flipkart.submit()
    time.sleep(2)  # Wait for search results to load

    # Get the price from Flipkart
    try:
        price_flipkart_element = driver.find_element(By.XPATH, "//div[@class='_30jeq3']")
        price_flipkart = price_flipkart_element.text
    except:
        price_flipkart = "Price not found on Flipkart"

    # Close the browser window
    driver.quit()

    return {"Amazon": price_amazon, "Flipkart": price_flipkart}

# Example usage
product_name = "iPhone 12"
prices = compare_prices(product_name)
print("Prices for", product_name, ":\nAmazon:", prices["Amazon"], "\nFlipkart:", prices["Flipkart"])
