from familia.models import familia
familia(nombre="Cristiano", direccion="Americo vespucio 745", numero_pasaporte=123123).save()
familia(nombre="Enrique", direccion="Rio Parana 745", numero_pasaporte=890890).save()
familia(nombre="Jose", direccion="Becerrina 8544", numero_pasaporte=345345).save()
familia(nombre="Carlos", direccion="San miguel 31", numero_pasaporte=567567).save()

print("Se cargo con éxito los usuarios de pruebas")
