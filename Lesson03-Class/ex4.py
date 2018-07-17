class Map:
    def __init__method(self,size,p):
        self.size=size
        self.lise=[['*']* size for i in range(size)]#創建
        if p==1:
            c=int(self.size/2+0.5) #中心點
            self.lise[c-2][c-2]=int(0)
            self.lise[c-2][c-1]=int(0)
            self.lise[c-2][c]=int(0)
            self.lise[c-1][c-2]=int(0)
            self.lise[c][c-1]=int(0)
            self.replace=self.lise
                       
    def display(self):     
        for i in range(self.size):
            for j in range(self.size):
                print(self.replace[i][j], end=' ')
                if (j+1) % self.size == 0:
                    print(' ')
            
#main
my_map=Map(9,1)#建立 instance object
my_map.display() # 展示有 Glider 圖案的地圖