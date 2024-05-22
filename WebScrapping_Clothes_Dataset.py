import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By 

from pathlib import Path
from PIL import Image
import hashlib
import io
import requests
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

def get_content_from_url(url):
    options = ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    page_content = driver.page_source
    driver.quit()
    return page_content


def parse_image_urls(content, classes, location, source):
    soup = BeautifulSoup(content, "html.parser")
    results = []
    for a in soup.findAll(attrs={"class": classes}):
        name = a.find('img')
        if name is not None:
            source_value = name.get(source)
            if source_value is not None:
                results.append(source_value)
    return results


def save_urls_to_csv(image_urls):
    df = pd.DataFrame({"links": image_urls})
    df.to_csv("links.csv", index=False, encoding="utf-8")


def get_and_save_image_to_file(image_url, output_dir, target_size=(600, 720)):
    image_content = requests.get(image_url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file).convert("RGB")

    image = image.resize(target_size, Image.LANCZOS)
    
    filename = hashlib.sha1(image_content).hexdigest()[:10] + ".png"
    file_path = output_dir / filename
    image.save(file_path, "PNG", quality=80)


# def main():
    
#     options = ChromeOptions()
#     options.add_argument("--headless=new")
#     driver = webdriver.Chrome(options=options)
     
#     url = "https://www.trendyol.com/"
#     driver.get(url)
#     sleep(10)
   
#     # Sayfa içeriğini al
#     content = driver.page_source
    
 
#     image_urls = parse_image_urls(
#         content=content, classes="carousel-item", location="img", source="src")
#     save_urls_to_csv(image_urls)

#     output_dir = Path("C:/Users/kubra/OneDrive/Masaüstü/Web Scrapping/ButtonImage")
    
#     for image_url in image_urls:
#         get_and_save_image_to_file(image_url, output_dir=output_dir)
    
#     image_urls = parse_image_urls(
#                 content=content, classes="image-container", location="img", source="src")
        
#     for image_url in image_urls:
#             get_and_save_image_to_file(image_url, output_dir=output_dir)

#     driver.quit()  # WebDriver örneğini kapat

#     print("Tamamlandı!")


# if _name_ == "_main_":
#     main()



def main():
    
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    
    # driver.maximize_window()  # Full  scene
    url = "https://www.trendyol.com/en/trendyol-collection/mint-midi-knitwear-basic-striped-dress-twoaw23el00018-p-646025633"
    # driver.get(url)
    # sleep(20)
    

    # input =driver.find_element(By.CLASS_NAME,"activeGender")
    # input.click()
    # # nextButton=driver.find_element(By.CLASS_NAME,"icon-forward-button")
    # # nextButton.click()
    # sleep(10)
    
    
    # print(f"Input:{input}")
    
    # while True:
    #     continue
    
    # content = get_content_from_url(url)
    
   
    content = driver.page_source
    # Create WebDriver instance

    image_urls = parse_image_urls(
        content=content, classes="carousel-item", location="img", source="src")
    save_urls_to_csv(image_urls)

    output_dir = Path("C:/Users/KUBRA/Desktop/NewImages")
    
    for image_url in image_urls:
        get_and_save_image_to_file(image_url, output_dir=output_dir)
    



    driver.quit()  # WebDriver örneğini kapat
    print("Done!")


if __name__== "__main__":
    main()
    
    
    
    # Navigate through the slider
    # Navigate through the slider
    # for _ in range(6):  # Sliderda 6 defa ileri git
    #     try:
    #         next_button = WebDriverWait(driver, 10).until(
    #             EC.visibility_of_element_located((By.CSS_SELECTOR, '.navigation.next'))
    #         )   
    #         next_button.click()
    #     except NoSuchElementException:
    #         print("Sonraki düğme bulunamadı")
    #         # Element bulunamazsa sayfa içeriğini yeniden alın
    #         content = driver.page_source
    #         image_urls = parse_image_urls(
    #             content=content, classes="carousel-item", location="img", source="src")
            
    #         for image_url in image_urls:
    #             get_and_save_image_to_file(image_url, output_dir=output_dir)
    
    

    # for _ in range(6):
    #     try:
    #         #              button = driver.find_element_by_class_name("slide-out-btn")
            
    #         # # clicking on the button
    #         # button.click()
    #         next_button = driver.find_element_by_class_name( "navigation.next")
    #         next_button.click()
    #     except NoSuchElementException:
    #         print("Sonraki düğme bulunamadi")
    #         content = driver.page_source
    #         image_urls = parse_image_urls(
    #             content=content, classes="carousel-item", location="img", source="src")
        
    #         for image_url in image_urls:
    #             get_and_save_image_to_file(image_url, output_dir=output_dir)

    # driver.quit()  # Quit WebDriver instance