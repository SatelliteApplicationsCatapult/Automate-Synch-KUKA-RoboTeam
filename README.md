# Automate-Synch-KUKA-RoboTeam
This is to modify an existing KUKA program to make both robots work in synchronisation. <br>
The code needs to be run for the program of BOTH robots, for the DAT and SRC file. <br>
This is useful when you have more than 10 points in the KUKA program for the robots to execute in synchronisation. <br>
<br>
MotionSynchSRC.py is for the src file <br>
MotionSynchDAT.py is for the dat file. But you need to convert the dat file as a txt type first. <br>
<br>
# Important information:
The POINTS NEED TO BE DEFINED AS SLIN for the program to work and for Synch to work!!!!!!!! <br>
Points should be named ONLY BY NUMBERS IN ASCENDING ORDER!!!!!!! E.g: 1, 2, 3, ... 800 <br>
This program will go through each point declared. <br>
You need to do this for BOTH Robot program that will work in synch <br>
Make sure to give the generated src and dat file the same name. <br>
<br>
# 1 - MotionSynchSRC.py
This code is to use on a SRC file. <br>
1-Enter the correct path file and path output with a new name. <br>
2-Run the program. <br>
<br>
<br>
# 2 - MotionSynchDAT.py
This code is to use on a txt file. <br>
1-Convert the dat file to a txt type. <br>
2-Enter the correct path file and path output with a new name. <br>
3-Run the program. <br>
4-Rename the generated file to be of type .dat <br>
<br>
