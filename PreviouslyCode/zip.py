import os
import time

source = ["/Users/Broccoli/Documents/Python", "/Users/Broccoli/Documents/info.text"]

target_dir = '/Users/Broccoli/Desktop/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'Succeessful backup to', target
else:
    print 'Backup FAILED'
