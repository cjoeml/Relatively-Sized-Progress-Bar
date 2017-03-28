import time
import shutil
##-----------##
## import os ##
##-----------##

def ProgressBar(items, decimal=2, sleep=0.05):
	"""
	Desc : Create a progress bar with dynamic size
	Goal : Always fits within current terminal (at time of usage)
	Reqs : time, shutil [os (deprecated)]
	----------
	Parameters
	----------
	(int) items   : REQUIRED - items to be iterated on
	(int) decimal : OPTIONAL - Number of decimal places 
	(float) wait  : OPTIONAL - time to sleep (pseudo-loading)
	"""

	## Below is deprecated but still can be used for user's own convenience ##
	##----------------------------------------------------------------------##
	## r, length = os.popen('stty size', 'r').read().split()			    ##
	## r, length = subprocess.check_output(['stty', 'size']).split()		##
	##----------------------------------------------------------------------##

	## Build the variables ##
	length = shutil.get_terminal_size((80, 20))[0] - 30
	fill = "█"
	finish = len(items)

	## Construct the initial progress bar ##
	percent = ("{0:." + str(decimal) + "f}").format(100 * (0 / float(finish)))
	rest = int(length * 0 // finish)
	progress_bar = fill * rest + '-' * (length - rest)
	print("\r{0} |{1}| {2}% {3}".format("Status:", progress_bar, percent, "Done"), end='\r')

	## Updating progress bar ##
	for i in range(finish+1):
			percent = ("{0:." + str(decimal) + "f}").format(100 * (i / float(finish)))
			rest = int(length * i // finish)
			progress_bar = fill * rest + '-' * (length - rest)
			print("\r{0} |{1}| {2}% {3}".format("Status:", progress_bar, percent, "Done"), end='\r')
			time.sleep(sleep)

	## End with newline ##
	print()

##============TESTING============##
## items = list(range(0, 67))	 ##
## ProgressBar(items)			 ##
##============TESTING============##
