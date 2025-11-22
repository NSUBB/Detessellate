import os, sys
import FreeCAD
import FreeCADGui

class MeshToBodyCommand:
    def GetResources(self):
        icon_path = os.path.join(
            os.path.dirname(__file__), "..", "Macros", "MeshToBody", "meshtobody.svg"
        )
        return {
            'Pixmap': icon_path,
            'MenuText': 'Mesh To Body',
            'ToolTip': 'Convert mesh to parametric body'
        }

    def Activated(self):
        macro_path = os.path.join(os.path.dirname(__file__), "..", "Macros", "MeshToBody")
        macro_path = os.path.abspath(macro_path)
        if macro_path not in sys.path:
            sys.path.append(macro_path)

        try:
            import importlib
            if 'MeshToBody' in sys.modules:
                import MeshToBody
                importlib.reload(MeshToBody)
            else:
                import MeshToBody

            # Call the function directly
            MeshToBody.run_unified_macro(auto_mode=True)

        except Exception as e:
            FreeCAD.Console.PrintError(f"Error running MeshToBody: {e}\n")
            import traceback
            traceback.print_exc()

    def IsActive(self):
        return True
