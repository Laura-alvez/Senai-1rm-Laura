from time import sleep

def contagem_regressiva(número):
    while número > 0:
        número = número - 1
        print(número)
        sleep(1)

contagem_regressiva(10)