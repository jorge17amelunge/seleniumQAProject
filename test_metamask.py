import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import pyperclip
from dotenv import load_dotenv

def run_selenium_test():
    """
    Runs a sample Selenium test and generates a report file.
    """
    # Create the reports directory if it doesn't exist
    if not os.path.exists('reports'):
        os.makedirs('reports')

    load_dotenv()

    print("Starting Selenium test...")
    EXTENSION_PATH = 'chrome/NKBIHFBEOGAEAOEHLEFNKODBEFGPGKNN_13_2_0_0.crx'

    service = Service(ChromeDriverManager().install())
    opt = webdriver.ChromeOptions()
    opt.add_extension(EXTENSION_PATH)

   

    driver = webdriver.Chrome(service=service, options=opt)
    try:
        # Navigate to a website

      


        driver.get("https://www.sushi.com")
        print(f"Navigated to: {driver.title}")

        # Wait for the page to load
        time.sleep(1)

        # Example: Find and click the "Launch App" button on Uniswap homepage
        try:

            original_tab_handle = driver.current_window_handle

            div_element_accept_cookies = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept all cookies')]")
            div_element_accept_cookies.click()
            print("Clicked 'Accept all cookies' button.")
            time.sleep(2)

            button_connect_wallet = driver.find_element(By.CSS_SELECTOR, "[testdata-id='connect-button']")
            button_connect_wallet.click()
            print("Clicked 'Connect Wallet' button.")
            time.sleep(2)

            div_element_choose_metamask = driver.find_element(By.XPATH, "//div[contains(text(), 'MetaMask')]")
            div_element_choose_metamask.click()
            print("Clicked 'Launch App' button.")
            time.sleep(3)

            div_element_choose_metamask = driver.find_element(By.XPATH, "//div[contains(text(), 'OBTENER')]")
            div_element_choose_metamask.click()
            time.sleep(3)

            div_element_choose_metamask = driver.find_element(By.XPATH, "//div[contains(text(), 'Añadir a Chrome')]")
            div_element_choose_metamask.click()
            time.sleep(5)

            all_window_handles = driver.window_handles
            print("Number of tabs: " + str(all_window_handles))
            chrome_handle = [handle for handle in all_window_handles if handle != original_tab_handle][0]
            driver.switch_to.window(chrome_handle)

            div_element_choose_metamask = driver.find_element(By.XPATH, "//span[contains(text(), 'Agregar a Chrome')]")
            div_element_choose_metamask.click()
            time.sleep(1)

            pyautogui.click(730, 790)

            time.sleep(1)
            # Switch back to the original tab
            driver.switch_to.window(original_tab_handle)        
            print("Switched back to the original tab.")
           

            div_element_choose_metamask = driver.find_element(By.XPATH, "//div[contains(text(), 'Actualizar')]")
            div_element_choose_metamask.click()
            time.sleep(10)

            
            

            all_window_handles = driver.window_handles
            print("Number of tabs: " + str(all_window_handles))
            chrome_handle = [handle for handle in all_window_handles if handle != original_tab_handle][0]
            driver.switch_to.window(chrome_handle)

            
            driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")
            time.sleep(2)

            driver.find_element(By.XPATH, "//button[contains(text(), 'Get started')]").click()
            
            driver.find_element(By.CSS_SELECTOR, "[data-testid='terms-of-use-scroll-button']").click()
            driver.find_element(By.CSS_SELECTOR, "[data-testid='terms-of-use-checkbox']").click()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "[data-testid='terms-of-use-agree-button']").click()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "[data-testid='onboarding-import-wallet']").click()
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, "[data-testid='onboarding-import-with-srp-button']").click()

            
            mnemonic = os.getenv("MM_SEED")
            pyperclip.copy(mnemonic)

            driver.find_element(By.CSS_SELECTOR, "[data-testid='srp-input-import__paste-button']").click()
            time.sleep(1)

            pyautogui.click(370, 260)

            driver.find_element(By.CSS_SELECTOR, "[data-testid='import-srp-confirm']").click()
            time.sleep(2)
            
            print("Copy the password to the clipboard.")
            password = os.getenv("MM_PASSWORD")

            all_window_handles = driver.window_handles
            print("Number of tabs: " + str(all_window_handles))
            chrome_handle2 = [handle for handle in all_window_handles if handle != original_tab_handle][0]
            driver.switch_to.window(chrome_handle2)
            
            print("Paste the Password.")
            input_element_pass = driver.find_element(By.CSS_SELECTOR, "[data-testid='create-password-new-input']")
            input_element_pass.clear()
            input_element_pass.send_keys(password)

            print("Paste the Confirmation Password.")

            #input_element_confirm_pass = driver.find_element(By.CSS_SELECTOR, "[data-testid='create-password-confirm-input']")
            input_element_confirm_pass = driver.find_element(By.ID, "create-password-new") 
            input_element_confirm_pass.clear()
            input_element_confirm_pass.send_keys(password)

            print("Create Password.")

           
            driver.find_element(By.CSS_SELECTOR, "[data-testid='create-password-terms']").click()
            


        except Exception as e:
            print(f"Could not find or click the button: {e}")

        # Capture a screenshot
        # screenshot_path = os.path.join('reports', 'screenshot_1.png')
        # driver.save_screenshot(screenshot_path)
        # print(f"Captured screenshot: {screenshot_path}")

        # Write a sample log file
        log_path = os.path.join('reports', 'log_output.txt')
        with open(log_path, 'w') as f:
            f.write("Test started at: " + time.ctime() + "\n")
            f.write("Successfully navigated to Google.\n")
            f.write("Test finished.\n")
        print(f"Wrote log file: {log_path}")

    finally:
        # driver.quit()
        print("End.")
        time.sleep(10003)

if __name__ == "__main__":
    run_selenium_test()