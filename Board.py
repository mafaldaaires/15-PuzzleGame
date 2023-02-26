ROWS = 4
COLS = 4
class Board:

    def __init__(self,matrix,blank):
        self.board=matrix
        self.blank=blank #[x,y] vetor com a posiçao do quadrado branco
        self.goal=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

    
    def __repr__(self): #semelhante a __str___
        k=0
        for i in self.board:
            for j in i:
                print(j, end = " ")
            if(k<3):
                print()
            k += 1
        return "" #funçao repr obriga a retornar algo
        
    def blank_position(self):
        return self.blank

    def finished(self):
        pass

    #de matriz para lista
    def correspond_list(self, matriz):
        list = [item for sublist in matriz for item in sublist]
        return list

    #funçao pa contar inverçoes N de uma lista correspontente configuraçao da matriz
    def inversions(self, list):
        inv = 0
        for i in range(len(list)):
            for j in range(i+1,len(list)):
                if (list[i]>list[j] and list[i]!=0 and list[j]!=0):
                    inv += 1
        return inv

    #tendo em conta que o tabuleiro terá sempre tamanho par
    def possible(self):
        lista=self.correspond_list(self.board)    # lista que corresponde ao self.board
        n_inv=self.inversions(lista)              # número de inversões
        i_blank=self.blank[0]                     # indice da linha do branco
        if ((n_inv%2)!=(i_blank%2)):
            return True
        return False

    #comando, mover branco para cima
    def up(self):
        if (self.blank[0]>0 and self.blank[0]<=3):
            upper=self.board[self.blank[0]-1][self.blank[1]] #upper é uma variavel aux que guarda o valor a cima do blank
            self.board[self.blank[0]-1][self.blank[1]]=0
            self.board[self.blank[0]][self.blank[1]]=upper #neste ponto a troca ja aconteceu
            self.blank[0]-=1 #atualizar localizaçao do blank
        else: 
            return 

    #comando, mover branco para baixo
    def down(self):
        if (self.blank[0]<3 and self.blank[0]>=0):
            lower=self.board[self.blank[0]+1][self.blank[1]] #lower é uma variavel aux que guarda o valor a baixo do blank
            self.board[self.blank[0]+1][self.blank[1]]=0
            self.board[self.blank[0]][self.blank[1]]=lower #neste ponto a troca ja aconteceu
            self.blank[0]+=1 #atualizar localizaçao do blank
        else: 
            return 
    
    #comando, mover branco para a direita 
    def right(self):
        if (self.blank[1]<3 and self.blank[1]>=0):
            thenext=self.board[self.blank[0]][self.blank[1]+1] #thenext é uma variavel aux que guarda o valor a direita do blank
            self.board[self.blank[0]][self.blank[1]+1]=0
            self.board[self.blank[0]][self.blank[1]]=thenext #neste ponto a troca ja aconteceu
            self.blank[1]+=1 #atualizar localizaçao do blank
        else: 
            return 
    
    #comando, mover branco para a esquerda
    def left(self):
        if (self.blank[1]>0 and self.blank[1]<=3):
            theprev=self.board[self.blank[0]][self.blank[1]-1] #thenext é uma variavel aux que guarda o valor a direita do blank
            self.board[self.blank[0]][self.blank[1]-1]=0
            self.board[self.blank[0]][self.blank[1]]=theprev #neste ponto a troca ja aconteceu
            self.blank[1]-=1 #atualizar localizaçao do blank
        else: 
            return 
    

    #passar lista para matriz
    #def matriz(self):
    #    size = 4
    #    matrix = [self.goal[i:i+size] for i in range(0, len(self.goal), size)]
    #    return matrix