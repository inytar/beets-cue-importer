# This is an extension to beets
# MIT license

"""Allows cue files to be imported: cue files are copied to a specific folder, the filenames are changed to filenames in your collection
"""

from beets.plugins import BeetsPlugin
from beets import library
from beets.ui import Subcommand

cue-importer_command = Subcommand('importcue', help='import cue files, give a folder or cue file') # how do make it so you have to add a folder/file
def fileLoader(load_path):
    if load_path ==# FIXME is folder
        cue_list = # FIXME make an array containing all cue files
    else:
        cue_list = load_path

def (cue_file):
    open cue_file
    total_tracks == # FIXME find the last TRACK ?? AUDIO and insert ??
    for album in lib.albums('tracktotal:'total_tracks): # what to put in the tracks
        album_ids += album.album_id # FIXME make array with album ids, not correct syntax
        album_list += (album.albumartist + u' - ' + album.album)

def cueEditor(cue_file, album_id, new_path):
    open cue_file
    track_num = 1
    for line in cue_file: # fix really read line by line...
        if line = :# starts with FILE and end with or WAVE or MP3
            lib.items('album_id:'album_id 'track:'track_num)
                new_filename = newpath'/'print_(self.filename) #FIXME does a function filename exist?
            # replace everything between FILE and WAVE or MP3 with new_filename
            track_num++
    return new_cue_file

def SaveCue(new_cue_file, save_path):
    
    

class cueImporterPlugin(BeetsPlugin):
    def configure(self, config):
        save_path = beets.ui.config_val(config, 'cueimporter', 'path', '')
    def commands(self):
        return [cue-importer_command]
