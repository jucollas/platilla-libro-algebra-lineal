from grading import check

@check
def check_list(glob):
    ans = glob["ans"]   # El arreglo del estudiante
    n   = glob["n"]     # El valor de n que se espera usar
    
    # Generamos el arreglo esperado
    expected = []
    for i in range(n+1):
        if i % 2 == 0:
            expected.append(i)
    
    if ans == expected:
        print(f"✅ Correcto: tu arreglo contiene todos los pares de 0 a {n}.")
    else:
        print(f"❌ Incorrecto: tu arreglo no coincide con lo esperado para n={n}.")
        print(f"    Tu resultado:     {ans}")
        print(f"    Resultado esperado: {expected}")
