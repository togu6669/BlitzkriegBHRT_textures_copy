#!/usr/local/bin/python2.7
# encoding: utf-8
'''
BlitzkriegBHRT_texture_copy copies the *_h.dds textures to the *_c.dds textures
if they are missing. This solves the black and white checkerboards instead of
the unit sprites.

Usage: BlitzkriegBHRT_texture_copy Path_To_The_Data_Folder


@author:    togu6669
@email:     togu6669@gmail.com

@disclaimer: this code is offered “as-is”, without warranty, and disclaiming
liability for damages resulting from using this project.

'''
import sys
import os.path

from shutil import copyfile
from _tracemalloc import stop


def main():

    try:
        if len (sys.argv) < 1:
            print('No textures path has been given in the command line!')
            return stop

        topdir = sys.argv[1]

        # The extension to search for
        exten = '.dds'
        logname = 'findfiletype.log'

        # What will be logged
        results = str()
        if not os.path.exists(topdir):
            print('path "%s" does not exist' % topdir)
            return stop

        if not os.path.isdir(topdir):
            print('path "%s" is not a directory' % topdir)
            return stop

        count = 0
        for dirpath, dirnames, files in os.walk(topdir):
            for name in files:
                if name.lower().endswith(exten):
                    # Save to results string instead of printing
                    if "_h" in name:
                        cname = name.replace ("_h", "_c")
                        srcdirfile = os.path.join(dirpath, name)
                        destdirfile = os.path.join(dirpath, cname)
                        if not os.path.isfile(destdirfile):
                            count += 1
                            copyfile(srcdirfile, destdirfile)
                            results += '%s\n' % destdirfile

        # Write results to logfile
        logifiledir = os.path.join(topdir, logname)
        with open(logifiledir, 'w') as logfile:
            logfile.write(results)

        print('Done, %s files have been copied' % count)
        return 0

    except Exception as e:
        print ('Exception %s occurred.' % str (e) )
        return 2
    
sys.exit(main())

