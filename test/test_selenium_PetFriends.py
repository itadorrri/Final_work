from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_show_all_pets():
   pytest.driver.find_element_by_id('email').send_keys('abc@mail.ru')
   pytest.driver.find_element_by_id('pass').send_keys('1234gg5')
   pytest.driver.implicitly_wait(10)
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

   images = pytest.driver.find_elements_by_xpath('//img[@class="card-img-top"]')
   names = pytest.driver.find_elements_by_xpath('//h5[@class="card-title"]')
   descriptions = pytest.driver.find_elements_by_xpath('//p[@class="card-text"]')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0




def test_show_my_pets():
   pytest.driver.find_element_by_id('email').send_keys('abc@mail.ru')
   pytest.driver.find_element_by_id('pass').send_keys('1234gg5')
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   wait = WebDriverWait(pytest.driver, 5)
   assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME,'h1'), "PetFriends"))

   pytest.driver.find_element_by_css_selector('a[href="/my_pets"]').click()
   assert wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), "All"))

   css_locator = 'tbody>tr'
   data_my_pets = pytest.driver.find_elements_by_css_selector(css_locator)

   for i in range(len(data_my_pets)):
      assert wait.until(EC.visibility_of(data_my_pets[i]))

   image_my_pets = pytest.driver.find_elements_by_css_selector('img[style="max-width: 100px; max-height: 100px;"]')
   for i in range(len(image_my_pets)):
      if image_my_pets[i].get_attribute('src') != '':
         assert wait.until(EC.visibility_of(image_my_pets[i]))

   name_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[1]')
   for i in range(len(name_my_pets)):
      assert wait.until(EC.visibility_of(name_my_pets[i]))
   type_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[2]')
   for i in range(len(type_my_pets)):
      assert wait.until(EC.visibility_of(type_my_pets[i]))

   age_my_pets = pytest.driver.find_elements_by_xpath('//tbody/tr/td[3]')
   for i in range(len(age_my_pets)):
      assert wait.until(EC.visibility_of(age_my_pets[i]))

   all_statistics = pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text.split("\n")
   statistics_pets = all_statistics[1].split(" ")
   all_my_pets = int(statistics_pets[-1])
   assert len(data_my_pets) == all_my_pets

   m = 0
   for i in range(len(image_my_pets)):
      if image_my_pets[i].get_attribute('src') != '':
         m += 1
   assert m >= all_my_pets/2

   for i in range(len(name_my_pets)):
      assert name_my_pets[i].text != ''

   for i in range(len(type_my_pets)):
      assert type_my_pets[i].text != ''

   for i in range(len(age_my_pets)):
      assert age_my_pets[i].text != ''

   list_name_my_pets = []
   for i in range(len(name_my_pets)):
      list_name_my_pets.append(name_my_pets[i].text)
   set_name_my_pets = set(list_name_my_pets)
   assert len(list_name_my_pets) == len(set_name_my_pets)

   list_data_my_pets = []
   for i in range(len(data_my_pets)):
      list_data = data_my_pets[i].text.split("\n")
      list_data_my_pets.append(list_data[0])
   set_data_my_pets = set(list_data_my_pets)
   assert len(list_data_my_pets) == len(set_data_my_pets)