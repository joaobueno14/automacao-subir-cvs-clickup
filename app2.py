from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import openpyxl
import clipboard
import pyautogui

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

tabela = pd.read_excel("basedecandidatos.xlsx")

for I, nome in enumerate (tabela['nome']):
    local = tabela.loc[I, 'local']
    celular = tabela.loc[I, 'celular']
    email = tabela.loc[I, 'email']
    linkedin = tabela.loc[I, 'linkedin']
    salario = tabela.loc[I, 'salario']
    comosoubedavaga = tabela.loc[I, 'comosoubedavaga']  


    link = ('COLE AQUI SEU LINK DE FORMULARIO')


    # Abrir forms 
    navegador.get(link)
    sleep(5)
    
    # Preencher o nome
    navegador.find_element('xpath','/html/body/app-root/cu-form/div/div/div[5]/div[1]/input').send_keys(nome)
    
    # Preencher local 
    navegador.find_element('xpath','/html/body/app-root/cu-form/div/div/div[5]/div[2]/div[2]/cu-location-input/div/div/input').send_keys(local)
    sleep(2)

    navegador.find_element('xpath','//*[@id="cdk-overlay-0"]/cdk-virtual-scroll-viewport/div[1]/cu-location-autocomplete-option').click()
    

    # Preencher número
    navegador.find_element('xpath','/html/body/app-root/cu-form/div/div/div[5]/div[3]/div[2]/div/cu-telephone-input/div/input').send_keys(str(celular))
    
    navegador.find_element('xpath','/html/body/app-root/cu-form/div/div/div[5]/div[3]/div[2]/div/cu-telephone-input/div/cu-select/div/div/div[1]/span').click()
    
    navegador.find_element('xpath','/html/body/app-root/cu-form/div/div/div[5]/div[3]/div[2]/div/cu-telephone-input/div/cu-select/div/div[2]/div/cu-select-option[1]/div').click()
    sleep(1)
    # Preencher email
    navegador.find_element('xpath','/html/body/app-root/cu-form/div/div/div[5]/div[4]/div[2]/input').send_keys(email)
    

    # Preencher Valor
    navegador.find_element('xpath','/html/body/app-root/cu-form/div/div/div[5]/div[5]/div[2]/input').send_keys(str(salario))
    
    
    # Preencher linkedin
    navegador.find_element('xpath','/html/body/app-root/cu-form/div/div/div[5]/div[6]/div[2]/input').send_keys(linkedin)
    

    # Preencher como soube da vaga
    navegador.find_element('xpath','/html/body/app-root/cu-form/div/div/div[5]/div[7]/div[2]/input').send_keys(comosoubedavaga)
    
    # Clicar na caixa
    navegador.find_element('xpath','/html/body/app-root/cu-form/div/div/div[5]/div[8]/div/cu-checkbox/div').click()
    
    # Clicar no botão de anexo 
    navegador.find_element('xpath','/html/body/app-root/cu-form/div/div/div[5]/div[9]/div[2]/button').click()
    sleep(1)

    # Atomação de achar o PDF usando o pyautogui

    pyautogui.click(809,87,)
    sleep(1)

    clipboard.copy(nome)
   
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')

    pyautogui.keyUp('v')
    pyautogui.keyUp('ctrl')
    

    pyautogui.click(932,81,duration=1)

    pyautogui.click(516,195,duration=1)

    pyautogui.click(764,563,duration=1)

    sleep(3)
    

    # Clicar no botão de enviar
    navegador.find_element('xpath','/html/body/app-root/cu-form/div/div/button').click()
    sleep(10)


