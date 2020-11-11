import sympy as sp


def Point_Input():
    d = True
    Points = []
    while d:
        Point = [sp.S(i) for i in input("Valor do Ponto nos eixos X, Y e Z, separados por ',', utilizando . para numeros decimais:").split(',')]
        Points.append(Point)
        temp = int(input("Para adicionar mais pontos digite 1, para continuar digite 0: "))
        if temp == 0:
            d = False
    return Points


def Adding_Vectors(Points):
    n1 = [i for i in range(len(Points) - 1)]
    Final_Vectors = []
    for x in n1:
        TEMP = []
        for i, i2 in zip(Points[x], Points[-1]):
            temp = i - i2
            TEMP.append(temp)
        scalar = sum([x ** 2 for x in TEMP])
        TEMP.append(sp.root(scalar, 2))
        Final_Vectors.append(TEMP)
    return Final_Vectors


def print_output(resultados, desconhecidos):
    for results in resultados:
        for resultado, symbol in zip(results, desconhecidos):
            print(f'{symbol} = ', resultado, "Newtons")




def creating_equations(Vectors, Forces):
    all_forces = []
    for vector, force in zip(Vectors, Forces):
        temp = []
        for i in range(len(vector)-1):
            result = vector[i] * force / vector[-1]
            temp.append(result)
        all_forces.append(temp)
    return all_forces
        
if __name__ == "__main__":
    VECTORS = Adding_Vectors(Point_Input())

    Desconhecidos = []

    for i in range(1, len(VECTORS) + 1):
        exec("Força_%s = sp.symbols('Força-%s'); Desconhecidos.append(Força_%s)" % (i, i, i))

    Force_Extra = [sp.S(i) for i in
                   input("Força extra, fora dos vetores, como força peso (separado por , nos eixos):").split(',')]

    EQUATIONS = creating_equations(VECTORS, Desconhecidos)

    number_temp = 1
    FORCES = []
    for i in range(1,len(EQUATIONS)+1):
        exec("forces%s = []" % i)
        for force in EQUATIONS:
            exec("forces%s.append(force[%s])" % (i, i-1))
        exec("FORCES.append(forces%s)" % i)

    for equations in FORCES:
        equation = "eq%s = equations[0]" % number_temp
        for i in range(1,len(equations)):
            equation = equation + " + equations[%s]" % i
        exec(equation, globals())
        number_temp += 1

    equationes = []
    for i in range(1, number_temp):
        exec("equationes.append(sp.Eq(eq%s, %s))" % (i, Force_Extra[i-1]))

    resultados = sp.linsolve(equationes, Desconhecidos)

    print_output(resultados, Desconhecidos)