import unittest
from unittest import result

from numpy import True_
import toyrobot

class TestRobot(unittest.TestCase):

    def setUp(self):
        self.robot = toyrobot.toyRobot()
        pass

    def tearDown(self):
        pass

    def test_validateBoundaries(self):
       
        self.assertEqual(self.robot.validateBoundaries(0,0),True)
        self.assertEqual(self.robot.validateBoundaries(5,5),True)
        self.assertEqual(self.robot.validateBoundaries(3,3),True)
        self.assertEqual(self.robot.validateBoundaries(6,0),False)
        self.assertEqual(self.robot.validateBoundaries(0,6),False)
        self.assertEqual(self.robot.validateBoundaries(-1,0),False)
        self.assertEqual(self.robot.validateBoundaries(0,-1),False)
        self.assertEqual(self.robot.validateBoundaries(-5,-5),False)
        


    def test_commnandValidity(self):
        self.assertEqual(self.robot.isCommandValid("MOVE"),True)
        self.assertEqual(self.robot.isCommandValid("REPORT"),True)
        self.assertEqual(self.robot.isCommandValid("LEFT"),True)
        self.assertEqual(self.robot.isCommandValid("RIGHT"),True)
        self.assertEqual(self.robot.isCommandValid("PLACE 1,2,NORTH"),True)
        self.assertEqual(self.robot.isCommandValid("PLACE 5,5,WEST"),True)
        self.assertEqual(self.robot.isCommandValid("PLACE 1,2,SOUTH"),True)
        self.assertEqual(self.robot.isCommandValid("PLACE 1,2,EAST"),True)
        self.assertEqual(self.robot.isCommandValid("PLACE 1,2,EASSS"),False)
        self.assertEqual(self.robot.isCommandValid("PLAACE 1,2,EAST"),False)
        self.assertEqual(self.robot.isCommandValid("PLACE q,2,NORTH"),False)
        self.assertEqual(self.robot.isCommandValid("PLACE 1,r,NORTH"),False)


    def test_BearingChange(self):
        self.assertEqual(self.robot.changeBearing("LEFT"),True)
        self.assertEqual(self.robot.changeBearing("RIGHT"),True)
        self.assertEqual(self.robot.changeBearing("Up"),True)
        self.assertEqual(self.robot.changeBearing("Down"),True)

    def test_fullRobotMoveCommand(self):
        self.assertEqual(self.robot.executeCommand("PLACE 1,1,NORTH"),True)
        self.assertEqual(self.robot.executeCommand("REPORT"),True)
        self.assertEqual(self.robot.executeCommand("MOVE"),True)
        self.assertEqual(self.robot.executeCommand("RIGHT"),True)
        self.assertEqual(self.robot.executeCommand("MOVE"),True)
        self.assertEqual(self.robot.executeCommand("LEFT"),True)
        self.assertEqual(self.robot.executeCommand("MOVE"),True)
        



    

if __name__ == '__main__':
    unittest.main()