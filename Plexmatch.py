# python -m plexmatch -d 'C:\directory'
# python -m plexmatch -d '//Network\directory'
import os
import re
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-d", "--directory", help="specific a directory", metavar="Directory", required=True)
args = parser.parse_args()
directory = args.directory

video_exts = ['3g2', '3gp', 'asf', 'asx', 'avc', 'avi', 'avs', 'bivx', 'bup', 'divx', 'dv', 'dvr-ms', 'evo', 'fli', 'flv',
              'm2t', 'm2ts', 'm2v', 'm4v', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'mts', 'nsv', 'nuv', 'ogm', 'ogv', 'tp',
              'pva', 'qt', 'rm', 'rmvb', 'sdp', 'svq3', 'strm', 'ts', 'ty', 'vdr', 'viv', 'vob', 'vp3', 'wmv', 'wtv', 'xsp', 'xvid', 'webm']


plexmatchFilename = '.plexmatch'
plexmatchFilePath = os.path.join(directory, plexmatchFilename)

if os.path.exists(plexmatchFilePath):
    os.remove(plexmatchFilePath)
    
with open(plexmatchFilePath,"a+", encoding="utf-8-sig") as f:
    index = 1
    for filename in os.listdir(directory):
        if filename == plexmatchFilename:
            continue
        
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_extension = filename.rsplit('.', 1)
            if file_extension[-1] in video_exts:
                ep = re.search(r'\d+', filename).group()
                if (index == int(ep)):
                    index = index + 1
                    line = "ep: " + ep + ": " +filename
                    print(line)
                    print(line, file=f)
