import pyautogui
import time
import pandas

# ============================================================================
# CONFIGURAÇÕES INICIAIS
# ============================================================================

# URL do sistema de cadastro de produtos
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Define um intervalo padrão entre as ações do PyAutoGUI
pyautogui.PAUSE = 0.5

# ============================================================================
# ETAPA 1 - ACESSAR O SISTEMA
# ============================================================================

# Abre o navegador Google Chrome e acessa o sistema
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('enter')

# Aguarda o carregamento da página
time.sleep(3)

# ============================================================================
# ETAPA 2 - REALIZAR LOGIN
# ============================================================================

# Preenche as credenciais de acesso e entra no sistema
pyautogui.press('tab')
pyautogui.write('pythonautomation@gmail.com')

pyautogui.press('tab')
pyautogui.write('123456')

pyautogui.press('enter')

# Aguarda o carregamento da área interna do sistema
time.sleep(3)

# ============================================================================
# ETAPA 3 - IMPORTAR BASE DE DADOS
# ============================================================================

# Carrega a planilha CSV contendo os produtos a serem cadastrados
tabela = pandas.read_csv('produtos.csv')

# ============================================================================
# ETAPA 4 - CADASTRO AUTOMÁTICO DOS PRODUTOS
# ============================================================================

# Percorre todas as linhas da planilha
for linha in tabela.index:

    # Posiciona o cursor no primeiro campo do formulário
    pyautogui.click(x=951, y=326)

    # ------------------------------------------------------------------------
    # Coleta e preenche os dados do produto
    # ------------------------------------------------------------------------

    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    # Campo observação (preenchido apenas quando existir informação)
    obs = str(tabela.loc[linha, 'obs'])

    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press('tab')

    # Envia o formulário para cadastrar o produto
    pyautogui.press('enter')

    # Retorna ao topo da página para o próximo cadastro
    pyautogui.scroll(3000)

