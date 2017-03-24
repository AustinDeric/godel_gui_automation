from ldtp import *
from ldtputils import *
import time
import subprocess

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
print('pressing `Scan and Find`')
click('irb1200_blending.rviz* -RViz', 'Scan and Find')
print('waiting 20 seconds')
time.sleep(20)
print('pressing `Select All`')
click('irb1200_blending.rviz* -RViz', 'Select All')
print('pressing `Generate Paths`')
click('irb1200_blending.rviz* -RViz', 'Generate Paths')
print('waiting 20 seconds')
time.sleep(20)
print('waiting 20 seconds')
activatetext('irb1200_blending.rviz* -RViz', '1_edge_0')

# Simple gui
# click('irb1200_blending.rviz* -RViz', 'Next' )
