#Importando o módulo PYTES
import pytest

#Importando WebBrowser (navegador de internet) e open_new_tab (abrir uma nova guia)
from webbrowser import open_new_tab

#Criar uma função DEF e informar o site que deve ser aberto
def abrir_um_site():
    open_new_tab ("https://sp.senai.br/unidade/mogidascruzes/")

for i in range(5):
    pytest.main(abrir_um_site())