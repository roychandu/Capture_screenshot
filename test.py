import os
import django
from django.core.mail import EmailMessage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

def fill_form(driver):
    wait = WebDriverWait(driver, 60)
    
    name_field = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    name_field.send_keys("Chandan Roy")
    
    contact_field = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    contact_field.send_keys("8869846824")
    
    email_field = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    email_field.send_keys("cr717753@gmail.com")
    
    address_field = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')))
    address_field.send_keys("Bharam Puri, Haridwar, Uttarakhand")
    
    pin_code_field = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    pin_code_field.send_keys("249401")
    
    dob_field = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')))
    dob_field.send_keys("24/02/2001")
    
    gender_field = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    gender_field.send_keys("Male")
    
    code_field = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    code_field.send_keys("GNFPYC")
    
    submit_btn = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
    submit_btn.click()
    
    time.sleep(2)

def capture_screenshot(driver, filepath):
    driver.save_screenshot(filepath)

def send_email(subject, body, from_email, to_email, attachment):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Capture_screenshot.settings')
    django.setup()
    
    email = EmailMessage(
        subject,
        body,
        from_email,
        [to_email],
    )
    email.attach_file(attachment)
    email.send(fail_silently=False)

def main():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://forms.gle/WT68aV5UnPajeoSc8")
        fill_form(driver)
        screenshot_path = 'confirmation_page_screenshot.png'
        capture_screenshot(driver, screenshot_path)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
    
    send_email(
        'Subject here',
        'Python (Selenium) Assignment - [Chandan Roy]',
        'roys242001@gmail.com',
        'cr717753@gmail.com',
        screenshot_path
    )

if __name__ == "__main__":
    main()
