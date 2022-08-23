# pylint: skip-file
import sys

import Xlib.display
from Xlib import X

display = Xlib.display.Display()
root = display.screen().root

# These are retrieved from the X server itself
# To get a list of all atoms, emerge xlsatoms and run it
NET_WM_PID = display.intern_atom("_NET_WM_PID")
NET_CLIENT_LIST = display.intern_atom("_NET_CLIENT_LIST")

window_ids = root.get_full_property(NET_CLIENT_LIST, X.AnyPropertyType).value

find_pid = 16872
for window_id in window_ids:
    window = display.create_resource_object("window", window_id)
    pid = window.get_full_property(NET_WM_PID, X.AnyPropertyType).value
    if not pid or pid[0] != find_pid:
        continue

    geometry = window.get_geometry()
    print(
        f"{window.get_wm_class()=}\n{window.id=}\n"
        f"{geometry.x=}\n{geometry.y=}\n"
        f"{geometry.width=}\n{geometry.height=}"
    )
    sys.exit(0)

print(f"PID {find_pid} not found")
sys.exit(1)
