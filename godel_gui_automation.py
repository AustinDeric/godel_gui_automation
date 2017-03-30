from ldtp import *
import time

window_name = 'irb1200_blending.rviz* -RViz'
sleep_time = 1

def click_next():
    click(window_name, 'Next')

def sleep():
    time.sleep(sleep_time)

while True:
    try:
        click_next()
    except LdtpExecutionError:
        sleep()
    else:
        sleep()

