#from numpy import False_
from robotPosition import robotPosition

class toyRobot:
    commandBuffer =0
    bearing= ''
    bearingPlace=''
    xPlace=0
    yPlace=0

    errorStatusMessage=''


    rows,cols =(6,6) #table dimensions array will have length 6 instead of 5 due to the fact that a cartesean plane for any  distance starts from 0,0. Each array elemnt represent a point in the cartesean plane

    table=[[0]*cols]*rows

    robot = robotPosition()
    bearings = ["NORTH","EAST","SOUTH","WEST"]
    tableAxis= ["x","y"]
    moveArithmetic = ["+","-"]
    currentBearingIndex=0


    def isCommandValid(self,commandString):
        
        commandArray = commandString.split(',')
        
        if(len(commandArray)==1):
        
            if (commandArray[0] == "MOVE"):
                return True
            elif(commandArray[0] == "REPORT"):
                return True
            elif(commandArray[0] == "LEFT"):
                return True
            elif(commandArray[0] == "RIGHT"):
                return True
            else:           
                self.errorStatusMessage = "Error: Invalid command (unrecognised bearing)"
                return False
        
        elif(len(commandArray)==3):
            
            tempBuffer= commandArray[0].split(' ')
            if(len(tempBuffer)==2):
                if(tempBuffer[0]=="PLACE" and (self.checkInteger(tempBuffer[1]))):
                    self.xPlace= tempBuffer[1]
                    
                    if(self.checkInteger(commandArray[1])):
                        self.yPlace= commandArray[1]
                        
                        
                        if(self.validateBearing(commandArray[2])):
                            self.bearingPlace= commandArray[2]
                            return True
                        else:
                            self.errorStatusMessage="Error: Invalid command (argument 3)"
                            return False
                    else:
                        self.errorStatusMessage = "Error: Invalid command (argument 2)"
                        return False
                else:
                    self.errorStatusMessage ="Error: Invalid command (argument 1)"
                    return False
                
            
            else:
                self.errorStatusMessage ="Error: Invalid Command on argument 1"
                return False
        else:
            self.errorStatusMessage= "Error: Invalid command"
            return False
                    


    def validateBearing(self,bearingParam):
        
        try:
            arrayIndex= self.bearings.index(bearingParam)
            return True
        except ValueError:
            return False
        
    def checkInteger(self,value):
        
        try:
            int(value)
            return True
        except ValueError:
            return False
        
    def setBearingIndex(self,bearing):        
        
        index = self.bearings.index(bearing)
        self.currentBearingIndex= index
        
        
        
    def changeBearing(self,rotation):        
        
        if(rotation=="LEFT"):
            if((self.currentBearingIndex-1) <0):
                self.currentBearingIndex = len(self.bearings) -1
            else:
                self.currentBearingIndex -= 1
        
        elif(rotation=="RIGHT"):
            if((self.currentBearingIndex+1) >3):
                self.currentBearingIndex = 0
            else:
                self.currentBearingIndex += 1
                
        self.robot.bearing = self.bearings[self.currentBearingIndex]
        return True
            

    def move(self,bearing):
        
        if(bearing=="NORTH"):
            return self.moveRobot(self.moveArithmetic[0],self.tableAxis[1])
        elif(bearing=="EAST"):
            return self.moveRobot(self.moveArithmetic[0],self.tableAxis[0])
        elif(bearing=="SOUTH"):
            return self.moveRobot(self.moveArithmetic[1],self.tableAxis[1])
        elif(bearing=="WEST"):
            return self.moveRobot(self.moveArithmetic[1],self.tableAxis[0])
        else:
            print("invalid direction")
            return False


    def placeRobot(self,x,y):
        
        if(self.validateBoundaries(int(x),int(y))):
            self.robot.setXPosition(x)
            self.robot.setYPosition(y)
            self.robot.setBearing(self.bearingPlace)
            self.setBearingIndex(self.bearingPlace)
            self.robot.setFlag=True
            return True
        else:
            print("Forbidden Placement: off table placement is not allowed")
            return False
            
        
    def moveRobot(self,direction,axis):
        
        if(axis=="y"):
            yMove=eval(str(self.robot.getYPosition()) + str(direction) +str(1))
            if(self.validateBoundaries(self.robot.getXPosition(),yMove)):
                self.robot.setYPosition(yMove)
                return True
            else:
                print("Forbidden move: Robot not allowed to fall")
                return False
        else:
            xMove= eval(str(self.robot.getXPosition()) + str(direction) + str(1))
            if(self.validateBoundaries(xMove,self.robot.getYPosition())):
                self.robot.setXPosition(xMove)
                return True
            else:
                print("Forbidden move: Robot not allowed to fall")
                return False
            

    def validateBoundaries(self,x,y):
        
        try:
            if(int(x)>=0 and int(y)>=0):            
                self.table[int(x)][int(y)]
                return True
            else:
                return False
        except IndexError:
            return False
        

    def gridCommand(self,commandString):
        
        if (commandString == "MOVE"):
            return self.move(self.robot.getBearing())
        elif(commandString == "REPORT"):
            print("Output: ",self.robot.getFullPosition())
            return True
        elif(commandString == "LEFT"):
            return self.changeBearing("LEFT")
        elif(commandString == "RIGHT"):
            return self.changeBearing("RIGHT")
        
        
    def isRobotPlaced(self):
        
        if(self.robot.setFlag == True):
            return True
        else:
            print("Error: Robot has not been placed on the table")
            return False


    def executeCommand(self,inputString):

            commandBuffer = inputString.split(',')
            command_size= len(commandBuffer)       
            
            commandStatus = self.isCommandValid(inputString)
            if(commandStatus):
                        
                if(command_size == 3):
                    return self.placeRobot(self.xPlace,self.yPlace)                                               
                
                elif(command_size==1 and self.isRobotPlaced()):              
                    return self.gridCommand(commandBuffer[0])                                
                    
            else:
                print(self.errorStatusMessage)
                return False

    
if __name__ == "__main__":

    robotInstance = toyRobot()
           
    while(1):
    
        inputCommand = str(input("Enter commnand:"))
        robotInstance.executeCommand(inputCommand)

                    
                

                
            
            
            
    


