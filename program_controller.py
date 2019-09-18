#!/usr/bin/python3

# import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
menu = True

while (menu == True):
    print("Selecione sua opcao:(Q para sair)\n")
    print("Acender led: A\t apagar led: X\n Mudar frequencia envio: M")
    a = input()
    if(a == "A" or a =="a"):
        publish.single("led", "A", hostname="localhost")
    if(a == "X" or a =="x"):
        publish.single("led", "X", hostname="localhost")
    if(a == "M" or a =="m"):
        print("Insira a frequencia de envio:\t(Q para sair)\n")    
        a = input()
        publish.single("led", a, hostname="localhost")
    if(a =="Q"):
        menu = False
    # problemas: não consegui transformar binario para int no arduino
    # problemas2: lê alguns dados da serial e para
    
