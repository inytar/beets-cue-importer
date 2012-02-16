# This is an extension to beets
# MIT license

"""Allows cue files to be imported: cue files are copied to a specific folder, the filenames are changed to filenames in your collection
"""

from beets.plugins import BeetsPlugin
from beets import library



class cue-importer(BeetsPlugin):
    def configure(self, config):
        save_path = beets.ui.config_val(config, 'cueimporter', 'path', '')
