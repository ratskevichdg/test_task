# import unittest

# from time import sleep
# from selenium import webdriver


# class MetricConversionsOrgTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(
#             "third_task/chromedriver"
#         )
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(5)

#     def test_convert_cels_to_fahr_using_search(self):
#         """
#         Testing a temperature conversion throw userInput
#         on a Temperature Conversion page
#         """
#         driver = self.driver
#         driver.get("https://www.metric-conversions.org")
#         self.assertIn("Metric Conversion charts and calculators", driver.title)
#         driver.find_element_by_link_text("Temperature").click()
#         self.assertIn(
#             "Temperature conversion calculators for metric and imperial units",
#             driver.title,
#         )
#         driver.find_element_by_id("convertForm")
#         driver.find_element_by_id("queryFrom").send_keys("Celsius")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_id("queryTo").send_keys("Fahrenheit")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_class_name("argument").send_keys("42")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_link_text("Convert").click()
#         self.assertIn("Celsius to Fahrenheit conversion | °C to °F", driver.title)

#     def test_conver_cels_to_fahr_using_button(self):
#         """
#         Testing a temperature conversion throw popLinks
#          on a Temperature Conversion page
#         """
#         driver = self.driver
#         driver.get("https://www.metric-conversions.org")
#         self.assertIn("Metric Conversion charts and calculators", driver.title)
#         driver.find_element_by_link_text("Temperature").click()
#         self.assertIn(
#             "Temperature conversion calculators for metric and imperial units",
#             driver.title,
#         )
#         driver.find_element_by_link_text("Celsius to Fahrenheit").click()
#         self.assertIn("Celsius to Fahrenheit conversion | °C to °F", driver.title)
#         # page image before entering data
#         blank_page_picture = driver.page_source
#         driver.find_element_by_id("argumentConv").send_keys("42")
#         # page image after entering data
#         resulted_page_picture = driver.page_source
#         self.assertNotEqual(blank_page_picture, resulted_page_picture)

#     def test_conver_cels_to_fahr_from_right_menu(self):
#         """
#         Testing a temperature conversion throw
#         rightside panel
#         """
#         driver = self.driver
#         driver.get("https://www.metric-conversions.org")
#         self.assertIn("Metric Conversion charts and calculators", driver.title)
#         driver.find_element_by_link_text("Temperature").click()
#         self.assertIn(
#             "Temperature conversion calculators for metric and imperial units",
#             driver.title,
#         )
#         driver.find_element_by_link_text("Celsius").click()
#         self.assertIn(
#             "Celsius conversion calculators, tables and forumas",
#             driver.title,
#         )
#         driver.find_element_by_link_text("Celsius to Fahrenheit").click()
#         self.assertIn("Celsius to Fahrenheit conversion | °C to °F", driver.title)
#         # page image before entering data
#         blank_page_picture = driver.page_source
#         driver.find_element_by_id("argumentConv").send_keys("42")
#         # page image after entering data
#         resulted_page_picture = driver.page_source
#         self.assertNotEqual(blank_page_picture, resulted_page_picture)

#     def test_convert_cels_to_fahr_using_search_from_start_page(self):
#         """
#         Testing a temperature conversion throw search input
#         on main page
#         """
#         driver = self.driver
#         driver.get("https://www.metric-conversions.org")
#         self.assertIn("Metric Conversion charts and calculators", driver.title)
#         driver.find_element_by_id("queryFrom").send_keys("Celsius")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_id("queryTo").send_keys("Fahrenheit")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_xpath("//*[@id='results']/ol/li[1]/div/input").send_keys(
#             "42"
#         )
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_xpath("//*[@id='results']/ol/li[1]/div/a[2]").click()
#         self.assertIn("Celsius to Fahrenheit conversion | °C to °F", driver.title)

#     def test_meters_to_feet_using_searh(self):
#         """
#         Testing a lenght conversion throw userInput
#         on a Lenght Conversion page
#         """
#         driver = self.driver
#         driver.get("https://www.metric-conversions.org")
#         self.assertIn("Metric Conversion charts and calculators", driver.title)
#         driver.find_element_by_link_text("Length").click()
#         self.assertIn("Length conversion", driver.title)
#         driver.find_element_by_id("convertForm")
#         driver.find_element_by_id("queryFrom").send_keys("Meters")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_id("queryTo").send_keys("Feet")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_class_name("argument").send_keys("42")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         # page image before entering data
#         blank_page_picture = driver.page_source
#         driver.find_element_by_link_text("Convert").click()
#         self.assertIn("Meters to Feet - m to ft conversion", driver.title)
#         # page image after entering data
#         resulted_page_picture = driver.page_source
#         self.assertNotEqual(blank_page_picture, resulted_page_picture)

#     def test_conver_meters_to_feet_using_button(self):
#         """
#         Testing a lenght conversion throw popLinks
#         on a Lenght Conversion page
#         """
#         driver = self.driver
#         driver.get("https://www.metric-conversions.org")
#         self.assertIn("Metric Conversion charts and calculators", driver.title)
#         driver.find_element_by_link_text("Length").click()
#         self.assertIn("Length conversion", driver.title)
#         driver.find_element_by_link_text("Meters to Feet").click()
#         self.assertIn("Meters to Feet - m to ft conversion", driver.title)
#         # page image before entering data
#         blank_page_picture = driver.page_source
#         driver.find_element_by_id("argumentConv").send_keys("42")
#         # page image after entering data
#         resulted_page_picture = driver.page_source
#         self.assertNotEqual(blank_page_picture, resulted_page_picture)

#     def test_conver_meters_to_feet_from_right_menu(self):
#         """
#         Testing a lenght conversion throw
#         rightside panel
#         """
#         driver = self.driver
#         driver.get("https://www.metric-conversions.org")
#         self.assertIn("Metric Conversion charts and calculators", driver.title)
#         driver.find_element_by_link_text("Length").click()
#         self.assertIn("Length conversion", driver.title)
#         driver.find_element_by_link_text("Meters").click()
#         self.assertIn("Meters conversion calculators, tables and forumas", driver.title)
#         driver.find_element_by_link_text("Meters to Feet").click()
#         self.assertIn("Meters to Feet - m to ft conversion", driver.title)
#         # page image before entering data
#         blank_page_picture = driver.page_source
#         driver.find_element_by_id("argumentConv").send_keys("42")
#         # page image after entering data
#         resulted_page_picture = driver.page_source
#         self.assertNotEqual(blank_page_picture, resulted_page_picture)

#     def test_convert_meters_to_feet_using_search_from_start_page(self):
#         """
#         Testing a lenght conversion throw search input
#         on main page
#         """
#         driver = self.driver
#         driver.get("https://www.metric-conversions.org")
#         self.assertIn("Metric Conversion charts and calculators", driver.title)
#         driver.find_element_by_id("queryFrom").send_keys("Meters")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_id("queryTo").send_keys("Feet")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_xpath("//*[@id='results']/ol/li[1]/div/input").send_keys(
#             "42"
#         )
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_xpath("//*[@id='results']/ol/li[1]/div/a[2]").click()
#         self.assertIn("Meters to Feet - m to ft conversion", driver.title)

#     def test_convert_ounces_to_grams_using_search(self):
#         """
#         Testing a weight conversion throw userInput
#         on a Weight Conversion page
#         """
#         driver = self.driver
#         driver.get("https://www.metric-conversions.org")
#         self.assertIn("Metric Conversion charts and calculators", driver.title)
#         driver.find_element_by_link_text("Weight").click()
#         self.assertIn(
#             "Weight conversion calculators for imperial and metric units",
#             driver.title,
#         )
#         driver.find_element_by_id("convertForm")
#         driver.find_element_by_id("queryFrom").send_keys("Ounces")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_id("queryTo").send_keys("Grams")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_class_name("argument").send_keys("42")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         # page image before entering data
#         blank_page_picture = driver.page_source
#         driver.find_element_by_link_text("Convert").click()
#         self.assertIn("Ounces to Grams - oz to g conversion", driver.title)
#         # page image after entering data
#         resulted_page_picture = driver.page_source
#         self.assertNotEqual(blank_page_picture, resulted_page_picture)

#     def test_conver_ounces_to_grams_using_button(self):
#         """
#         Testing a weight conversion throw popLinks
#         on a Weight Conversion page
#         """
#         driver = self.driver
#         driver.get("https://www.metric-conversions.org")
#         self.assertIn("Metric Conversion charts and calculators", driver.title)
#         driver.find_element_by_link_text("Weight").click()
#         self.assertIn(
#             "Weight conversion calculators for imperial and metric units",
#             driver.title,
#         )
#         driver.find_element_by_link_text("Ounces to Grams").click()
#         self.assertIn("Ounces to Grams - oz to g conversion", driver.title)
#         # page image before entering data
#         blank_page_picture = driver.page_source
#         driver.find_element_by_id("argumentConv").send_keys("42")
#         # page image after entering data
#         resulted_page_picture = driver.page_source
#         self.assertNotEqual(blank_page_picture, resulted_page_picture)

#     def test_conver_ounces_to_grams_from_right_menu(self):
#         """
#         Testing a weight conversion throw
#         rightside panel
#         """
#         driver = self.driver
#         driver.get("https://www.metric-conversions.org")
#         self.assertIn("Metric Conversion charts and calculators", driver.title)
#         driver.find_element_by_link_text("Weight").click()
#         self.assertIn(
#             "Weight conversion calculators for imperial and metric units",
#             driver.title,
#         )
#         driver.find_element_by_link_text("Ounces").click()
#         self.assertIn("Ounces conversion calculators, tables and forumas", driver.title)
#         driver.find_element_by_link_text("Ounces to Grams").click()
#         self.assertIn("Ounces to Grams - oz to g conversion", driver.title)
#         # page image before entering data
#         blank_page_picture = driver.page_source
#         driver.find_element_by_id("argumentConv").send_keys("42")
#         # page image after entering data
#         resulted_page_picture = driver.page_source
#         self.assertNotEqual(blank_page_picture, resulted_page_picture)

#     def test_convert_ounces_to_grams_using_search_from_start_page(self):
#         """
#         Testing a weight conversion throw search input
#         on main page
#         """
#         driver = self.driver
#         driver.get("https://www.metric-conversions.org")
#         self.assertIn("Metric Conversion charts and calculators", driver.title)
#         driver.find_element_by_id("queryFrom").send_keys("Ounces")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_id("queryTo").send_keys("Grams")
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_xpath("//*[@id='results']/ol/li[1]/div/input").send_keys(
#             "42"
#         )
#         # Use sleep to fill the form correctly
#         # otherwise the two fields will not fill in together
#         sleep(1)
#         driver.find_element_by_xpath("//*[@id='results']/ol/li[1]/div/a[2]").click()
#         self.assertIn("Ounces to Grams - oz to g conversion", driver.title)

#     def tearDown(self):
#         self.driver.close()


# if __name__ == "__main__":
#     unittest.main()
