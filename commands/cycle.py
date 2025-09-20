import os
import FreeCAD as App
import FreeCADGui as Gui


from OrbitingModes.utils import Log


class _CycleOrbitingModesCmd:
    def GetResources(self):
        return {
            # "Pixmap": os.path.join(
            #     App.getUserAppDataDir(),
            #     "Mod",
            #     "CycleOrbitingModes",
            #     "Resources",
            #     "icons",
            #     "OrbitingModes_Orbit.svg",
            # ),
            "Pixmap": "icons:OrbitingModes_Orbit.svg",
            "MenuText": "CycleOrbitingModes",
            "ToolTip": "Cycle orbiting style between Turntable+Center, Trackball+Cursor, and others",
            "Accel": "Ctrl+Shift+J",
        }

    def Activated(self):
        # Log.info("OrbitingModes activated\n")
        try:
            from OrbitingModes.core import toggle_orbiting

            toggle_orbiting()
        except Exception as e:
            Log.error(f"Error in toggle_orbiting: {e}\n")

    def IsActive(self):
        return True


def register_command_globally() -> None:
    """Register the command globally (not tied to any specific workbench)."""
    Gui.addCommand("CycleOrbitingModes", _CycleOrbitingModesCmd())
