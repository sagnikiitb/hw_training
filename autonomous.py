#!/usr/bin/env python

from roboclaw import RoboClaw
import rospy

#---------------------------------------------------- 

class Drive:
    def __init__(self,driver1,driver2):
        self.rightClaw = driver1
        self.leftClaw = driver2
         

    def drive_callback(self,inp):
        # A bit of help! These are arrays of data
        axes = inp.axes
        buttons = inp.buttons
        
        if(axes[1] > 0):
            ForwardM1(self,100)
            ForwardM2(self,100)
        elif(axes[1] <0):
            BackwardM1(self,100)
            BackwardM2(self,100)
            
        if(axes[0] > 0):
            TurnLeftMixed(self,100)
        elif(axes[0] < 0):
            TurnRIghtMixes(self,100)
            

        

    def current_limiter(self):
        """BONUS: 

        Try to implement this function as well. It is a saftey feature. 
        How would you decide the current threshold? - Please elaborate
        """
        return False
                

#---------------------------------------------------                



