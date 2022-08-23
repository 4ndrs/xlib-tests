# pylint: skip-file
from Xlib import display, X

display = display.Display()
screen = display.screen()
root = screen.root

print(root.get_attributes())
root.change_attributes(event_mask=X.ExposureMask)
print(root.get_attributes())

gc = root.create_gc(
    foreground=screen.white_pixel, background=screen.black_pixel
)


def draw_it():
    root.draw_text(gc, 0, 0, b"Hello, world!")
    display.flush()


draw_it()
while True:
    if display.pending_events() != 0:
        event = display.next_event()
        if event.type == X.Expose and event.count == 0:
            draw_it()
