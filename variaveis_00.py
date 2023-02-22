import numpy as np

x = []
y = []

x2 = []
y2 = []
produtoxy = []

tamanho = int(input('\033[37m' + "Digite o tamanho do numero de amostras: " + '\033[37m'))

print("\033[31m " + "-------------------------" + "\033[31m")
print("Valores de x: ")
for k in range(0, tamanho):
    Valor1 = float(input("Digite o valor para x: "))
    x.append(Valor1)

print("\033[32m " + "-------------------------" + "\033[32m")
print("Valores de y: ")
for i in range(0, tamanho):
    valor2 = float(input("Digite o valor para y: "))
    y.append(valor2)

print('\033[37m', x, " = ", y, '\033[37m')

def media():
    mx = sum(x)/len(x)
    my = sum(y)/len(y)
    print(mx.__round__(4))
    print(my.__round__(4))

def valor_incerteza():
    dx = np.std(x)
    mx = np.mean(x)
    dy = np.std(y)
    my = np.mean(y)
    print("X= {} +/- {}".format(mx.round(4), dx.round(4)))
    print("Y = {} +/- {}".format(my.round(4), dy.round(4)))

def correlacao_regressao():
    for i in range(0, tamanho):
        x2.append(x[i]**2)
        y2.append(y[i]**2)
        produtoxy.append(x[i]*y[i])

    rx = tamanho*(sum(produtoxy)) - sum(x)*sum(y)
    ry = np.sqrt(tamanho*sum(x2) - sum(x)**2)*np.sqrt(tamanho*sum(y2) - sum(y)**2)
    rxy = rx/ry

    print("correlacao = {}".format(rxy.__round__(4)))
    if rxy < 0 and rxy > -0.5:
        print("Correlacao fraca negativa")
    elif rxy <= -0.5 and rxy > -1:
        print("Correlacao forte negativa")
    elif rxy > 0 and rxy < 0.5:
        print("Correlacao fraca positiva")
    elif rxy >= 0.5 and rxy <= 1:
        print("Correlacao forte positiva")
    else:
        print("Sem correlacao") #se a correlacao for fraca quase nao ha uma reta

    b = (tamanho*sum(produtoxy) - sum(x)*sum(y))/(tamanho*sum(x2) - sum(x)**2)
    a = (sum(y) - b*sum(x))/tamanho

    print("y = {} + {}x".format(a.__round__(4), b.__round__(4)))

correlacao_regressao()