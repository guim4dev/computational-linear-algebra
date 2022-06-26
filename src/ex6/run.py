from src.ex6.runge_kutta_nystrom import RungeKuttaNystrom
import pandas as pd
import matplotlib.pyplot as plt

def run():
    time = float(input('Tempo total de integração: '))
    passo = float(input('Passo de integração: '))
    m, c, k, a1, a2, a3, w1, w2, w3 = 0, 0, 0, 0, 0, 0, 0, 0, 0

    switcher = int(input('Deseja rodar o teste pré-configurado? 1 para sim, 2 para não: '))
    if switcher == 1:
        m = 1
        c = 0
        k = 2
        a1 = 1
        a2 = 2
        a3 = 1.5
        w1 = 0.05
        w2 = 1
        w3 = 2
    else:
        m = float(input('m: '))
        c = float(input('c: '))
        k = float(input('k: '))
        a1 = float(input('a1: '))
        a2 = float(input('a2: '))
        a3 = float(input('a3: '))
        w1 = float(input('w1: '))
        w2 = float(input('w2: '))
        w3 = float(input('w3: '))

    runge_kutta_nystton = RungeKuttaNystrom(
        m=m, c=c, k=k, a1=a1, a2=a2, a3=a3, w1=w1, w2=w2, w3=w3, total_time=time, step=passo)
    
    data_points = runge_kutta_nystton.solve()
    data_points_df = pd.DataFrame(data_points)
    data_points_df.plot(x='tempo', y=['deslocamento', 'velocidade', 'aceleracao'])
    data_points_df.to_csv('tests/ex6/data_points.csv')

    plt.savefig('tests/ex6/moments.png')
    print("Arquivos de saída gerados com sucesso!")
