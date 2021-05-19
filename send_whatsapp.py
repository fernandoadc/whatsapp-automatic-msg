from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import urllib
import pandas as pd


navegador = webdriver.Chrome(ChromeDriverManager().install())
navegador.get("https://web.whatsapp.com/")

contatos_df = pd.read_excel("Enviar.xlsx")

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

# já estamos com o login feito no whatsapp web
for i, pessoa in enumerate(contatos_df['Pessoa']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    print(pessoa)
    print(numero)
    mensagem = 'Boa tarde! \nComo você está?  \nSou o Fernando, bolsista do projeto "Impactos psicossociais da pandemia: construindo um observatório de saúde mental com enfoque nos discentes e docentes da pós-graduação", venho informá-los do nosso próximo encontro com os alunos dos programas de doutorado! \nO projeto visa fomentar as ações de atenção ao público dos programas de Pós-graduação da Ufopa, com a parceria entre o Núcleo de Psicologia/Proges e a Pró-Reitoria de Pesquisa, Pós-graduação e Inovação Tecnológica (Proppit) no âmbito do Programa de Ações Emergenciais – PAEM, uma das ações do projeto é realizar o Círculo Acolhedor com as/os estudantes da pós-graduação. \nAcontecerá agora dia 20/05/21 das 14h:30min. Link da inscrição: https://tinyurl.com/3yh9ybbk  \n\n O Projeto Círculo Acolhedor é uma iniciativa do Núcleo de Psicologia (NUPSI) da PROGES/UFOPA, através da qual são realizadas semanalmente ações de psicologia em grupo (terapêuticas ou psicoeducativas), possibilitando a abordagem de temáticas pertinentes aos participantes, a partilha de saberes, o acolhimento, a integração, o fortalecimento das relações interpessoais e vínculos afetivos, a empatia e escuta respeitosa do outro, com vistas a tornar o grupo um espaço de crescimento pessoal e coletivo contribuindo para a construção de uma cultura de paz e bem viver na Universidade. Contamos com sua participação!😉 Abaixo, destacamos algumas orientações iniciais importantes para que possamos aproveitar da melhor forma o nosso encontro: ᴪ Procure um lugar tranquilo para acessar, que você tenha privacidade sem o trânsito de pessoas; ᴪ Verifique se o uso do fone de ouvido pode otimizar a comunicação, às vezes ajuda e às vezes nem tanto 😅; ᴪ Quando você não estiver com a palavra, desligue seu microfone (no celular é só clicar na tela e tocar no ícone do microfone) para evitar ruídos externos e estabilizar a nossa conexão; ᴪ Estaremos compartilhando nossas percepções, vivências, sentimentos e angústias, é um momento muito especial para todas/os, por isso é importante manter uma atitude empática, de escuta e também respeitar a privacidade das pessoas. Guarde sigilo do que será tratado no grupo. ᴪ Esse é um grupo de acolhimento e de presença, por isso, caso seja possível ligue sua câmera, caso não possa, se comunique pelo chat ☺ Vamos juntas/os construir um espaço seguro de acolhimento e cuidado no contexto acadêmico!'
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone=55{numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)