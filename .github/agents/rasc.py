# OBJETIVO: automatizar digitação de texto em outra aplicação
# PASSO 1: identificar biblioteca adequada
# PASSO 2: pensar em como controlar tempo e foco da janela
import pyautogui as py

import time
# PASSO 3: escrever o código
py.press('win')  # abre o menu iniciar
py.write('bloco de notas')  # digita "bloco de notas"

py.press('enter')  # abre o bloco de notas

time.sleep(5)  # tempo para o usuário focar a janela correta
texto = "Olá, esta é uma mensagem automática enviada pelo meu agente RASC."

py.write(texto, interval=0.05)  # digita o texto com intervalo entre as teclas
py.press('enter')  # envia a mensagem pressionando Enter
# PASSO 4: testar e ajustar conforme necessário
py.write("Teste concluído com sucesso!", interval=0.05)
py.press('ctrl+s')  # envia a mensagem pressionando Enter
# qual o próximo passo? 
py.write("C:\\Users\\wiill\\Desktop\\mensagem_automatica.txt")  # caminho do arquivo
py.press('enter')  # confirma o salvamento   
time.sleep(1)
py.press('enter')  # confirma a substituição do arquivo, se necessário
py.write("Agente RASC finalizou a tarefa.")
py.press('enter')  # envia a mensagem pressionando Enter
py.hotkey('alt', 'f4')  # fecha o bloco de notas
py.press('n')  # não salvar as alterações se perguntadoA
# PASSO 5: documentar o código para futuras referências
# Este script automatiza a abertura do Bloco de Notas, digita uma mensagem automática,
# salva o arquivo na área de trabalho e fecha o aplicativo. Ajuste os tempos de espera
# conforme necessário para o desempenho do seu sistema.
# Bibliotecas usadas: pyautogui para automação de teclado e mouse, time para controle de tempo.

#pq meu cogo nao aplica qual o erro?
#pyautogui.click = cllica
#pyautogui.write = escreva um texto