class Pagamento:
    def processar(self, valor):
        return valor


class Dinheiro(Pagamento):
    def processar(self, valor):
        return valor * 0.95


class Cartao(Pagamento):
    def processar(self, valor):
        return valor * 1.02


class Pix(Pagamento):
    def processar(self, valor):
        return valor


pagamentos = [Dinheiro(), Cartao(), Pix()]

valor = 100

for pagamento in pagamentos:
    valor_final = pagamento.processar(valor)
    print(f"{pagamento.__class__.__name__}: R$ {valor_final:.2f}")
