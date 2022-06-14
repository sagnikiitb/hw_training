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

        """TODO - INSERT YOUR CODE HERE
        
        Problem Statement: Insert Code here to make the rover move 
        forwards, backwards, left, right according to input given
        """
        

    def current_limiter(self):
        """BONUS: 

        Try to implement this function as well. It is a saftey feature. 
        How would you decide the current threshold? - Please elaborate
        """
        return False
                

#---------------------------------------------------                



