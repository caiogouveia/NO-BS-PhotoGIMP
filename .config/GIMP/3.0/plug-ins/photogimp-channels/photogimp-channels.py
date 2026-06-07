#!/usr/bin/env python3
# Replicates Photoshop's channel view shortcuts:
#   Ctrl+~ = composite (all channels)
#   Ctrl+1 = Red channel only
#   Ctrl+2 = Green channel only
#   Ctrl+3 = Blue channel only

import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp, GLib
import sys

# (procedure-name, channels-visible: [R, G, B])
PROCEDURES = {
    'photogimp-view-channel-composite': (True,  True,  True),
    'photogimp-view-channel-red':       (True,  False, False),
    'photogimp-view-channel-green':     (False, True,  False),
    'photogimp-view-channel-blue':      (False, False, True),
}

LABELS = {
    'photogimp-view-channel-composite': 'View Composite (RGB)',
    'photogimp-view-channel-red':       'View Red Channel',
    'photogimp-view-channel-green':     'View Green Channel',
    'photogimp-view-channel-blue':      'View Blue Channel',
}


class PhotoGimpChannels(Gimp.PlugIn):

    def do_query_procedures(self):
        return list(PROCEDURES.keys())

    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(
            self, name,
            Gimp.PDBProcType.PLUGIN,
            self.run, None
        )
        procedure.set_sensitivity_mask(Gimp.ProcedureSensitivityMask.DRAWABLE)
        procedure.set_menu_label(LABELS[name])
        procedure.set_documentation(
            LABELS[name],
            LABELS[name],
            name
        )
        procedure.set_attribution('PhotoGIMP', 'PhotoGIMP', '2025')
        procedure.add_menu_path('<Image>/Filters/PhotoGIMP')
        return procedure

    def run(self, procedure, run_mode, image, drawables, config, run_data):
        channels = PROCEDURES.get(procedure.get_name())
        if channels is None:
            return procedure.new_return_values(
                Gimp.PDBStatusType.EXECUTION_ERROR,
                GLib.Error()
            )

        r, g, b = channels
        image.set_component_visible(Gimp.ChannelType.RED,   r)
        image.set_component_visible(Gimp.ChannelType.GREEN, g)
        image.set_component_visible(Gimp.ChannelType.BLUE,  b)
        Gimp.displays_flush()

        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())


Gimp.main(PhotoGimpChannels.__gtype__, sys.argv)
