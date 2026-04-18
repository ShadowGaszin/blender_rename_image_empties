# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Gustaf Normann
#
# This file is part of Rename Image Empties.
#
# Rename Image Empties is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

bl_info = {
    "name": "Rename Image Empties",
    "author": "Gustaf Normann",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "3D Viewport > Sidebar (N-panel) & Object Menu",
    "description": "Quickly rename selected Image Empties to actual images' names",
    "category": "Object",
}

import bpy
from bpy.props import BoolProperty

# Allows the add-on to fully start after rechecking it via preferences without exiting them first
def update_keep_extension(self, context):
    pass

# Sidebar checkbox of extension saving
bpy.types.Scene.rename_image_keep_extension = BoolProperty(
    name="Keep Extension",
    description="Empties will be named as 'image.extension'",  # Tooltip on hover
    default=False,
    update=update_keep_extension
)

# Addon components
from . import operators, panels, menus

# List of operators/classes
classes = (
    operators.RenameImageEmptiesSidebarOperator,  # Sidebar operator
    operators.RenameImageEmptiesMenuOperator,    # Object operator
    panels.VIEW3D_PT_RenameImageEmpties,         # Sidebar UI
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    menus.register()
    panels.register()
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw()

def unregister():
    menus.unregister()
    panels.unregister()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    if hasattr(bpy.types.Scene, "rename_image_keep_extension"):
        del bpy.types.Scene.rename_image_keep_extension

if __name__ == "__main__":
    register()