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


def print_output(results):
    for name, value in results.items():
        print(f"{name} =", value, "Newtons")


def creating_equations(Vectors, Forces):
    all_forces = []
    for vector, force in zip(Vectors, Forces):
        temp = []
        for i in range(len(vector)-1):
            result = vector[i] * force / vector[-1]
            temp.append(result)
        all_forces.append(temp)
    print(all_forces)
        
if __name__ == "__main__":
    VECTORS = Adding_Vectors(Point_Input())

    Desconhecidos = []

    for i in range(1, len(VECTORS) + 1):
        exec("global Força_%s; Força_%s = sp.symbols('Força-%s'); Desconhecidos.append(Força_%s)" % (i, i, i, i))

    Force_Extra = [sp.S(i) for i in
                   input("Força extra, fora dos vetores, como força peso (separado por , nos eixos):").split(',')]

    EQUATIONS = creating_equations(VECTORS, Desconhecidos)

    for equation in EQUATIONS[0]:








'''
eq1 = sp.Eq(VECTORS[0][0] * Force1 / VECTORS[0][-1] + VECTORS[1][0] * Force2 / VECTORS[1][-1] + VECTORS[2][0] * Force3 /
            VECTORS[2][-1], -Force_Extra[0])
eq2 = sp.Eq(VECTORS[0][1] * Force1 / VECTORS[0][-1] + VECTORS[1][1] * Force2 / VECTORS[1][-1] + VECTORS[2][1] * Force3 /
            VECTORS[2][-1], -Force_Extra[1])
eq3 = sp.Eq(VECTORS[0][2] * Force1 / VECTORS[0][-1] + VECTORS[1][2] * Force2 / VECTORS[1][-1] + VECTORS[2][2] * Force3 /
            VECTORS[2][-1], -Force_Extra[2])

equations = [eq1, eq2, eq3]

Result = sp.solve(equations, Desconhecidos)

print_output(Result)
'''