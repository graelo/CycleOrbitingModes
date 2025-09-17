import os, sys
import FreeCAD as App
import FreeCADGui as Gui

user_data = App.getUserAppDataDir()  # e.g., ~/Library/Application Support/FreeCAD/
mod_dir = os.path.join(user_data, "Mod", "CycleOrbitingModes")
if mod_dir not in sys.path:
    sys.path.insert(0, mod_dir)

mod_icon_path = os.path.join(mod_dir, "Resources", "icons")
Gui.addIconPath(mod_icon_path)


class _CycleOrbitingModesCmd:
    def GetResources(self):
        return {
            "Pixmap": "CycleOrbitingModes_Orbit",
            "MenuText": "CycleOrbitingModes",
            "ToolTip": "Cycle orbiting style between Turntable+Center, Trackball+Cursor, and others",
        }

    def Activated(self):
        App.Console.PrintMessage("running the shortcut")
        from cycle_orbiting_modes import toggle_orbiting

        toggle_orbiting()

    def IsActive(self):
        return True


Gui.addCommand("CycleOrbiting", _CycleOrbitingModesCmd())
App.Console.PrintMessage("CycleOrbiting command added")
