import subprocess
import os

def gerar_diagrama(codigo_uml, nome_arquivo):
    # Criar a pasta 'diagramas' se ela não existir
    if not os.path.exists('diagramas'):
        os.makedirs('diagramas')

    # Salvar o código UML em um arquivo temporário dentro da pasta 'diagramas'
    caminho_temp_uml = os.path.join('diagramas', 'temp_uml.txt')
    with open(caminho_temp_uml, 'w') as file:
        file.write(codigo_uml)

    # Caminho absoluto para o arquivo JAR do PlantUML
    caminho_jar = 'C:/Users/Luiz/Desktop/projetofinal-pds/code/plantuml-1.2024.8.jar'

    # Executar o comando PlantUML via subprocess
    result = subprocess.run(['java', '-jar', caminho_jar, caminho_temp_uml], capture_output=True, text=True)
    
    # Verificar se o comando foi executado corretamente
    if result.returncode != 0:
        print(f"Erro ao executar PlantUML: {result.stderr}")
        return

    # Caminho completo para o arquivo de saída
    caminho_completo_arquivo = os.path.join('diagramas', nome_arquivo)

    # Verificar se o arquivo de saída já existe e excluí-lo se necessário
    if os.path.exists(caminho_completo_arquivo):
        os.remove(caminho_completo_arquivo)

    # Renomear o arquivo de saída para o nome desejado
    os.rename(os.path.join('diagramas', 'temp_uml.png'), caminho_completo_arquivo)

def diagrama_sequencias():
    uml_code = """
    @startuml
    Alice -> Bob: Teste de Sequência
    @enduml
    """
    gerar_diagrama(uml_code, 'diagrama_sequencias.png')

def diagrama_componentes():
    uml_code = """
    @startuml
    [ComponentA] --> [ComponentB]
    @enduml
    """
    gerar_diagrama(uml_code, 'diagrama_componentes.png')

def diagrama_classes():
    uml_code = """
    @startuml
    class ClassA
    class ClassB
    ClassA --> ClassB: Associação
    @enduml
    """
    gerar_diagrama(uml_code, 'diagrama_classes.png')

def diagrama_caso_de_uso():
    uml_code = """
    @startuml
    Actor -> (Caso de Uso)
    @enduml
    """
    gerar_diagrama(uml_code, 'diagrama_caso_de_uso.png')

def diagrama_estado():
    uml_code = """
    @startuml
    [*] --> Estado1
    Estado1 --> Estado2
    @enduml
    """
    gerar_diagrama(uml_code, 'diagrama_estado.png')

def diagrama_comunicacao():
    uml_code = """
    @startuml
    Bob -> Alice : Teste de Comunicação
    @enduml
    """
    gerar_diagrama(uml_code, 'diagrama_comunicacao.png')
