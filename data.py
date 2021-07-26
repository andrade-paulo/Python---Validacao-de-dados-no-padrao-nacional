from datetime import datetime, timedelta

class Data:
    def __init__(self):
        self.data_cadastro = datetime.today()
    
    def tempo_cadastro(self):
        agora = datetime.today() + timedelta(days=11, minutes=42, seconds=37)
        return agora - self.data_cadastro

    def __str__(self):
        return self.formatar()

    def formatar(self):
        data_formatada = self.data_cadastro.strftime("%d/%m/%y - %H:%M")
        return data_formatada
