bl_info = {
    "name": "ToFlat",
    "author": "NorthForge",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "View3D",
    "description": "Allows you to switch the view to see the silhouette of the model, and switch the view back Usage: Object->ToFlat",
    "warning": "",
    "category": "3DView",
}

import bpy

class ToFlat(bpy.types.Operator):
    
    ToFlatmLight ='FLAT'
    ToFlatmColorType = 'SINGLE'
    
    bl_idname = "shading.light"
    bl_label = "ToFlat"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        global ToFlatmLight
        global ToFlatmColorType
        my_areas = bpy.context.workspace.screens[0].areas
        for area in my_areas:
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    if space.shading.light != 'FLAT':
                        ToFlatmLight = space.shading.light
                        ToFlatmColorType = space.shading.color_type
                        space.shading.light = 'FLAT'
                        space.shading.color_type = 'SINGLE'
                        space.shading.single_color = (0,0,0)
                        return {'FINISHED'} 
                    else:
                        space.shading.light = ToFlatmLight
                        space.shading.color_type = ToFlatmColorType
        return {'FINISHED'}     
    
def menu_func(self, context):
    self.layout.operator(ToFlat.bl_idname)     

def register():
    bpy.utils.register_class(ToFlat)
    bpy.types.VIEW3D_MT_object.append(menu_func)

def unregister():
    bpy.utils.unregister_class(ToFlat)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
