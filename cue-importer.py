# This is an extension to beets
# MIT license

"""Allows cue files to be imported: cue files are copied to a specific folder, the filenames are changed to filenames in your collection
"""

from beets.plugins import BeetsPlugin
from beets import library
from beets.ui import Subcommand

cue-importer_command = Subcommand('importcue', help='import cue files, give a folder or cue file') # how do make it so you have to add a folder/file
def cueimporter(path=):
    if path :# is folder
        cueList = # make an array containing all cue files
    else:
        cueList = path
    for cueFile in cueList:
        open cueFile
        totalTracks = # find the last TRACK ?? AUDIO and insert ??
        # do a query to the library and find all albums with totalTracks totaltracks, not clear how I should do a library query

class cueImporterPlugin(BeetsPlugin):
    def configure(self, config):
        save_path = beets.ui.config_val(config, 'cueimporter', 'path', '')
    def commands(self):
        return [cue-importer_command]
