import sys
import os
import re
found = False

def search(patt , val):
    sr = re.search(patt,val , re.I)
    if  sr :
        return True
    else :
        return False

def locate(dirname,obj):
    global found
    for dir , subdir , files in os.walk(dirname) :
        for file in files :
            if search(obj,file) :
                print os.path.join(dir,file)
                found = True
        for subdr in subdir :
            if search(obj,subdr) :
                print os.path.join(dir,subdr)
                found = True
                

def locate_fast(dirname ,obj):
    global found
    subdirlist = []
    for item in os.listdir(dirname) :
        if search(obj,item) :
            print os.path.join(dirname,item)
            found = True
        else :
            if not os.path.isfile(os.path.join(dirname,item)):
                subdirlist.append(os.path.join(dirname , item))
    for subdir in subdirlist :
        locate(subdir , obj)
                
        
if __name__== "__main__":
    if len(sys.argv) == 3:
        print len(sys.argv)
        fname=str(sys.argv[1])
        option = str(sys.argv[2])
    else :
        raw_input('Please provide valid inputs next time')
        exit()
    if option.upper() == 'FAST' :
        dirname = str(raw_input('Enter the name of directory where to search : '))
        print '*********************************'
        print '\n\n\n\n'
        locate_fast(dirname , fname)
        print '\n\n\n\n'
        print '*********************************'
    else :
        dirname = str(raw_input('Enter the name of directory where to search : '))
        print '*********************************'
        print '\n\n\n\n'
        locate(dirname , fname)
        print '\n\n\n\n'
        print '*********************************'
    if not found :
        print '\n\n'
        print 'File not found in this space'
    print '\n\n'
    raw_input('Press Enter to exit ...')
    
