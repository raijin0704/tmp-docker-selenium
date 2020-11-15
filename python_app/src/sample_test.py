import os
from datetime import datetime

from selenium import webdriver


def setup_driver():
    driver = webdriver.Remote(
            command_executor="http://chrome:4444/wd/hub",
            options=webdriver.ChromeOptions(),
        )

    return driver


def test():
    driver = setup_driver()
    
    file_name = datetime.now().strftime("%y%m%d_%H%M%S.png")
    screenshot_path = os.path.join("/work/screenshots/", file_name)
    driver.get("https://www.google.com/")
    driver.get_screenshot_as_file(screenshot_path)
    driver.quit()



if __name__ == "__main__":
    test()