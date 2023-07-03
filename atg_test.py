from selenium import webdriver

# Set up the web driver
driver = webdriver.Chrome()

try:
    # Open the atg.world website
    driver.get("https://atg.world")

    # Check if the website loaded successfully
    assert "atg.world" in driver.title
    print("Website loaded successfully. Test Passed!")

except Exception as e:
    print(f"Website failed to load. Test Failed! Error: {e}")

finally:
    # Close the web driver
    driver.quit()
