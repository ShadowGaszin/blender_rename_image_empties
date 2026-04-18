# SPDX-License-Identifier: GPL-3.0-or-later
# Part of Rename Image Empties add-on. See __init__.py for license.

import bpy

# Sidebar
class RenameImageEmptiesSidebarOperator(bpy.types.Operator):
    """Rename Image Empties"""  # Tooltip
    bl_idname = "object.rename_image_empties_sidebar"  # identifier
    bl_label = "Rename Image Empties"
    bl_options = {'REGISTER', 'UNDO'}  # Adds to undo stack and shows in search
    
    def execute(self, context):
        # Report of the number of empties renamed
        renamed_count = 0
        # Checks if extensions are to be kept
        keep_extension = context.scene.rename_image_keep_extension
        
        # Loop through selections
        for obj in context.selected_objects:
            # Check if object is an IMAGE Empty
            if obj.type == 'EMPTY' and obj.empty_display_type == 'IMAGE':
                # Get the image data
                img = obj.data
                if img and img.name:
                    # Checks the checkbox
                    if keep_extension:
                        # Keep full filename including extension ("image.png")
                        new_name = img.name
                    else:
                        # Strip all but the name ("image.png" → "image")
                        new_name = img.name.rsplit('.', 1)[0]
                    # Renames
                    obj.name = new_name
                    renamed_count += 1
        
        # Report
        self.report({'INFO'}, f"Renamed {renamed_count} Image Empties")
        return {'FINISHED'}

# Object menu
class RenameImageEmptiesMenuOperator(bpy.types.Operator):
    """Rename Image Empties""" # Tooltip
    bl_idname = "object.rename_image_empties_menu"
    bl_label = "Rename Image Empties"
    bl_options = {'REGISTER', 'UNDO'}
    
    # F9
    keep_extension: bpy.props.BoolProperty(
        name="Keep Extension",
        description="Keep file extension in the object name (e.g., 'image.png' instead of 'image')",
        default=False,
    )
    
    def execute(self, context):
        renamed_count = 0
        
        for obj in context.selected_objects:
            if obj.type == 'EMPTY' and obj.empty_display_type == 'IMAGE':
                img = obj.data
                if img and img.name:
                    if self.keep_extension:
                        new_name = img.name
                    else:
                        new_name = img.name.rsplit('.', 1)[0]
                    obj.name = new_name
                    renamed_count += 1
        
        self.report({'INFO'}, f"Renamed {renamed_count} Image Empties")
        return {'FINISHED'}
    
    def invoke(self, context, event):
        return self.execute(context)