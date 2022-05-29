class robotPosition:
    x=0
    y=0
    bearing=0
    setFlag=False
    
    def setXPosition(self,x):
        self.x=x
    def setYPosition(self,y):
        self.y=y
        
    def setBearing(self,bearing):
        self.bearing = bearing
        
    def setFlag(self,flag):
        self.setFlag = flag
    
    def getXPosition(self):
        return self.x
    
    def getYPosition(self):
        return self.y
    
    def getBearing(self):
        return self.bearing
    
    def getFlag(self):
        return self.setFlag 
    
    
    def getFullPosition(self):        
        return (str(self.x) +"," +str(self.y) +","+ str(self.bearing)) 