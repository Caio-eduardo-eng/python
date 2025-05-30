import main
dict_carro: dict = {
    "marca" : "FIAT",
    "modelo" : "Chronos",
    "ano" : 2023,
    "cor" : "prata"}
print("o modelo do carro é: ", dict_carro["modelo"])
print("o ano do carro é: ",dict_carro["ano"])
print("a marca di carro é: ",dict_carro["marca"])
print("a cor do carro é: ",dict_carro["cor"])
print(dict_carro.keys())
print(dict_carro.values())
for item in dict_carro.keys():
    print(dict_carro.get(item))
main.somar





def somar():
    num1 : int = int(input("informe um numero"))
    num2 : int = int(input("informe um numero")) 
    num2 : int = int(input("informe um numero"))
    total: int = num1 + num2
    print("a soma totap")
    
    
    somar()







#print(dict_carro)
#dict_carro.pop("marca")
#del dict_carro['modelo']
#print(dict_carro)