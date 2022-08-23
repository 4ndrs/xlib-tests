# pylint: skip-file
import Xlib.display
from Xlib import X

display = Xlib.display.Display()
screen = display.screen()

NET_ACTIVE_WINDOW = display.intern_atom("_NET_ACTIVE_WINDOW")
wid = screen.root.get_full_property(
    NET_ACTIVE_WINDOW, X.AnyPropertyType
).value[0]
print(f"{wid = }")

# show window size and position
window = display.create_resource_object("window", wid)
geometry = window.get_geometry()
print(f"{geometry.x=}\n{geometry.y=}\n{geometry.width=}\n{geometry.height=}")
