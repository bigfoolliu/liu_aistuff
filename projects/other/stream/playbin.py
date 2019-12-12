#!/usr/bin/env python3
#
# Plays a file to screen.
#
# Make sure the environment variable SRC is set to a playable file
# e.g.
#   export SRC='/tmp/me.mp4'
#

import gi
import os

gi.require_version('Gst', '1.0')

from gi.repository import GObject, Gst
import os

Gst.init(None)
mainloop = GObject.MainLoop()

video_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos/input.mp4")
print(video_path)

pipeline = Gst.ElementFactory.make("playbin", "player")
pipeline.set_property('uri', 'file://' + video_path)

pipeline.set_state(Gst.State.PLAYING)
mainloop.run()
