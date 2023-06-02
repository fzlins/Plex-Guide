# python -m Plexmatch -d 'C:\directory -o'
# python -m Plexmatch -d '//Network\directory -o'

import os
import re
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-d", "--directory", help="Specify a directory.", required=True)
parser.add_argument("-o", "--order", action='store_true', help="Select only ordered files.")
parser.add_argument("-ow", "--overwrite", action='store_true', help="Overwirte .plexmatch file.")
parser.add_argument("-s", "--season", help="Specify a season number.")
args = parser.parse_args()
directory = args.directory

video_exts = ['3g2', '3gp', 'asf', 'asx', 'avc', 'avi', 'avs', 'bivx', 'bup', 'divx', 'dv', 'dvr-ms', 'evo', 'fli', 'flv',
              'm2t', 'm2ts', 'm2v', 'm4v', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'mts', 'nsv', 'nuv', 'ogm', 'ogv', 'tp',
              'pva', 'qt', 'rm', 'rmvb', 'sdp', 'svq3', 'strm', 'ts', 'ty', 'vdr', 'viv', 'vob', 'vp3', 'wmv', 'wtv', 'xsp', 'xvid', 'webm']


plexmatchFilename = '.plexmatch'
plexmatchFilePath = os.path.join(directory, plexmatchFilename)

if os.path.exists(plexmatchFilePath):
    if (args.overwrite):
        os.remove(plexmatchFilePath)
    else:
        quit()
    
with open(plexmatchFilePath,"a+", encoding="utf-8-sig") as f:
    print("# Regular episodes with tricky filenames", file=f)
    season_number = '01'
    if (args.season):
        season_number = args.season

    index = 1
    for filename in os.listdir(directory):
        if filename == plexmatchFilename:
            continue
        
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            file_extension = filename.rsplit('.', 1)
            if file_extension[-1] in video_exts:
                ep = re.search(r'\d{2,3}', filename).group()
                if (args.order and index != int(ep)):
                    continue

                index = index + 1
                line = f"ep: S{season_number}E{ep}: {filename}"
                #print(line)
                print(line, file=f)
