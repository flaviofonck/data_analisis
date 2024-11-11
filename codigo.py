from selenium import webdriver
from selenium.webdriver.common.by import By

def get_dropdown_options(driver, xpath_expression):
    # Locate the dropdown element using the provided XPath
    dropdown_element = driver.find_element(By.XPATH, xpath_expression)

    # Extract all the option elements within the dropdown
    options = dropdown_element.find_elements(By.TAG_NAME, "option")

    # Create a list of dictionaries containing the value and text of each option
    dropdown_options = []
    for option in options:
        value = option.get_attribute("value")
        text = option.text
        dropdown_options.append({'value': value, 'text': text})

    return dropdown_options

# Example usage
if __name__ == "__main__":
    # Initialize the WebDriver (e.g., ChromeDriver)
    driver = webdriver.Chrome()

    # Navigate to the webpage
    driver.get("https://www.example.com/page-with-dropdown")

    # Define the XPath expression for the dropdown
    xpath_expression = "//select[@id='dropdown-id']"

    # Get the dropdown options
    options = get_dropdown_options(driver, xpath_expression)

    # Print the options
    for option in options:
        print(f"Value: {option['value']}, Text: {option['text']}")

    # Close the WebDriver
    driver.quit()
