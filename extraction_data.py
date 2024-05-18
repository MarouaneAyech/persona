
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# URL de la page d'authentification
url_page = 'http://polytechserver.cloudapp.net/gest-scol/inscription/logform-user.php'

# Identifiants de connexion
login = 'marouane'
mot_de_passe = 'm0a6r8o3'

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options) 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get(url_page)

wait = WebDriverWait(driver, 10)
# Localiser les champs de texte de login et de mot de passe
login_field = wait.until(EC.visibility_of_element_located((By.ID, 'log')))
password_field =  wait.until(EC.visibility_of_element_located((By.ID, 'pas')))

# Saisir le login et le mot de passe
login_field.send_keys(login)
password_field.send_keys(mot_de_passe)

# Localiser et cliquer sur le bouton de connexion
login_button =  wait.until(EC.visibility_of_element_located((By.NAME, 'btn')))
login_button.click()

# Ajoutez un délai si nécessaire pour observer le résultat
driver.implicitly_wait(5)

driver.quit()
