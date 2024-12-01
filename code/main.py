import sys
from diagrama_uml import (
    diagrama_sequencias,
    diagrama_componentes,
    diagrama_classes,
    diagrama_caso_de_uso,
    diagrama_estado,
    diagrama_comunicacao
)

def menu():
    while True:
        print("\nMenu de Diagramas UML")
        print("1. Diagrama de Sequências")
        print("2. Diagrama de Componentes")
        print("3. Diagrama de Classes")
        print("4. Diagrama de Caso de Uso")
        print("5. Diagrama de Estado")
        print("6. Diagrama de Comunicação")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            diagrama_sequencias()
            print("Diagrama de Sequências gerado como 'diagrama_sequencias.png'.")
        elif escolha == '2':
            diagrama_componentes()
            print("Diagrama de Componentes gerado como 'diagrama_componentes.png'.")
        elif escolha == '3':
            diagrama_classes()
            print("Diagrama de Classes gerado como 'diagrama_classes.png'.")
        elif escolha == '4':
            diagrama_caso_de_uso()
            print("Diagrama de Caso de Uso gerado como 'diagrama_caso_de_uso.png'.")
        elif escolha == '5':
            diagrama_estado()
            print("Diagrama de Estado gerado como 'diagrama_estado.png'.")
        elif escolha == '6':
            diagrama_comunicacao()
            print("Diagrama de Comunicação gerado como 'diagrama_comunicacao.png'.")
        elif escolha == '0':
            print("Saindo...")
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
