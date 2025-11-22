import FreeCAD
import FreeCADGui
import traceback

print("Detessellate InitGui.py starting to load")

# Command specs: (command name, module path, class name, toolbar group)
command_specs = [
    ("MeshPlacement", "Commands.MeshPlacementCommand", "MeshPlacementCommand", "Detessellate Mesh"),
    ("MeshToBody", "Commands.MeshToBodyCommand", "MeshToBodyCommand", "Detessellate Mesh"),
]

commands = {}

for cmd_name, module_path, class_name, toolbar in command_specs:
    try:
        module = __import__(module_path, fromlist=[class_name])
        cmd_class = getattr(module, class_name)
        commands[cmd_name] = (cmd_class, toolbar)
        print(f"{cmd_name} imported successfully")
    except Exception as e:
        print(f"ERROR importing {cmd_name}: {e}")
        traceback.print_exc()

print("Detessellate InitGui.py loaded")

class DetessellateWorkbench(FreeCADGui.Workbench):
    MenuText = "Detessellate"
    ToolTip = "Tools to reverse engineer meshes"
    Icon = "Detessellate/Macros/MeshPlacement/meshplacement.svg"

    def Initialize(self):
        global commands
        # Register all successfully imported commands
        for cmd_name, (cmd_class, toolbar) in commands.items():
            FreeCADGui.addCommand(cmd_name, cmd_class())
            self.appendToolbar(toolbar, [cmd_name])
            self.appendMenu("Detessellate", [cmd_name])

    def Activated(self):
        pass

    def Deactivated(self):
        pass

FreeCADGui.addWorkbench(DetessellateWorkbench())
