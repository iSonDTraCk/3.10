from CuentaBancaria import CuentaBancaria
saldo_inicial = float(input("Ingrese el saldo actual: "))
cuenta = CuentaBancaria(saldo_inicial)
cuenta.aplicar_interes()
cuenta.mostrar_saldo_final()
