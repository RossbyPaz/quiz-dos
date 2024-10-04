nombre="Luis vejarano"
dias_laborados=(int("7"))
salario= (float("785000"))

prima= salario*dias_laborados/360
cesantias= salario * dias_laborados /360
intereses_cesantias= cesantias * 0.12 / dias_laborados
vacaciones = salario *dias_laborados / 720
liquidacion= prima + cesantias + intereses_cesantias + vacaciones

print(f"Señor {nombre} para los {dias_laborados} dias laborados y salario {salario} su liquidacion se compone así: ")
print(f"prima: {prima:.2f}")
print(f"Cesantía: {cesantias:.2f}")
print(f"Intereses_cesatias: {intereses_cesantias:.2f}")
print(f"Vacaciones: {vacaciones:.2f}")
print(f"liquidacion: {liquidacion:.2f}")