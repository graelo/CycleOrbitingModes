import FreeCAD as App

from OrbitingModes.utils import Log


def toggle_orbiting():
    """Toggle between (Turntable + Window center) and (Trackball + Drag at cursor)."""
    pView = App.ParamGet("User parameter:BaseApp/Preferences/View")

    # Preference keys
    #  OrbitStyle: 0=Trackball, 1=Turntable
    #  RotationMode: 0=Drag at cursor, 1=Window center
    orbit_style = pView.GetInt("OrbitStyle", 0)
    rot_mode = pView.GetInt("RotationMode", 0)

    # Define the two states
    #   State A: Turntable + Window center  => (0, 0)
    #   State B: Trackball + Drag at cursor => (1, 1)
    if (orbit_style, rot_mode) == (0, 0):
        # Currently in Turntable+Window center → switch to Trackball+Drag at cursor
        new_orbit = 1
        new_rot = 1
    else:
        # Otherwise switch to Turntable+Window center
        new_orbit = 0
        new_rot = 0

    # Apply new settings
    pView.SetInt("OrbitStyle", new_orbit)
    pView.SetInt("RotationMode", new_rot)

    # Notify the user
    state_name = "Trackball+Drag at cursor" if new_orbit else "Turntable+Window center"
    Log.info(f"Navigation toggled to: {state_name}\n")
