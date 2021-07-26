from cpf_cnpj import Documento
from telefone import Telefone
from data import Data
from cep import Endereco

# Dados
numero_cpf = "62634871007"
numero_cnpj = "98877312000182"
numero_telefone = "558299334902"
numero_cep = "01001000"

# Objetos
cnpj = Documento.criar_novo(numero_cnpj)
cpf = Documento.criar_novo(numero_cpf)
telefone = Telefone(numero_telefone)
cep = Endereco(numero_cep)
data = Data()

# Dados específicos
bairro, localidade, uf = cep.acesso_via_cep()
tempo_de_cadastro = data.tempo_cadastro()

# Outputs
print(f"""CPF: {cpf}
CNPJ: {cnpj}
Telefone: {telefone}
Data do cadastro: {data}
Tempo de cadastro: {tempo_de_cadastro}
CEP: {cep}
Endereço: {bairro} - {localidade} - {uf}""")
