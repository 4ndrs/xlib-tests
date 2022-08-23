# pylint: skip-file
import Xlib.display

display = Xlib.display.Display()
root = display.screen().root

# This is a window resource object
window = root.query_pointer().child

geometry = window.get_geometry()
print(
    f"{window.id}\n{geometry.x=}\n{geometry.y=}\n"
    f"{geometry.width=}\n{geometry.height=}"
)
