from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from termcolor import colored
import time
import subprocess


download_directory="/home/nkosindu/Documents/goojara-movie-downloader"
def setup():
    # Set up the ChromeDriver service
    service = Service(executable_path="chromedriver")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def search_for_movies(driver, movie_name):
    # Open the target URL
    driver.get("https://www.goojara.to/")

    # Wait until the input element is present and interact with it
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'putin'))
    )
    input_element.clear()
    input_element.send_keys(movie_name.strip(), Keys.RETURN)

    # Wait for the search results to load and be visible
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'im'))
    )

    # Click on the first search result
    search_results.click()

def get_movie_first_link(driver):
    iframe = WebDriverWait(driver, 30).until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, 'iframe[src*="wootly.ch"]'))
    )

    print("Successfully shifted to the iframe.")

    # Find and click the play button
    play_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'play-button'))
    )
    print("Successfully found the button ")
    driver.execute_script("arguments[0].scrollIntoView(true);", play_button)
    play_button.click()

    # Wait for the new tab to open and switch to it
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    original_window = driver.window_handles[0]
    new_window = [
        window for window in driver.window_handles if window != original_window][0]
    driver.switch_to.window(new_window)
    print("Successfully switched to the new tab.")

    # Close the new tab
    driver.close()
    print("Closed the new tab and switched back to the original tab.")

    # Wait for a short delay to ensure the new tab is closed before switching back
    time.sleep(2)

    # Switch back to the original tab
    driver.switch_to.window(original_window)
    print("Successfully switched back to the original tab.")
    # Find the div containing the iframe
    iframe_div = driver.find_element(By.ID, "vidcon")

    # Find the iframe element inside the div
    iframe_element = iframe_div.find_element(By.TAG_NAME, "iframe")

    # Get the value of the src attribute
    movie_link = iframe_element.get_attribute("src")

    print("Link to the movie:", movie_link)

    driver.get(movie_link)

def get_movie_second_link(driver):
    # Find the div element with the class "vid-holder"
    vid_holder_div = driver.find_element(By.CLASS_NAME, "vid-holder")
    print("Video holder found !!!!!")

    play_button2 = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'play-button'))
    )
    # Find the video element inside the div
    play_button2.click()
    print('A second play button clicked succesfully!!!')
    time.sleep(2)
    # download_link = driver.find_element_by_id('arwel')
   
    # Switch back to the original window
    driver.switch_to.window(driver.window_handles[0])

    time.sleep(30)

    container = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'dld'))
    )
    print("Container found !!!!!")

    # Find the download link within the container
    download_link = container.find_element(By.TAG_NAME, 'a')
    print("A tag found")

    # Get the value of the 'href' attribute of the download link
    download_url = download_link.get_attribute('href')
    subprocess.run(['curl', '-OJL', download_url],cwd=download_directory)

   
def run_downloader(driver, movie_name):
    try:
        # Open the target URL
        print(colored("Downloader: Browser succesfully opened ,Please wait while movie gets downloaded",
                      color="green", attrs=["bold"]))
        driver.get("https://www.goojara.to/")
        search_for_movies(driver, movie_name)
        driver.refresh()
        time.sleep(5)

        get_movie_first_link(driver)
        get_movie_second_link(driver)
        # time.sleep(1000)

    except Exception as e:
        print(f"An error occurred: Goojara took long to respond or the downloader failed to fetch movie!!")
        print(e)

    finally:
        # Quit the driver
        driver.quit()

if __name__ == "__main__":
    movie_name = input('Enter the name of the movie here: ')
    driver = setup()    
    run_downloader(driver, movie_name)
