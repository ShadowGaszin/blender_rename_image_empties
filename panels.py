# SPDX-License-Identifier: GPL-3.0-or-later
# Part of Rename Image Empties add-on. See __init__.py for license.

import bpy

# Defines UI
class VIEW3D_PT_RenameImageEmpties(bpy.types.Panel):
    bl_label = "Rename Image Empties"  # Header text of the panel
    bl_idname = "VIEW3D_PT_rename_image_empties"  # identifier
    bl_space_type = 'VIEW_3D'  # Where it appears
    bl_region_type = 'UI'  # Region
    bl_category = "Image Empties"  # Creates its own tab in sidebar
    
    # UI
    def draw(self, context):
        layout = self.layout
        
        # Add the sidebar operator button (executes immediately)
        layout.operator("object.rename_image_empties_sidebar")
        
        # Adds checkbox below the rename button
        layout.prop(context.scene, "rename_image_keep_extension")

def register():
    pass

def unregister():
    pass