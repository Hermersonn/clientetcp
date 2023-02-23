# Modulo que faz o relacionamento com a placa de rede com o S.O
import socket
# Modulo fornece o acesso a algumas variaveis e funçoes que tem forte interaçao com o interpretador 
import sys

# função para criar a conexão
def main ():

    try:
        # Variavel com o metodo para a conexão, passando como parametro o tipo de conexão que ira fazer
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    # Se tiver alguma exceção ele vai disparar um erro e printar o motivo do erro
    except socket.error as erro:
        print("A conexão falhou")
        print(f"Erro: {erro}")
        # Ira finalizar a conexão se der erro
        sys.exit()
    
    # Menssagem que vai ser disparada apos ter conectado com o host. 
    print("Socket criado com sucesso.")

    # input para digitar o host que vai ser conectado
    hostAlvo = input("Digite o Host ou IP a ser conectado: ")
    # Input para digitar a porta TCP pra ser conectada
    portaAlvo = input("Digite a porta a ser conectada: ")

    # Tentando a conexão
    try:
        # Passando o host e a porta para a conexão
        s.connect((hostAlvo, int(portaAlvo)))
        # Se a conexão der certo ira printar mensagem na tela
        print(f"Cliente TCP conectado com sucesso no host: {hostAlvo} e na porta: {portaAlvo}. ")
        # Ira fechar a conexão depois de 2 minutos
        s.shutdown(2)
    except socket.error as e:
        print("A conexão falhou.")
        print(f"Erro: {e}")
        # Se der erro ele ira sair da aplicaçao
        sys.exit()

# Chamando a função pelo nome criado
if __name__ == "__main__":
    main()