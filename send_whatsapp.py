from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import urllib
import pandas as pd


navegador = webdriver.Chrome(ChromeDriverManager().install())
navegador.get("https://web.whatsapp.com/")

contatos_df = pd.read_excel("Lista-de-contatos-a-serem-enviados.xlsx")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

# já estamos com o login feito no whatsapp web
for i, pessoa in enumerate(contatos_df['Pessoa']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    print(pessoa)
    print(numero)
    mensagem = 'Boa tarde! \nComo você está?'
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone=55{numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)
