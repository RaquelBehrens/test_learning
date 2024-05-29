from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def calculate(expression):
    # Input
    search_box = driver.find_element("id", "searchbox_input")
    search_box.clear()
    search_box.send_keys(expression)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    # Elemento que mostra o resultado
    result = driver.find_element("id", "display")
    return result.text

def calculate_after_search(expression):
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

try:
    # 1. Somar dois números diferentes e verificar o resultado
    driver.get("https://duckduckgo.com")
    sum_result = calculate("3 + 5")
    assert sum_result == "8", f"Expected 8 but got {sum_result}"
    print(f"Sum result: {sum_result}")

    # 2. Somar dois números diferentes e em seguida dividir o resultado por 10 e verificar o resultado
    driver.get("https://duckduckgo.com")
    calculate_result = calculate("3 + 5")
    result_divided = calculate_after_search(f"/10")
    assert result_divided == "0.8", f"Expected 0.8 but got {result_divided}"
    print(f"Result after division: {result_divided}")

    # 3. Fazer duas operações diferentes e verificar o resultado da última operação
    driver.get("https://duckduckgo.com")
    first_op = calculate("7 - 2")
    second_op = calculate_after_search("10 * 2")
    assert second_op == "20", f"Expected 20 but got {second_op}"
    print(f"Second operation result: {second_op}")

    # 4. Fazer três operações diferentes e verificar que as três operações aparecem no histórico
    driver.get("https://duckduckgo.com")
    first_history = calculate("1 + 2")
    second_history = calculate_after_search("3 + 4")
    third_history = calculate_after_search("5 + 6")
    
    # Histórico
    history_element = driver.find_element("css selector", ".tile__history")
    past_calculations = history_element.find_elements("css selector", ".tile__past-calc")
    expected_history = [
        ("5 + 6", "11"),
        ("3 + 4", "7"),
        ("1 + 2", "3"),
    ]

    for i, calculation in enumerate(past_calculations):
        formula = calculation.find_element("css selector", ".tile__past-formula").text
        result = calculation.find_element("css selector", ".tile__past-result").text
        assert (formula, result) == expected_history[i], f"Unexpected history at index {i+1}"

    print("History contains all three operations.")

finally:
    driver.quit()
