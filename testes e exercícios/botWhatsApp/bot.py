from selenium import webdriver
import time

class WhatsBot:
    def __init__(self):
        # Define a mensagem que vai ser enviada
        self.mensagem = []
        # Escolha das conversas que vai ser enviada a mensagem
        self.conversas = "Nai Baitolinha"
        # Transformando em objeto e configurando

        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        # aqui vai pegar as conversas que queremos
        conversa = self.driver.find_element_by_xpath(f"//span[@title='{self.conversas}']")
        time.sleep(3)
        conversa.click()

    def LerMensagem(self):
        Ultmsg = self.driver.find_elements_by_class_name("_1Gy50")
        time.sleep(5)
        pos = len(Ultmsg) - 1
        texto = Ultmsg[pos].find_element_by_css_selector("span.selectable-text").text
        time.sleep(5)
        return texto
    
    def EnviarMsg(self, texto):
        # <span dir="auto" title="Nai Baitolinha" class="_ccCW FqYAR i0jNr">Nai Baitolinha</span>
        # <div tabindex="-1" class="p3_M1">
        # <span data-testid="send" data-icon="send" class="">
        # <span aria-label="Pai:"></span>
        # entrar na página

        # Aqui ele vai encontrar o elemento (no caso, aonde digita)   
        chat_box = self.driver.find_element_by_class_name('p3_M1')
        time.sleep(3)
        chat_box.click()
        # aqui ele vai colocar a mensagem
        chat_box.send_keys(texto)
        time.sleep(3)
        # Aqui ele vai achar o botão para enviar
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(3)
        # aqui ele vai clicar para enviar
        botao_enviar.click()
        time(5)
        conversa = self.driver.find_element_by_xpath(f"//span[@title='{self.conversas}']")
        time.sleep(3)
        conversa.click()


bot = WhatsBot()
texto = ''
while texto != ":v":
    if bot.LerMensagem() == '':
        time.sleep(10)
    else:
        texto = bot.LerMensagem()
        bot.EnviarMsg(texto)
