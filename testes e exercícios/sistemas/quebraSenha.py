from zipfile import ZipFile # Importando os arquivos

def gerandoPWD(): # Função para gerar às senhas
    password = [] # Var para armazenar
    i = 0
    while i < 10000:
        i += 1
        pwd = str(i)
        print('Buscando...', pwd)
        password.append(pwd) # pwd vai receber todos os dados e passar para password
    return password
    
def quebrandoPWD(): # Nessa parte vamos quebrar a senha
    pwd = gerandoPWD() # pwd vai receber agora todos os dados contidos na função 'gerandoPWD()'
    zip_file = 'textinho.zip' # vamos passa uma variavel que vai receber o arquivo
    
    for c in pwd: # agora c vai procurar a senha contida em 'pwd'
        with ZipFile(zip_file) as zf: # aqui seria para simplificar para zf
            try:
                zf.extractall(pwd=bytes(c, encoding='utf-8'))
                print('Força Bruta')
                return(c)
            except:
                pass


print('A senha é: ' + str(quebrandoPWD()))
