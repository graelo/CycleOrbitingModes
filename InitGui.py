import os
import FreeCAD as App
import FreeCADGui as Gui


class OrbitingModesWorkbench(Gui.PythonWorkbench):
    #  Icon in XPM 16x16
    Icon = os.path.dirname(__file__) + "/Resources/icons/OrbitingModes_Orbit.svg"
    MenuText = "OrbitingModes"
    ToolTip = "Change Orbiting Modes easily"

    def GetClassName(self):
        return super().GetClassName()

    def Initialize(self):
        # Do not add toolbar or menu
        pass

    def Activated(self):
        """Hide the workbench tab."""
        mw = Gui.getMainWindow()
        dock = mw.findChild("QDockWidget", "OrbitingModesDockWidget")
        if dock:
            dock.hide()
        App.Console.PrintMessage("OrbitingModes workbench activated (tab hidden)")
        return super().Activated()  # TODO: remove?

    def Deactivated(self):
        pass

    def ContextMenu(self, recipient):
        pass

    def GetPreferencesPages(self) -> None:
        return None


class _CycleOrbitingModesCmd:
    def GetResources(self):
        return {
            "Pixmap": "OrbitingModes_Orbit",
            "MenuText": "CycleOrbitingModes",
            "ToolTip": "Cycle orbiting style between Turntable+Center, Trackball+Cursor, and others",
        }

    def Activated(self):
        App.Console.PrintMessage("running the shortcut")
        from orbiting_modes import toggle_orbiting

        toggle_orbiting()

    def IsActive(self):
        return True


Gui.addWorkbench(OrbitingModesWorkbench)
Gui.addCommand("CycleOrbitingModes", _CycleOrbitingModesCmd())
App.Console.PrintMessage("CycleOrbitingModes command added")
