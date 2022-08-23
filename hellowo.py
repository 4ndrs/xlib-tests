# pylint: skip-file
import sys
import Xlib
from Xlib import X, display


class Window:
    def __init__(self, display, msg):
        self.display = display
        self.msg = msg

        self.screen = self.display.screen()
        self.window = self.screen.root.create_window(
            1403,
            10,
            1080,
            1080,
            1,
            self.screen.root_depth,
            background_pixel=self.screen.white_pixel,
            event_mask=X.ExposureMask
            | X.ButtonPressMask
            | X.EnterWindowMask
            | X.LeaveWindowMask
            | X.KeyPressMask
            | X.PointerMotionMask,
        )
        self.gc = self.window.create_gc(
            foreground=self.screen.black_pixel,
            background=self.screen.white_pixel,
            line_width=3,
        )

        self.WM_DELETE_WINDOW = self.display.intern_atom("WM_DELETE_WINDOW")

        self.window.set_wm_class("hellowo", "HellOWO")
        self.window.map()

        self.coordinates = {"x": 0, "y": 0}

    def draw(self):
        self.window.rectangle(
            self.gc,
            self.coordinates["x"],
            self.coordinates["y"],
            300,
            300,
        )

    def loop(self):
        while True:
            try:
                e = self.display.next_event()
            except KeyboardInterrupt:
                sys.exit()
            except Xlib.error.ConnectionClosedError:
                print("Connection to the X server closed.")
                sys.exit(-1)

            match e.type:
                case X.Expose:
                    self.draw()
                case X.MotionNotify:
                    self.coordinates["x"] = e.event_x
                    self.coordinates["y"] = e.event_y
                    self.draw()

                case X.KeyPress:
                    # the keycode is 24 which is q
                    # can be converted Window.keycode_to_keysym(24, 0)
                    # Display.keysym_to_keycode(ordinal which is 113)
                    if e.detail == self.display.keysym_to_keycode(ord("q")):
                        sys.exit()
                    else:
                        print(e.detail)
                case X.ClientMessage:  # what is this? Never reached
                    print(e.data)
                    fmt, data = e.data
                    if fmt == 32 and data == self.WM_DELETE_WINDOW:
                        sys.exit()


if __name__ == "__main__":
    Window(display.Display(), "Hello, World!").loop()
