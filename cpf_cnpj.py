from validate_docbr import CPF, CNPJ

class Documento: # Factory Method
    @staticmethod
    def criar_novo(documento):
        strdoc = str(documento)
        if len(strdoc) == 11:
            return DocPdf(documento)
        elif len(strdoc) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Número de dígitos inválidos.")

class DocPdf:
    def __init__(self, documento):
        if self.validar_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.formatar()

    def validar_cpf(self, documento):
        objeto = CPF()
        return objeto.validate(documento)
    
    def formatar(self):
        objeto = CPF()
        return objeto.mask(self.cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.validar_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido")

    def __str__(self):
        return self.formatar()

    def validar_cnpj(self, documento):
        objeto = CNPJ()
        return objeto.validate(documento)
    
    def formatar(self):
        objeto = CNPJ()
        return objeto.mask(self.cnpj)
