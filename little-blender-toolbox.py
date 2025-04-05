import bpy
import os

class LittleBlenderToolbox(bpy.types.Panel):
    bl_label = "lil' Toolbox"
    bl_idname = "VIEW3D_PT_little_blender_toolbox"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = '🧩 lil Tooly'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        layout.label(text="Hello there goblin/angel s?")
        
        row = layout.row()
        row.operator("liltooly.remove_unused_materials", text="Remove Unused Materials", icon='GHOST_DISABLED')

class RemoveUnusedMaterials(bpy.types.Operator):
    bl_idname = "liltooly.remove_unused_materials"
    bl_label = "Remove Unused Textures"

    # This is the core of the operator. It contains the code that runs when the operator is invoked. 
    # The return value should be {'FINISHED'} when the operation completes successfully. 
    # If there is an error, you can return {'CANCELLED'}.
    def execute(self, context):
        for mat in bpy.data.materials:
            if mat.users == 0:
                bpy.data.materials.remove(mat)
        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(LittleBlenderToolbox)
    bpy.utils.register_class(RemoveUnusedMaterials)

def unregister():
    bpy.utils.unregister_class(LittleBlenderToolbox)
    bpy.utils.unregister_class(RemoveUnusedMaterials)

if __name__ == "__main__":
    register()
