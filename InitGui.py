import os
import FreeCAD as App
import FreeCADGui as Gui


class _CycleOrbitingModesCmd:
    def GetResources(self):
        # XPM icon data (16x16 pixels)
        """
        /* XPM */
        static char * CycleOrbitingModes_Orbit_xpm[] = {
        "16 16 2 1",
        " 	c None",
        ".	c #000000",
        "                ",
        "      ....      ",
        "    ..    ..    ",
        "   .        .   ",
        "  .    ..    .  ",
        " .    .  .    . ",
        " .   .    .   . ",
        ".   .  ..  .   .",
        ".   .  ..  .   .",
        " .   .    .   . ",
        " .    .  .    . ",
        "  .    ..    .  ",
        "   .        .   ",
        "    ..    ..    ",
        "      ....      ",
        "                "};
        """

        return {
            "Pixmap": os.path.join(
                App.getUserAppDataDir(),
                "Mod",
                "CycleOrbitingModes",
                "Resources",
                "icons",
                "CycleOrbitingModes_Orbit.svg",
            ),
            "MenuText": "CycleOrbitingModes",
            "ToolTip": "Cycle orbiting style between Turntable+Center, Trackball+Cursor, and others",
            "Accel": "Ctrl+Shift+J",
        }

    def Activated(self):
        App.Console.PrintMessage("running the shortcut\n")
        try:
            from orbiting_modes import toggle_orbiting

            toggle_orbiting()
        except Exception as e:
            App.Console.PrintError(f"Error in toggle_orbiting: {e}\n")

    def IsActive(self):
        return True


# Register the command globally (not tied to any specific workbench)
Gui.addCommand("CycleOrbitingModes", _CycleOrbitingModesCmd())
