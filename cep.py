import requests

class Endereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.validar_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido")
    
    def validar_cep(self, numero):
        if len(numero) == 8:
            return True
        else:
            return False

    def __str__(self) :
        return self.formatar()

    def formatar(self):
        cep_formatado = f"{self.cep[:5]}-{self.cep[5:]}"
        return cep_formatado
    
    def acesso_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        return (dados['bairro'], dados['localidade'], dados['uf'])
