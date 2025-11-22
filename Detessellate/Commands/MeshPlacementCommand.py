import os, sys
import FreeCAD
import FreeCADGui

class MeshPlacementCommand:
    def GetResources(self):
        icon_path = os.path.join(
            os.path.dirname(__file__), "..", "Macros", "MeshPlacement", "meshplacement.svg"
        )
        return {
            'Pixmap': icon_path,
            'MenuText': 'Mesh Placement',
            'ToolTip': 'Center and align meshes at origin'
        }

    def Activated(self):
        macro_path = os.path.join(os.path.dirname(__file__), "..", "Macros", "MeshPlacement")
        macro_path = os.path.abspath(macro_path)
        if macro_path not in sys.path:
            sys.path.append(macro_path)
        try:
            # Force reload if already imported
            import importlib
            if 'MeshPlacement' in sys.modules:
                import MeshPlacement
                importlib.reload(MeshPlacement)
            else:
                import MeshPlacement
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error running MeshPlacement: {e}\n")
            import traceback
            traceback.print_exc()

    def IsActive(self):
        return True
