#!/usr/bin/python
# -*- coding: utf-8 -*- 
import time, os
import sys, subprocess, platform
##---------------##
## import shutil ##
##---------------##

def ProgressBar(items, decimal=2, wait=0.05):
    """
    Desc : Create a progress bar with dynamic size
    Goal : Always fits within current terminal (at time of usage)
    Reqs : time, os, sys, subprocess [deprecated: shutil]
    ----------
    Parameters
    ----------
    (int)  items   : REQUIRED - items to be iterated on
    (int)  decimal : OPTIONAL - Number of decimal places 
    (float) wait    : OPTIONAL - time to sleep (pseudo-loading)
    """

    ## Below is deprecated but still can be used for user's own convenience ##
    ##----------------------------------------------------------------------##
    ## length = os.popen('stty size', 'r').read().split()[1]                ##
    ## length = shutil.get_terminal_size((80, 20))[0] - 30                  ##
    ##----------------------------------------------------------------------##

    ## Build the variables ##
    if platform.system() == 'Windows':
        from con_size import csize
        length = csize()    
    else:
        length = subprocess.check_output(['stty', 'size']).split()[1]   
    fill = "█"
    finish = len(items)
    length = int(length) - 30

    ## Construct the initial progress bar ##
    percent = ("{0:." + str(decimal) + "f}").format(100 * (0 / float(finish)))
    rest = int(length * 0 // finish)
    progress_bar = fill * rest + '-' * (length - rest)
    sys.stdout.write("\r{0} |{1}| {2}% {3}\r".format("Status:", progress_bar, percent, "Done"))

    ## Updating progress bar ##
    for i in range(finish+1):
        percent = ("{0:." + str(decimal) + "f}").format(100 * (i / float(finish)))
        rest = int(length * i // finish)
        progress_bar = fill * rest + '-' * (length - rest)
        sys.stdout.write("\r{0} |{1}| {2}% {3}\r".format("Status:", progress_bar, percent, "Done"))
        sys.stdout.flush()
        time.sleep(wait)

    ## End with newline ##
    if sys.version_info < (3, 0):
        print
    else:
        print()

##============TESTING============##
## items = list(range(0, 67))    ##
## ProgressBar(items)            ##
##============TESTING============##
