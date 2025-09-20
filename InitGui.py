"""Addon initialization."""

import FreeCAD as App


# Fake workbench class to make the addon manager happy
class OMWorkBench:
    pass


def initialize() -> None:
    # cycle.register_command_globally()

    from OrbitingModes.utils import register_toolbar, Log, Resources

    ADDON_NAME = "OrbitingModes"
    Log.addon = ADDON_NAME
    Resources.register_search_paths()

    from OrbitingModes.commands import cycle

    cycle.register_command_globally()

    target_toolbar = App.ParamGet("User parameter:BaseApp/Workbench/PartDesignWorkbench/Toolbar")
    register_toolbar(
        addon_toolbar_name="OrbitingModes",
        workbench_name="OMWorkbench",
        command_names=["CycleOrbitingModes"],
        target_toolbar=target_toolbar,
    )


initialize()
