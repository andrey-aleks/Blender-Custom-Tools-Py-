# Blender Custom Tools
Custom tools (addons) for Blender3D
***
## [Custom Properties Setter](https://github.com/andrey-aleks/Blender_Custom_Tools/blob/master/Scripts/custom_properties_setter.py)
This addon adds a button for simple setting of custom properties to objects.
### How to Use
The tool location in Blender: 3D Viewport → N-panel → CP Setter, here you can find a list of available to set properties as well as a button “Add custom properties” (Figure 1).

![image](https://user-images.githubusercontent.com/58087965/217100270-d9080da5-ab57-4131-8540-ab513f5423e3.png)

Figure 1 - Addon panel

1. Select the objects that you want to add properties to.
2. Enable the necessary custom properties that you want to add by clicking on the checkboxes in the addon panel (Figure 1).
3. Click the button “Add custom properties”.
4. Check the result in the Object Properties panel → Custom Properties (Figure 2).

![image](https://user-images.githubusercontent.com/58087965/217101730-fd6b87dd-a8fe-4b81-94ae-fd69d3d01ae5.png)

Figure 2 - Added custom properties

The following properties are now available:

**fbx_type = LodGroup** - mark with this property a parent object for LODs for importing LODs to Unreal Engine  
***
## [Bones constraints autosetter](https://github.com/andrey-aleks/Blender_Custom_Tools/blob/master/Scripts/bones_constraints_autosetter_addon.py)
This tool helps animators to simple bones setup in Blender. When you copypaste default rig from other file, bones constraint’s “Target” become empty, so you have to manually setup all bones constraints targets for futher rig using. 

This tool setups all these “Target” at one click.   
### How to Use
The tool location in Blender: Viewport → N-panel → Tool → (Figure 1).

![image](https://user-images.githubusercontent.com/58087965/217102153-6aada0db-3b6c-4cb5-a0e0-0f70d07e60c7.png)

Figure 1 - Addon panel

There must be 2 ready rigs in the project: source (which you want to use as “Target” object) and target (new, where you want to assign new “Target”). 

Open panel with this tool, then select in outliner new rig that you want to setup.

Go back to tool and click to the empty field “Source Rig Object” and select source rig, which you want to assign as “Target” to selected rig (Figure 2).

![image](https://user-images.githubusercontent.com/58087965/217102298-73d54cb8-9d77-4a1b-b6ad-abc2ebd7b8cf.png)

Figure 2 - Source Rig Object setup

If you want to replace all Targets in the current selected rig with Source Rig Object, enable “Force Set” beneath Source Rig Object, otherwise keep it as false.

Click “Set Target”.

Enjoy the result (Figure 3).

![image](https://user-images.githubusercontent.com/58087965/217102351-176b5689-8912-4140-92ff-63bb035a219b.png)

Figure 3 - Result of the setup

***
## [Convert image's absolute path to relative](https://github.com/andrey-aleks/Blender_Custom_Tools/blob/master/Scripts/relative_paths_converter_addon.py)
For a convinient usage of textures inside .blend project you can keep paths as relevant (not absolute). 

This addon adds button for simple image’s path convertation - from absolute to relative.

### How to Use
The tool location in Blender: Image Editor window → N-panel → Image → RelativePathConverterPT, here you can find button “Convert Path” (Figure 1).

![image](https://user-images.githubusercontent.com/58087965/217102829-8e9e2e51-1e54-4540-9397-0bf6f96e7165.png)

Figure 1 - Button for converting

If you want to convert all images paths to relative in the current .blend file, enable “Convert All”. 

After clicking it converts path to relative (Figure 2).

![image](https://user-images.githubusercontent.com/58087965/217102888-eaf214d6-66b9-4973-a9b5-46106d557aca.png)

Figure 2 - Result of the convertation

Don’t forget to save the project.
***
## [Fast FBX Import-Export](https://github.com/andrey-aleks/Blender_Custom_Tools/blob/master/Scripts/custom_export_addon.py)
Anyone who uses Blender to import an fbx, fix a mesh, and then export the fbx back into some game engine will benefit from using an addon that speeds up the whole process.

With this tool, you no longer need to apply transforms with your hands, set all the export settings with your hands, look for the folder with the fbx where you want to fill in the changes.

### How to Use
The tool location in Blender: N-panel → Tool → Custom Import/Export (Figure 1).

![image](https://user-images.githubusercontent.com/58087965/217105721-f6e1f165-3868-4fb5-ac28-918eb54f90a1.png)

Figure 1 - Addon panel

Now, directly, how to work with it:
1. Choose fbx through a special button (1)
2. Click "Import FBX" (2), the tool will import fbx into Blender
3. Make the necessary edits in the mesh
4. Select all the meshes that you want to export to the imported fbx back (do this only in Object Mode)
5. Press the button "Export FBX" (3). The addon automatically does "Apply All Transforms" to all selected meshes, after which it exports the selected meshes with the most common export settings (Figure 2) to the fbx that you imported

![image](https://user-images.githubusercontent.com/58087965/217105922-0c592ac7-9a87-486c-89d8-a61b15250cff.png)

Figure 2 - Export settings used by the tool

6. Enjoy the updated fbx
***
