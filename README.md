# computational-linear-algebra
Exercises for the Computational Linear Algebra lecture at UFRJ, 2022/1

## Project Structure


O projeto é feito de forma a modularizar e tornar tudo que foi utilizado reutilizável.
```
-- src
    |_ex1
    |_ex2
    |_ex3
    |_...
    |_utils
```

Assim, o que tiver sido desenvolvido no trabalho 1, por exemplo, pode ser utilizado por outros trabalhos, fora a existência do módulos utils, que contém funcionalidades que serão utilizadas amplamente por diversos trabalhos.


## How to use

Para executar qualquer um dos trabalhos, basta executar o comando `python runner.py` que este te guiará no processo. Ao rodar este comando, será perguntado qual trabalho é desejado a execução.
Será mostrado o seguinte:

```sh
$ python runner.py
> Escolha o trabalho que deseja executar:
```

Após isso, o trabalho sendo executado comandará os inputs necessários.

- [Executando o Trabalho 1](https://github.com/guim4dev/computational-linear-algebra/tree/main/src/ex1)
- [Executando o Trabalho 2](https://github.com/guim4dev/computational-linear-algebra/tree/main/src/ex2)
- [Executando o Trabalho 3](https://github.com/guim4dev/computational-linear-algebra/tree/main/src/ex3)
