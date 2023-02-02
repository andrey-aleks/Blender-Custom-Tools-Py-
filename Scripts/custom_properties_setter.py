bl_info = {
    "name": "Custom Properties Setter",
    "version": (1, 0, 1),
    "blender": (3, 3, 0),
    "author": "Andrey Alekseev",
    "location": "3D-viewport -> N-panel -> Tool -> CP Setter",
    "description": "Allows you to set custom properties with a few clicks",
    "category": "Object",
}
import bpy


class CP_Setter_OT(bpy.types.Operator):
    bl_idname = 'mesh.cp_setter'
    bl_label = "CP Setter"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        objects = bpy.context.selected_objects
        for obj in objects:
            # Add fbx_type = LodGroup
            if context.scene.lod:
                try:
                    obj["fbx_type"]
                except KeyError:
                    var_exists = False
                else:
                    var_exists = True
                if not var_exists:
                    obj["fbx_type"] = str('LodGroup')
        return {'FINISHED'}


# UI panel
class VIEW3D_PT_CP_Setter(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'
    bl_label = 'CP Setter'

    def draw(self, context):
        col = self.layout.column()

        col.prop(bpy.context.scene, 'lod')
        col.operator('mesh.cp_setter', text='Add custom properties')


##

blender_classes = [
    CP_Setter_OT,
    VIEW3D_PT_CP_Setter,
]


##

def register():
    for blender_class in blender_classes:
        bpy.utils.register_class(blender_class)

    bpy.types.Scene.lod = bpy.props.BoolProperty(name="fbx_type = LodGroup")


def unregister():
    for blender_class in blender_classes:
        bpy.utils.unregister_class(blender_class)

    del bpy.types.Scene.lod
