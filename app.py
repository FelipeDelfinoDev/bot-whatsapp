import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

webbrowser.open("https://web.whatsapp.com/")
sleep(20)
pyautogui.hotkey("ctrl", "w")
sleep(2)
workbook = openpyxl.load_workbook("botnumeros.xlsx")
pagina = workbook["Planilha1"]

for linha in pagina.iter_rows(min_row=1):
  nome = linha[0].value
  telefone = linha[1].value

  if not nome or not telefone:
    continue
  
  mensagem = f'Olá {nome}, mensagem automatica'

  try:
    link_mensagem = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
    webbrowser.open(link_mensagem)
    sleep(10)
    pyautogui.press("enter")
    sleep(7)
    pyautogui.hotkey("ctrl", "w")
    sleep(7)
  except Exception as e:
    print (f'não foi possivel enviar mensagem para {nome}: {e}')
    with open('erros.csv','a', newline='',encoding='utf-8') as arquivo:
      arquivo.write(f' {nome} , {telefone} \n')
