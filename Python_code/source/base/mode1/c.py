from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_extraction_code_from_baidu(url):
  """从百度网盘网页获取提取码"""
  driver = webdriver.Chrome()  # 使用 Chrome 浏览器
  driver.get(url)
  try:
    # 等待提取码元素出现
    extraction_code_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "share_password"))
    )
    extraction_code = extraction_code_element.get_attribute("value")
    return extraction_code
  finally:
    driver.quit()

if __name__ == "__main__":
  url = input("https://pan.baidu.com/s/1NWVUs5nDZqLWzV5xaPiBNA")
  extraction_code = get_extraction_code_from_baidu(url)
  if extraction_code:
    print(f"提取码：{extraction_code}")
  else:
    print("未找到提取码")