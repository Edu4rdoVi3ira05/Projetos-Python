#Variaveis
MAIUSCULAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SUB_MAIUSCULAS = 'QWERTYUIOPASDFGHJKLZXCVBNM'

MINUSCULAS = 'abcdefghijklmnopqrstuvwxyz'
SUB_MINUSCULAS = 'qwertyuiopasdfghjklzxcvbnm'

NUMEROS = '0123456789'
SUB_NUMEROS = '9876543210'

SIMBOLOS = '!@#$%^&*()_+-=[]{}|;:,.<>?'
SUB_SIMBOLOS = SIMBOLOS[::-1]  

#Parte Interativa
def main():
    mapa_sub = criar_mapa_substituicao()
    
    print("=======================")
    print(" ENCRIPTADOR DE SENHAS ")
    print("=======================")
    
    while True:
        print("\n1. Encriptar senha")
        print("2. Decifrar senha")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == '1':
            senha = input("Digite a senha para encriptar: ")
            senha_encriptada = encriptar(senha, mapa_sub)
            print(f"Senha encriptada: {senha_encriptada}")
            
        elif opcao == '2':
            senha_enc = input("Digite a senha encriptada: ")
            senha_original = decifrar(senha_enc, mapa_sub)
            print(f"Senha original: {senha_original}")
            
        elif opcao == '3':
            print("Até logo!")
            break
            
        else:
            print("Opção inválida!")

#Funcionamento
def criar_mapa_substituicao():
    """Cria o mapa de substituição"""
    mapa = {}

    for i, char in enumerate(MAIUSCULAS):
        mapa[char] = SUB_MAIUSCULAS[i]
    
    for i, char in enumerate(MINUSCULAS):
        mapa[char] = SUB_MINUSCULAS[i]
    
    for i, char in enumerate(NUMEROS):
        mapa[char] = SUB_NUMEROS[i]
    
    for i, char in enumerate(SIMBOLOS):
        mapa[char] = SUB_SIMBOLOS[i]
    
    return mapa


def encriptar(senha, mapa):
    return ''.join(mapa.get(char, char) for char in senha)


def decifrar(senha_encriptada, mapa):
    mapa_inverso = {v: k for k, v in mapa.items()}
    return ''.join(mapa_inverso.get(char, char) for char in senha_encriptada)

#Main
if __name__ == "__main__":
    main()
