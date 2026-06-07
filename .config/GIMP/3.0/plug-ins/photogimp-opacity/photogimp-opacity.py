#!/usr/bin/env python3
# Replicates Photoshop's number-key layer opacity behavior:
#   1 = 10%, 2 = 20%, ..., 9 = 90%, 0 = 100%

import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp, GLib
import sys

PROCEDURES = {
    'photogimp-set-opacity-1': 10.0,
    'photogimp-set-opacity-2': 20.0,
    'photogimp-set-opacity-3': 30.0,
    'photogimp-set-opacity-4': 40.0,
    'photogimp-set-opacity-5': 50.0,
    'photogimp-set-opacity-6': 60.0,
    'photogimp-set-opacity-7': 70.0,
    'photogimp-set-opacity-8': 80.0,
    'photogimp-set-opacity-9': 90.0,
    'photogimp-set-opacity-0': 100.0,
}


class PhotoGimpOpacity(Gimp.PlugIn):

    def do_query_procedures(self):
        return list(PROCEDURES.keys())

    def do_create_procedure(self, name):
        opacity = PROCEDURES[name]
        label = f'{int(opacity)}%'

        procedure = Gimp.ImageProcedure.new(
            self, name,
            Gimp.PDBProcType.PLUGIN,
            self.run, None
        )
        procedure.set_sensitivity_mask(Gimp.ProcedureSensitivityMask.DRAWABLE)
        procedure.set_menu_label(f'Layer Opacity {label}')
        procedure.set_documentation(
            f'Set active layer opacity to {label}',
            f'Sets the opacity of the active layer to {label}.',
            name
        )
        procedure.set_attribution('PhotoGIMP', 'PhotoGIMP', '2025')
        procedure.add_menu_path('<Image>/Filters/PhotoGIMP')
        return procedure

    def run(self, procedure, run_mode, image, drawables, config, run_data):
        opacity = PROCEDURES.get(procedure.get_name(), 100.0)

        layer = image.get_active_drawable()
        if layer is None:
            return procedure.new_return_values(
                Gimp.PDBStatusType.EXECUTION_ERROR,
                GLib.Error()
            )

        layer.set_opacity(opacity)
        Gimp.displays_flush()

        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())


Gimp.main(PhotoGimpOpacity.__gtype__, sys.argv)
