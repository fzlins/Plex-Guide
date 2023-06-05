# -*- coding: utf-8-sig -*-'

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
plexmatchFilename = '.plexmatch'
plexmatchFilePath = os.path.join(directory, plexmatchFilename)

if os.path.exists(plexmatchFilePath):
    if (args.overwrite):
        os.remove(plexmatchFilePath)
    else:
        quit()

from natsort import os_sorted
filelist = os_sorted(os.listdir(directory))
video_exts = ['3g2', '3gp', 'asf', 'asx', 'avc', 'avi', 'avs', 'bivx', 'bup', 'divx', 'dv', 'dvr-ms', 'evo', 'fli', 'flv',
              'm2t', 'm2ts', 'm2v', 'm4v', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'mts', 'nsv', 'nuv', 'ogm', 'ogv', 'tp',
              'pva', 'qt', 'rm', 'rmvb', 'sdp', 'svq3', 'strm', 'ts', 'ty', 'vdr', 'viv', 'vob', 'vp3', 'wmv', 'wtv', 'xsp', 'xvid', 'webm']

skip_files = [plexmatchFilename, '[SP]', '[MENU]']
filelist = list(filter(lambda x: not any(map(x.__contains__, skip_files)) and os.path.isfile(os.path.join(directory, x)) and x.rsplit('.', 1)[-1] in video_exts, filelist))

commonprefix = os.path.commonprefix(filelist)
def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

with open(plexmatchFilePath,"a+") as f:
    print("# Regular episodes with tricky filenames", file=f)
    season_number = 1
    if (args.season):
        season_number = args.season

    index = 1
    for filename in filelist:
        ep = re.search(r'\d{2,3}', remove_prefix(filename, commonprefix)).group()
        if (args.order and index != int(ep)):
            if int(ep) == 1:
                season_number = season_number + 1
                index = 1
            else:    
                continue

        index = index + 1
        line = f"ep: S{season_number}E{ep}: {filename}"
        #print(line)
        print(line, file=f)
