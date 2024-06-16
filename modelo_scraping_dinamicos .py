from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import subprocess
import time

# Configura as opções para o Chrome
chrome_options = Options()

# Definindo o user agent específico
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('--window-size=1920,1080')  # Tamanho da janela maior
chrome_options.add_argument('--headless')

# Inicializa o WebDriver do Selenium com as opções configuradas
driver = webdriver.Chrome(options=chrome_options)

try:
    # Abre a página desejada
    driver.get('https://www.imdb.com/chart/top/?ref=nv_mv_250')
    
    # Aguarda um tempo antes rolar a página para garantir que todos os elementos carreguem
    time.sleep(2)  

    # Simula a rolagem da página até o final
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Aguarda um tempo depois rolar a página para garantir que todos os elementos carreguem
    time.sleep(2)  

    dados = []

    # Tempo de espera para elementos dinâmicos
    elementos_lista_filmes = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.sc-b189961a-0.hBZnfJ.cli-children'))
    )

    # Itera sobre cada elemento para obter os dados formatados
    for elemento in elementos_lista_filmes:
        # Cria um dicionário com os dados formatados
        filme = {
            'Posição': linhas[0].split('.')[0].strip(),
            'Filme': linhas[0].split('.')[1].strip(),
            'Ano': linhas[1],
            'Duração': linhas[2],
            'Classificação': linhas[3],
            'Pontuação': linhas[4].replace(',', '.').strip(),
            'Quantidade de votos': linhas[5].strip()[1:-1],
        }

        # Adiciona o dicionário à lista de dados
        dados.append(filme)

except Exception as e:
    print(f"Erro: {e}")

finally:
    # Fecha o navegador ao terminar, mesmo em caso de exceção
    driver.quit()

    # Exporta os dados para um arquivo JSON
    with open('dados_filmes_imdb.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

    print('Dados exportados para dados_filmes_imdb.json')

    # Comando para encerrar todos os processos que você deseja após a exportação do JSON
    comando = 'taskkill /F /IM "python.exe"'
    subprocess.run(comando, shell=True)