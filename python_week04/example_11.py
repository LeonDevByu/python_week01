import math
import random
import turtle

from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
                   scene_width, scene_height, width=0, fill="midnightblue")

    # start
    half_height = round(scene_height / 1)
    min_diam = 5
    max_diam = 8

    # Draw 100 circles, each with
    # a random location and diameter.
    for i in range(50):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                  fill="yellow1")

def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
                   scene_width, scene_height / 3, width=0, fill="seagreen")

    tree_center_x = 380
    tree_bottom = 150
    tree_height = 50
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    tree_center_x = 350
    tree_bottom = 130
    tree_height = 75
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    tree_center_x = 300
    tree_bottom = 110
    tree_height = 100
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    tree_center_x = 240
    tree_bottom = 80
    tree_height = 125
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    # Draw a pine tree.
    tree_center_x = 160
    tree_bottom = 30
    tree_height = 180
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 60
    tree_bottom = 0
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    # ==================================
    tree_center_x = 420
    tree_bottom = 150
    tree_height = 50
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    tree_center_x = 450
    tree_bottom = 130
    tree_height = 75
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    tree_center_x = 500
    tree_bottom = 110
    tree_height = 100
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    tree_center_x = 560
    tree_bottom = 80
    tree_height = 125
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    # Draw a pine tree.
    tree_center_x = 640
    tree_bottom = 30
    tree_height = 180
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    # Draw another pine tree.
    tree_center_x = 740
    tree_bottom = 0
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)


def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the pine tree.
    draw_rectangle(canvas,
                   trunk_left, trunk_top, trunk_right, bottom,
                   outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    # Draw the crown (also called skirt) of the pine tree.
    draw_polygon(canvas, center_x, skirt_top,
                 skirt_right, trunk_top,
                 skirt_left, trunk_top,
                 outline="gray20", width=1, fill="dark green")


main()


