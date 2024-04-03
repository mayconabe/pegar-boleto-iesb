from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializa o WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('headless')
options.add_argument('log-level=3')
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080, driver.window_handles[0])

# Abre a página desejada
driver.get('https://aluno.iesb.br/aluno/#/login')

# matricula = input("Matricula: ")
# senha = input("Senha: ")
matricula = ""
senha = ""

# Encontra os elementos de Login(Username e Password)
username = driver.find_element(By.XPATH, "/html/body/ion-nav-view/div/div/div[2]/div/form/div/label[1]/input")
password = driver.find_element(By.XPATH, "/html/body/ion-nav-view/div/div/div[2]/div/form/div/label[2]/input")

# Envia os dados para o elemento de entrada
username.send_keys(matricula)
password.send_keys(senha)

# Loga no site
driver.find_element(By.XPATH,"/html/body/ion-nav-view/div/div/div[2]/div/form/div/button").click()

# Aperta no botão "Financeiro"
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/ion-nav-view/ion-side-menus/div/ion-side-menu/menu-left/ion-content/div[1]/ion-list/div/div[4]/div/ion-item[6]/a[1]"))).click()

# Aperta no botão "Boletos"
driver.find_element(By.XPATH,"/html/body/ion-nav-view/ion-side-menus/div/ion-side-menu/menu-left/ion-content/div[1]/ion-list/div/div[4]/div/ion-item[6]/div[2]/a").click()
time.sleep(35)
# Verifica se há boletos. Se não houver, retorna uma mensagem de erro.

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/ion-nav-view/ion-side-menus/div/ion-side-menu-content/ion-nav-view/ion-view/ion-content/div[1]/div/boleto-deck/div/div/div[2]/boleto-detail/div/div/div/a[2]"))).click()

time.sleep(2)

if driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/ion-modal-view/ion-content/div/div[1]/p").text == "Carregando código de barras" or driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/ion-modal-view/ion-content/div/div[1]/p").text == "loading bar code":
    time.sleep(10)
    boleto = driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/ion-modal-view/ion-content/div/div[1]/p").text
    print(boleto)
else:
    boleto = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div[2]/ion-modal-view/ion-content/div/div[1]/p"))).text
    print(boleto)


# Fecha o navegador
driver.quit()