# pylint: skip-file
import cairo

surface = cairo.ImageSurface(cairo.Format.ARGB32, 1920, 1080)
context = cairo.Context(surface)

context.set_source_rgba(1, 0, 0, 1)
context.rectangle(25, 25, 384, 899)
context.set_line_width(5.0)
context.stroke()

surface.write_to_png("cairo.png")
