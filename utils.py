import os
from typing import Optional

from PySide import QtCore
import FreeCAD as App

AddonName = "OrbitingModes"


class Resources:
    """Helper to register paths to resources."""

    mod_path = os.path.dirname(__file__)
    icons_path = os.path.join(mod_path, "Resources", "icons")

    @classmethod
    def register_search_paths(cls) -> None:
        QtCore.QDir.addSearchPath("icons", cls.icons_path)


class Log:
    """Consistent logging."""

    addon = AddonName

    @classmethod
    def error(cls, msg: str) -> None:
        App.Console.PrintError(f"[{cls.addon}] {msg}\n")

    @classmethod
    def warning(cls, msg: str) -> None:
        App.Console.PrintWarning(f"[{cls.addon}] {msg}\n")

    @classmethod
    def info(cls, msg: str) -> None:
        App.Console.PrintMessage(f"[{cls.addon}] {msg}\n")


def int_or_zero(value: str) -> int:
    """Parse a string into an int, otherwise return 0."""
    try:
        return int(value)
    except ValueError:
        return 0


def check_freecad_version(*, min_version: list[int]) -> bool:
    """Check whether the current FreeCAD version is greater or equal than min_version.

    Provide min_version
    Args:
        min_version: Mininum version expressed as a list of ints: "1.0.2" is
            expected as [1, 0, 2].
    """
    current = [int_or_zero(v.split()[0]) for v in App.Version()[:4]]
    return current >= min_version


def find_toolbar(toolbar_groups, toolbar_name: str) -> Optional["App.ParameterGrp"]:
    # Log.info(f"group names: {toolbar_groups.GetGroups()}")
    for group_name in toolbar_groups.GetGroups():
        tb_group = toolbar_groups.GetGroup(group_name)
        # Log.info(f"for {group_name}, GetString(name) -> {tb_group.GetString('Name')}")
        if tb_group.GetString("Name") == toolbar_name:
            # Log.info("found!")
            return tb_group
    return None


def register_toolbar(
    addon_toolbar_name: str,
    workbench_name: str,
    command_names: list[str],
    target_toolbar: "App.ParameterGrp",
):
    """Register the Addon toolbar in the targeted workbench.

    This function adds a toolbar named after `addon_toolbar_name`, and adds to
    a Tool Button for each command in `command_names`. In case this toolbar
    already exists, the function updates the existing toolbar and ensures each
    command from `command_names` has a Tool Button.

    The name of the workbench is needed to associate each Tool Button with it.

    Feel free to override the `host_toolbar_path` to install your toolbar in
    another workbench.

    Args:
        addon_toolbar_name: Visible name in the Toolbar customization menus and
            dialogs.
        workbench_name: Class name of the workbench defined in `InitGui.py`.
        command_names: Names of the commands to add to the toolbar. These are
            simply the class name of each command to add.
        target_toolbar: The workbench's toolbar where to add the Addon's
            toolbar and buttons.

    Example:
        target_toolbar = App.ParamGet("User parameter:BaseApp/Workbench/PartDesignWorkbench/Toolbar")
        register_toolbar(
            "OrbitingModes",
            "OMWorkbench",
            ["CycleOrbitingModes"],
            target_toolbar,
        )
    """

    existing_toolbar = find_toolbar(target_toolbar, addon_toolbar_name)

    if existing_toolbar:
        # Install any new commands that we now provide into the existing toolbar
        missing = [cmd for cmd in command_names if existing_toolbar.GetString(cmd) == ""]
        if len(missing) > 0:
            Log.info(f"Updating toolbar to include new {', '.join(missing)} as well!")

            # First remove them all
            for s in existing_toolbar.GetStrings():
                if s not in ["Active", "Name"]:
                    existing_toolbar.RemString(s)

            # Then add them back
            for cmd in command_names:
                existing_toolbar.SetString(cmd, workbench_name)
    else:
        Log.info("Registering toolbar into the target workbench...")

        # Create the Addon toolbar
        new_toolbar = target_toolbar.GetGroup(workbench_name)
        new_toolbar.SetString("Name", addon_toolbar_name)

        # Commands to be added:
        for cmd in command_names:
            new_toolbar.SetString(cmd, workbench_name)

        new_toolbar.SetBool("Active", 1)
