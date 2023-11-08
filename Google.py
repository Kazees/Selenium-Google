from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#PATH=r'C:\Users\kazee\Desktop\Python\Crawler\chromedriver.exe'

class Principal(webdriver.Chrome):
    def __int__(self):
        options=webdriver.ChromeOptions().add_experimental_option     \
            ('excludeSwitches', ['enable-logging'])
        service=Service(ChromeDriverManager().install())
        super(Principal,self).__init__(service=service,options=options)

    def abrir(self):
        self.maximize_window()
        self.get('https://www.google.com')

    def pesquisar(self):
        self.abrir()

        busca=self.find_element(By.NAME,'q')
        #busca=self.find_element(By.ID, 'APjFqb')
        #busca=self.find_element(By.XPATH, '//*[@id="APjFqb"]')
        #busca=self.find_element(By.CSS_SELECTOR, 'textarea[title="Pesquisar"]')

        busca.send_keys('Power rangers')
        busca.submit()

        #print('Título da página é:',self.title)
        #print('URL é:',self.current_url)

        time.sleep(4)

    def loginGoogle(self):
        self.abrir()

        butao=self.find_element(By.XPATH,'//*[@id="gb"]/div/div[2]/a')
        butao.click()

        time.sleep(0.5)

        login=self.find_element(By.NAME,'identifier')
        login.send_keys('seu gmail')
        butao = self.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
        butao.click()

        time.sleep(1)

        senha = self.find_element(By.NAME, 'password')
        senha.send_keys('sua senha')
        butao = self.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
        butao.click()

        time.sleep(5)

    def executar_script(self):
        self.abrir()

        self.execute_script("alert('Mudando de página')")
        time.sleep(2)

        self.switch_to.alert.accept()
        self.execute_script("window.open('https://www.youtube.com.br','new tab')")

        time.sleep(5)

    def trocar_pagina(self):
        self.abrir()

        self.execute_script("window.open()")
        self.switch_to.window(self.window_handles[1]) #Trocando de página
        self.get('https://www.youtube.com')

        time.sleep(0.5)

        self.execute_script("window.open()")
        self.switch_to.window(self.window_handles[2])
        self.get('https://www.shopinfo.com.br')

        time.sleep(0.5)

        self.switch_to.window(self.window_handles[1]) #Voltando para pág do Youtube
        time.sleep(1)

        self.switch_to.window(self.window_handles[0]) #Voltando para primeira página
        time.sleep(2)

    def trocar_janela(self):
        self.maximize_window()
        self.get('https://jqueryui.com/dialog/#modal-form')

        iframe=self.find_element(By.XPATH,'//*[@id="content"]/iframe')
        self.switch_to.frame(iframe)

        botao=self.find_element(By.ID,'create-user')
        botao.click()

        nome=self.find_element(By.ID,'name')
        nome.clear()
        nome.send_keys('Teste')

        gmail = self.find_element(By.ID, 'email')
        gmail.clear()
        gmail.send_keys('Teste@gmail.com')

        senha = self.find_element(By.ID, 'password')
        senha.clear()
        senha.send_keys('Teste12345')

        criar_conta=self.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/button[1]')
        #cancelar=self.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/button[2]')

        time.sleep(3)
        criar_conta.click()
        time.sleep(3)

    def atualizar_pagina(self):
        self.abrir()
        tempo=int(5)

        while True:
            time.sleep(tempo)
            self.refresh()

    def rolar_pagina(self):
        self.abrir()
        self.execute_script("alert('Mudando de página')")
        time.sleep(1)

        self.switch_to.alert.accept()
        self.execute_script("window.open()")
        self.switch_to.window(self.window_handles[1])
        self.get('https://pt.wikipedia.org')

        time.sleep(1.5)

        self.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

    def redimensionar(self):
        self.maximize_window()
        self.get('https://jqueryui.com/resizable/')

        iframe = self.find_element(By.XPATH, '//*[@id="content"]/iframe')
        self.switch_to.frame(iframe)

        canto=self.find_element(By.XPATH,'//*[@id="resizable"]/div[3]')
        acao=ActionChains(self) #redimensionar
        acao.drag_and_drop_by_offset(canto,150,75).perform()
        time.sleep(3)

    def segurar_arrastrar(self):
        self.maximize_window()
        self.get('https://jqueryui.com/droppable/')

        iframe = self.find_element(By.XPATH, '//*[@id="content"]/iframe')
        self.switch_to.frame(iframe)

        segurar=self.find_element(By.XPATH,'//*[@id="draggable"]')
        soltar=self.find_element(By.XPATH,'//*[@id="droppable"]')

        acao=ActionChains(self) #segurar e soltar o objeto no local desejado
        acao.drag_and_drop(segurar,soltar).perform()
        time.sleep(3)

    def loginGuru(self):
        self.abrir()

        self.execute_script("alert('Mudando de página')")
        time.sleep(1)

        self.switch_to.alert.accept()
        self.execute_script("window.open()")
        self.switch_to.window(self.window_handles[1])  #Trocando de página
        self.get('https://www.demo.guru99.com/test/newtours/')

        time.sleep(1)

        usuario = self.find_element(By.NAME, 'userName').send_keys('mercury')
        senha = self.find_element(By.NAME, 'password').send_keys('mercury')
        submit = self.find_element(By.NAME, 'submit').click()

        time.sleep(3)

if __name__=='__main__':
    bot=Principal()
    #bot.login() Google diz que a conexão não é segura para fazer o login
    #bot.loginGuru()
    #bot.trocar_janela()
    #bot.atualizar_pagina()
    #bot.rolar_pagina()
    #bot.redimensionar()
    bot.segurar_arrastrar()