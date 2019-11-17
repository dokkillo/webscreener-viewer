import sys
import os
import subprocess
from os import walk

def CreateHtml(files, folder):
    f = open( folder + '/webscreen.html','w')
    start = """<html><head></head><body>"""
    end ="""</body></html>"""
    message =""""""
    for img in  files:  
        url = FormatUrl(img)
        message += """<a href='""" + url +"""' target='_blank'> <img src='""" + img + """' height="300" width="300"/></a>"""
        print "added %s" %img

    f.write(start)
    f.write(message)
    f.write(end)
    f.close()

def FormatUrl(file):
    file = file.replace('http_', 'http://')
    file = file.replace('https_', 'https://')
    file = file.replace('_80.png', '')
    file = file.replace('_443.png', '')
    return file



def GetFiles(folder):
    f = []
    for (dirpath, dirnames, filenames) in walk(folder):
        f.extend(filenames)
        break
    return f


def main():
    if len(sys.argv) != 2:
        print ('[+] usage: <folder>')       
        sys.exit(-1)

    folder = sys.argv[1]
    files =GetFiles(folder)
    CreateHtml(files,folder)
    print ('[+] Task finished')       


if __name__ == "__main__":     
    main()