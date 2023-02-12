Automação feita em Python com o objetivo de preencher informações de candidatos a partir de uma planilha excel em um formulário da ferramenta de gestão ClickUp.

Pacotes do Python usados:

pandas
openpyxl
clipboard
pyautogui
sleep
webdriver
selenium

Como usar:

Por se tratar da primeira versão até aqui, o código não está compilado, então você precisara instalar o Python 64bits e também os pacotes citados a cima.

01 - Salve uma planilha com o nome: "basedecandidatos.xlsx" .

02 - Cole seu link de formulário dentro da variavel 'link'.

Essa automação não é de uso exclusivo do ClickUp, ou seja, você pode adaptar para google forms ou outro, basta trocar o link e mudar os xpath de cada campo que você queira preencher ou simplesmente "clicar", você também pode mudar a estrutura dos dados enviados na planilha, mas será necessário alterar as infos na estrutura da planilha e também do nosso loop 'FOR'.
