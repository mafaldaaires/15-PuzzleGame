from Board import Board

def main():
    list=[int(i) for i in input().split()]
    matrix=[[0 for l in range(4)] for l in range(4)]
    k=0
    for i in range(4):
        for j in range(4):
            matrix[i][j]=list[k]
            if(matrix[i][j]==0):
                blank_pos=[i,j]
            k+=1

    print("blank:(%d,%d)" %(blank_pos[0],blank_pos[1]))
    print()

    print("the matrix:")
    for i in matrix:
        for j in i:
            print(j, end="|")
        print()

    jogo=Board(matrix,blank_pos)
    print()
    print("__repr__ funtion:")
    print(jogo)
    print()
    print("is it possible?")
    if jogo.possible():
        print("yes, it is")
    else:  
        print("no, it is not")
    print()
    print("TESTAR COMANDOS")
    print()
    print("inicial:")
    print(jogo)
    print("up:")
    jogo.up()
    print(jogo)
    print("right:")
    jogo.right()
    print(jogo)
    print("down:")
    jogo.down()
    print(jogo)
    print("left:")
    jogo.left()
    print(jogo)

main()