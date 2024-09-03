class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def aplicar_interes(self):
        if self.saldo < 10000.00:
            self.saldo *= 1.03
        else:
            self.saldo *= 1.04

    def mostrar_saldo_final(self):
        print(f"El Saldo final es: {self.saldo:.2f}")