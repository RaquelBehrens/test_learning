import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class SeleniumTest(unittest.TestCase):

    # IMPLICIT FIXTURE SETUP
    def setUp(self):

        # modo headless, pra não abrir o chrome toda vez
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # self.driver = webdriver.Chrome(options=chrome_options)

        self.driver = webdriver.Chrome()
        self.driver.get("https://duckduckgo.com")

    
    # 1. Somar dois números diferentes e verificar o resultado
    def test_create_easter_2024_date(self):      
        # Implicit Fixture Setup
        
        # Exercise SUT
        sum_result = self.calculate(self.driver, "3 + 5")
        assert sum_result == "8", f"Expected 8 but got {sum_result}"
        
        # Fixture Teardown
        self.driver.quit()

    # 2. Somar dois números diferentes e em seguida dividir o resultado por 10 e verificar o resultado
    def test_create_beggining_of_year_2024_datetime(self):
        # Implicit Fixture Setup

        # Exercise SUT
        calculate_result = self.calculate(self.driver, "3 + 5")
        result_divided = self.calculate_after_search(self.driver, f"/10")

        # Result Verification
        assert result_divided == "0.8", f"Expected 0.8 but got {result_divided}"

    # 3. Fazer duas operações diferentes e verificar o resultado da última operação
    def test_sum_30_days_with_timedelta(self):
        # Implicit Fixture Setup

        # Exercise SUT
        first_op = self.calculate(self.driver, "7 - 2")
        second_op = self.calculate_after_search(self.driver, "10 * 2")

        # Result Verifications
        assert second_op == "20", f"Expected 20 but got {second_op}"

        # Fixture Teardown
        self.driver.quit()

    # 4. Fazer três operações diferentes e verificar que as três operações aparecem no histórico
    def test_four(self):
        # Implicit Fixture Setup

        # Exercise SUT
        first_history = self.calculate(self.driver, "1 + 2")
        second_history = self.calculate_after_search(self.driver, "3 + 4")
        third_history = self.calculate_after_search(self.driver, "5 + 6")
        
        # Histórico
        history_element = self.driver.find_element("css selector", ".tile__history")
        past_calculations = history_element.find_elements("css selector", ".tile__past-calc")
        expected_history = [
            ("5 + 6", "11"),
            ("3 + 4", "7"),
            ("1 + 2", "3"),
        ]

        # Result Verifications
        for i, calculation in enumerate(past_calculations):
            formula = calculation.find_element("css selector", ".tile__past-formula").text
            result = calculation.find_element("css selector", ".tile__past-result").text
            assert (formula, result) == expected_history[i], f"Unexpected history at index {i+1}"

        # Fixture Teardown
        self.driver.quit()


    def calculate(self, driver, expression):
        # Input
        search_box = driver.find_element("id", "searchbox_input")
        search_box.clear()
        search_box.send_keys(expression)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        # Elemento que mostra o resultado
        result = driver.find_element("id", "display")
        return result.text


    def calculate_after_search(self, driver, expression):
        # Interaje nos botões da calculadora
        time.sleep(1)
        for char in expression.replace(' ', ''):
            if char.isdigit() or char in '+-()=':
                button = driver.find_element("xpath", f"//button[@value='{char}']")
                button.click()
                time.sleep(0.3)
            elif char == '/':
                button = driver.find_element("xpath", "//button[@value='÷']")
                button.click()
                time.sleep(0.3)
            elif char == '*':
                button = driver.find_element("xpath", "//button[@value='×']")
                button.click()
                time.sleep(0.3)
        button_equal = driver.find_element("xpath", "//button[@value='=']")
        button_equal.click()
        time.sleep(2)
        # Resultado
        result = driver.find_element("id", "display")
        return result.text

if __name__ == '__main__':
    unittest.main()
