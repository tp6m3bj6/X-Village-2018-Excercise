#八皇后

def eight_queens(par):
    l = len(par)
    n=0
    n2=0 
    for i in range(2):#各list內0和1
        for j in range(l):#判斷8個list
            for k in range(j+1,8):
                if par[j][i] == par[k][i]:
                    n+=1
                else:
                    pass    
    
    if n!=0:
        print('False')
    else:
        for ii in range(l-1):
                if (par[ii][0]-par[ii+1][0]) == (par[ii][1]-par[ii+1][1]) or (par[ii][0]-par[ii+1][0]) == -(par[ii][1]-par[ii+1][1]):
                    n2+=1     
                else:
                    pass

    if n2==0:
        print("True")
    else:
        print("False")


eight_queens([[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]])
