# SPDX-License-Identifier: GPL-3.0-or-later
# Part of Rename Image Empties add-on. See __init__.py for license.

import bpy

def menu_func(self, context):
    self.layout.operator("object.rename_image_empties_menu")

def register():
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_func)