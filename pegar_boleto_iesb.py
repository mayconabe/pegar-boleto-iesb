from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Inicializa o WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Abre a página desejada
driver.get('https://aluno.iesb.br/aluno/#/login')

matricula = input("Matricula: ")
senha = input("Senha: ")

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

# Verifica se há boletos. Se não houver, retorna uma mensagem de erro.
# try:


# Fecha o navegador
# driver.quit()