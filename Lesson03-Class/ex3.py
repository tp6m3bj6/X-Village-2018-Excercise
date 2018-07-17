class Map:
    def set_map(self,size):
        self.size=size
        self.lise=[['*']* size for i in range(size)]#創建list陣列
        
    def set_pattern(self,p):
        if p==1:
            c=int(self.size/2+0.5) #中心點座標位置
            self.lise[c-2][c-2]=int(0)#以下為Glide位置需變成0
            self.lise[c-2][c-1]=int(0)
            self.lise[c-2][c]=int(0)
            self.lise[c-1][c-2]=int(0)
            self.lise[c][c-1]=int(0)
            self.replace=self.lise
        else:
            self.replace=self.lise #若p不為1則不做Glide   
                       
    def display(self):     
        for i in range(self.size):
            for j in range(self.size):
                print(self.replace[i][j], end=' ')
                if (j+1) % self.size == 0:
                    print(' ')
            
#main
my_map=Map()#建立 instance object
my_map.set_map(9) # size, 代表地圖為 nxn 大小
my_map.set_pattern(1)# p=1, 設置 Glider 圖案在地圖中央
my_map.display() # 展示有 Glider 圖案的地圖