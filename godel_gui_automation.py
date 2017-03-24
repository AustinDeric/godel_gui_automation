from ldtp import *
from ldtputils import *
import time
# import subprocess

#Launch the application
'''
roslaunch_location = '/opt/ros/kinetic/bin/roslaunch '
godel_package_location = '/home/aderic/godel_ws/src/godel/godel_robots/abb/godel_irb1200/godel_irb1200_support '
launch_file_location = '/home/aderic/godel_ws/src/godel/godel_robots/abb/godel_irb1200/godel_irb1200_support/launch '
args = 'real_pcd:=true pcd_location:=/home/aderic/godel_point_cloud_data/1490199847.795035265_input_cloud_1.pcd'
c = roslaunch_location + godel_package_location + launch_file_location + args
print('executing: ' + '\n')
print(c)
process = subprocess.Popen(c.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print('waiting 20 seconds')
time.sleep(20)
'''

# Admin gui automatation
'''
print('pressing `Scan and Find`')
click('irb1200_blending.rviz* -RViz', 'Scan and Find')
print('waiting 10 seconds')
time.sleep(10)
print('pressing `Select All`')
click('irb1200_blending.rviz* -RViz', 'Select All')
print('pressing `Generate Paths`')
click('irb1200_blending.rviz* -RViz', 'Generate Paths')
print('waiting 10 seconds')
time.sleep(10)
print('selecting edge')
click('irb1200_blending.rviz* -RViz', '1_edge_0')
'''

# Simple gui
while True:
    print("Scanning")
    click('irb1200_blending.rviz* -RViz', 'Next')
    print('waiting 10 seconds')
    time.sleep(10) #wait for robot scan

    print("Skipping Select Surfaces")
    click('irb1200_blending.rviz* -RViz', 'Next')
    print("Select All Surfaces and request plans")
    click('irb1200_blending.rviz* -RViz', 'Next')
    print('waiting 30 seconds')
    time.sleep(40) #wait for planning all surfaces

    print("Simulating all plans")
    click('irb1200_blending.rviz* -RViz', 'Next')
    print('waiting 20 seconds')
    time.sleep(40)#wait for simulation

    print("Executing All plans")
    click('irb1200_blending.rviz* -RViz', 'Next')
    print('waiting 60 seconds')
    time.sleep(40)#wait for simulation

    click('irb1200_blending.rviz* -RViz', 'Reset')
