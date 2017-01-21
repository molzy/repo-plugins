# #!/usr/bin/env python
# # -*- coding: UTF-8 -*-

#
# Imports
#
import os
import re
import sys
import urllib
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

LIB_DIR = xbmc.translatePath( os.path.join( xbmcaddon.Addon(id='plugin.video.botchamania').getAddonInfo('path'), 'resources', 'lib' ) )
sys.path.append (LIB_DIR)

from botchamania_const import ADDON, SETTINGS, LANGUAGE, IMAGES_PATH, DATE, VERSION

# Parse parameters...
if len(sys.argv[2]) == 0:
    #
    # Main menu
    #
    xbmc.log("[ADDON] %s, Python Version %s" % (ADDON, str(sys.version)), xbmc.LOGDEBUG)
    xbmc.log( "[ADDON] %s v%s (%s) is starting, ARGV = %s" % ( ADDON, VERSION, DATE, repr(sys.argv) ), xbmc.LOGDEBUG )
    import botchamania_main as plugin
else:
    action = urlparse.parse_qs(urlparse.urlparse(sys.argv[2]).query)['action'][0]
    #
    # archive
    #
    if action == 'list-archive':
        import botchamania_list_archive as plugin
    #
    # archive specials
    #
    if action == 'list-archive-specials':
        import botchamania_list_archive_specials as plugin
    #
    # List
    #
    elif action == 'list':
        import botchamania_list as plugin
    #
    # Play
    #
    elif action == 'play':
        import botchamania_play as plugin

plugin.Main()