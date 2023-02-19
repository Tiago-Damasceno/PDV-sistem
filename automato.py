from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pyautogui


serviço = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = serviço)
print name
navegador.get('https://www.conquistandosuavaga.com/pre-inscricao')
navegador.find_elements('xpath', '//*[@id="mauticform_input_99formulariopesquisaaposc10_eu_sou_o_pedro_marins_e_v"]')

