from djitellopy import Tello
import pygame
from pygame.locals import *

pygame.init()

joystick = pygame.joystick.Joystick(0)
tello = Tello()
tello.connect()
tello.takeoff()
print(tello.get_battery())

while True:
    for event in pygame.event.get(): # get the events (update the joystick)
        if event.type == QUIT: # allow to click on the X button to close the window
            pygame.quit()
            exit()
        horizontal = round(joystick.get_axis(0)*100)
        if horizontal <=5 and horizontal >= -5:
            horizontal = 0
        vertical = (-1)*round(joystick.get_axis(1)*100)
        if vertical <=5 and vertical >= -5:
            vertical = 0

        if joystick.get_button(0):
            #print("A")
            tello.move_down(100)
        elif joystick.get_button(1):
            tello.land()
            #print("B")
            
        elif joystick.get_button(2):
            #print("X")
            tello.takeoff()
        elif joystick.get_button(3):
            #print("Y")
            tello.move_up(100)
        tello.send_rc_control(left_right_velocity=horizontal , forward_backward_velocity= vertical ,up_down_velocity=0 , yaw_velocity=0)


