# pylint: skip-file
"""
Based on cairo-deomo/X11/cairo-demo.c
"""

import cairo
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk  # noqa: E402


def draw(area, context):
    context.set_source_rgb(1, 0, 0, 1)
    context.rectangle(25, 25, 384, 199)
    context.set_line_width(5.0)
    context.stroke()
    context.paint()


def main():
    win = Gtk.Window()
    win.connect("destroy", lambda w: Gtk.main_quit())
    win.set_default_size(450, 550)

    drawingarea = Gtk.DrawingArea()
    drawingarea.connect("draw", draw)
    win.show_all()
    win.add(drawingarea)
    Gtk.main()


if __name__ == "__main__":
    main()
