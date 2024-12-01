import subprocess
import os

def gerar_diagrama(codigo_uml, nome_arquivo):
    if not os.path.exists('diagramas'):
        os.makedirs('diagramas')

    caminho_temp_uml = os.path.join('diagramas', 'temp_uml.txt')
    with open(caminho_temp_uml, 'w') as file:
        file.write(codigo_uml)

    caminho_jar = 'C:/Users/Luiz/Desktop/projetofinal-pds/code/plantuml-1.2024.8.jar'


    result = subprocess.run(['java', '-jar', caminho_jar, caminho_temp_uml], capture_output=True, text=True)
    

    if result.returncode != 0:
        print(f"Erro ao executar PlantUML: {result.stderr}")
        return


    caminho_completo_arquivo = os.path.join('diagramas', nome_arquivo)


    if os.path.exists(caminho_completo_arquivo):
        os.remove(caminho_completo_arquivo)


    os.rename(os.path.join('diagramas', 'temp_uml.png'), caminho_completo_arquivo)

def diagrama_sequencias():
    uml_code = """
@startuml
actor Atleta
participant SistemaDeAutenticacao
participant Sistema
database BancoDeDados

Atleta -> SistemaDeAutenticacao: Fazer login
SistemaDeAutenticacao -> Atleta: Confirmação de login
Atleta -> Sistema: Solicitar formulário de inscrição
Sistema -> Atleta: Exibir formulário de inscrição
Atleta -> Sistema: Enviar dados de inscrição
Sistema -> Sistema: Validar dados de inscrição
Sistema -> BancoDeDados: Inserir dados de inscrição
BancoDeDados -> Sistema: Confirmar inserção de dados
Sistema -> Atleta: Confirmação de inscrição
@enduml



    """
    gerar_diagrama(uml_code, 'diagrama_sequencias.png')

def diagrama_componentes():
    uml_code = """
@startuml
component "Interface de Usuário" {
    [Frontend]
}

component "Serviço de Autenticação" {
    [AuthService]
}

component "Gestão de Competições" as GC
component "Inscrição de Atletas" as IA
component "Alocação de Locais" as AL
component "Controle de Resultados" as CR
component "Relatórios de Medalhas" as RM
database "Banco de Dados" as DB

[Frontend] --> GC : Acesso via Web
[Frontend] --> IA : Acesso via Web
[Frontend] --> AL : Acesso via Web
[Frontend] --> CR : Acesso via Web
[Frontend] --> RM : Acesso via Web

AuthService --> DB : Verificar e armazenar dados de usuários
GC --> DB : Operações CRUD
IA --> DB : Operações CRUD
AL --> DB : Operações CRUD
CR --> DB : Operações CRUD
RM --> DB : Consultar dados

[Frontend] --> AuthService : Autenticação de Usuários
@enduml

    """
    gerar_diagrama(uml_code, 'diagrama_componentes.png')

def diagrama_classes():
    uml_code = """
    @startuml
class Competicao {
    - id: int
    - nome: String
    - data: Date
    - horario: Time
    - local: String
    - atletas: List<Atleta>
    + cadastrarCompeticao(): void
    + obterCompeticao(id: int): Competicao
    + atualizarCompeticao(): void
    + deletarCompeticao(id: int): void
}

class Atleta {
    - id: int
    - nome: String
    - pais: String
    + inscrever(): void
    + obterAtleta(id: int): Atleta
}

class Local {
    - id: int
    - nome: String
    - disponibilidade: Boolean
    + alocarLocal(): void
    + obterLocal(id: int): Local
}

class Resultado {
    - id: int
    - competicao: Competicao
    - vencedor: Atleta
    - segundo: Atleta
    - terceiro: Atleta
    + registrarResultado(): void
    + obterResultado(id: int): Resultado
}

class RelatorioMedalhas {
    - id: int
    - pais: String
    - ouro: int
    - prata: int
    - bronze: int
    + gerarRelatorio(): void
}

class BancoDeDados {
    + conectar(): void
    + desconectar(): void
    + executarQuery(query: String): ResultSet
}

Competicao "1" -- "*" Atleta: Inscritos
Competicao "1" -- "1" Local: Ocorre em
Competicao "1" -- "1" Resultado: Tem
Resultado "1" -- "1" RelatorioMedalhas: Gera
Competicao --> BancoDeDados : Usa
Atleta --> BancoDeDados : Usa
Local --> BancoDeDados : Usa
Resultado --> BancoDeDados : Usa
RelatorioMedalhas --> BancoDeDados : Usa
@enduml



    """
    gerar_diagrama(uml_code, 'diagrama_classes.png')

def diagrama_caso_de_uso():
    uml_code = """
   @startuml
actor Administrador
actor Atleta
actor SistemaDeAutenticacao

usecase UC1 as "Inscrever Atleta em Competição"

Atleta -> SistemaDeAutenticacao : Fazer login
SistemaDeAutenticacao -> Atleta : Confirmação de login
Atleta -> UC1 : Preencher formulário de inscrição
UC1 -> Administrador : Revisar inscrição
Administrador -> UC1 : Aprovar inscrição
UC1 -> Atleta : Confirmação de inscrição
@enduml


    """
    gerar_diagrama(uml_code, 'diagrama_caso_de_uso.png')

def diagrama_estado():
    uml_code = """
@startuml
[*] --> SolicitaçãoDeInscrição

SolicitaçãoDeInscrição : Atleta solicita inscrição
SolicitaçãoDeInscrição --> PreenchendoFormulario : Formulário de inscrição exibido

PreenchendoFormulario : Atleta preenche os dados
PreenchendoFormulario --> ValidandoDados : Dados enviados para validação

ValidandoDados : Sistema valida os dados de inscrição
ValidandoDados --> InserindoDadosNoBanco : Dados válidos
ValidandoDados --> ErroDeValidacao : Dados inválidos

InserindoDadosNoBanco : Sistema insere dados no banco de dados
InserindoDadosNoBanco --> InscriçãoConfirmada : Dados inseridos com sucesso
InscriçãoConfirmada : Sistema confirma a inscrição
InscriçãoConfirmada --> [*]

ErroDeValidacao : Sistema retorna erro de validação
ErroDeValidacao --> PreenchendoFormulario : Atleta corrige os dados
@enduml




    """
    gerar_diagrama(uml_code, 'diagrama_estado.png')

def diagrama_comunicacao():
    uml_code = """
@startuml
actor Atleta
participant "Interface de Usuário" as IU
participant "Sistema de Autenticação" as Auth
participant "Sistema de Gestão" as SG
database "Banco de Dados" as BD

Atleta -> IU : Solicitar login
IU -> Auth : Enviar credenciais de login
Auth -> IU : Confirmar login
IU -> Atleta : Login confirmado

Atleta -> IU : Solicitar formulário de inscrição
IU -> SG : Solicitar formulário de inscrição
SG -> IU : Exibir formulário de inscrição
IU -> Atleta : Exibir formulário

Atleta -> IU : Preencher e enviar dados de inscrição
IU -> SG : Enviar dados de inscrição
SG -> SG : Validar dados de inscrição
SG -> BD : Inserir dados de inscrição
BD -> SG : Confirmar inserção de dados
SG -> IU : Confirmar inscrição
IU -> Atleta : Confirmação de inscrição
@enduml








    """
    gerar_diagrama(uml_code, 'diagrama_comunicacao.png')
    
    
def diagrama_arquitetura():
    uml_code = """
@startuml
node "Usuário" {
    actor Administrador
    actor Atleta
}

node "Internet" {
    cloud "Servidor Web" {
        [Sistema de Gestão das Olimpíadas]
    }
}

node "Rede Interna" {
    database "Banco de Dados"
}

node "Sistema de Autenticação" {
    [SistemaDeAutenticacao]
}

Administrador -left-> "Sistema de Gestão das Olimpíadas" : Acesso via Web
Atleta -left-> "Sistema de Gestão das Olimpíadas" : Acesso via Web

"Sistema de Gestão das Olimpíadas" -> "SistemaDeAutenticacao" : Autenticação de Usuários
"Sistema de Gestão das Olimpíadas" -> "Banco de Dados" : Operações CRUD

"SistemaDeAutenticacao" -down-> "Banco de Dados" : Armazenamento de Dados de Usuários
@enduml

    """
    gerar_diagrama(uml_code, 'diagrama_arquitetura.png')
    
def diagrama_implantacao():
    uml_code = """
   @startuml
node "Usuários" {
    actor Administrador
    actor Atleta
}

cloud "Internet" {
    node "Servidor Web" {
        [Frontend]
        [AuthService]
        node "Aplicações" {
            [Gestão de Competições]
            [Inscrição de Atletas]
            [Alocação de Locais]
            [Controle de Resultados]
            [Relatórios de Medalhas]
        }
    }
}

node "Rede Interna" {
    database "Banco de Dados"
}

Administrador -left-> [Frontend]
Atleta -left-> [Frontend]

[Frontend] --> [AuthService]
[AuthService] --> [Banco de Dados] : Verificar e armazenar dados de usuários

[Gestão de Competições] --> [Banco de Dados] : Operações CRUD
[Inscrição de Atletas] --> [Banco de Dados] : Operações CRUD
[Alocação de Locais] --> [Banco de Dados] : Operações CRUD
[Controle de Resultados] --> [Banco de Dados] : Operações CRUD
[Relatórios de Medalhas] --> [Banco de Dados] : Consultar dados
@enduml
    """
    gerar_diagrama(uml_code, 'diagrama_implantacao.png')
