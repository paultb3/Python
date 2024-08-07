def agae_value(age):
    if age>18 and age <20:
        return "Puede ingresar"
    if age >15 and age< 18:
        return f"tienes {age} años , muestre permiso"
    if age <15:
        return "Eres menor de edad, no puedes pasar"


age = int(input("Ingrese su edad: "))
agae_value(age)

