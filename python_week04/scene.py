# NAME: EDWIN LEONARDO LEON MATIAS
import math
import random
import turtle

from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500
    canvas = start_drawing("Scene", scene_width, scene_height)
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
                   scene_width, scene_height, width=0, fill="skyBlue1")

    # Draw the sun.
    draw_oval(canvas, 50, 350, 120, 420, width=0, fill="yellow1")

    # Draw tex.
    draw_text(canvas, 50, 480, "A sunny day", fill="purple")

    # Draw the bird.
    bird_center_x = 450  # (x)
    bird_center_y = 450  # (y)
    bird_hight = 100
    draw_bird(canvas, bird_center_x,
              bird_center_y, bird_hight)

    bird_center_x = 300  # (x)
    bird_center_y = 450  # (y)
    bird_hight = 50
    draw_bird(canvas, bird_center_x,
              bird_center_y, bird_hight)

    bird_center_x = 600  # (x)
    bird_center_y = 250  # (y)
    bird_hight = 70
    draw_bird(canvas, bird_center_x,
              bird_center_y, bird_hight)

    bird_center_x = 500  # (x)
    bird_center_y = 350  # (y)
    bird_hight = 70
    draw_bird(canvas, bird_center_x,
              bird_center_y, bird_hight)

    bird_center_x = 200  # (x)
    bird_center_y = 300  # (y)
    bird_hight = 140
    draw_bird(canvas, bird_center_x,
              bird_center_y, bird_hight)

    bird_center_x = 750  # (x)
    bird_center_y = 450  # (y)
    bird_hight = 50
    draw_bird(canvas, bird_center_x,
              bird_center_y, bird_hight)

    # draw_house
    width = 100
    height = 100
    x = 350
    y = scene_height / 3
    draw_rectangle(canvas, x, y, x + width, scene_height / 3 + height, width=1, fill="burlywood1")
    draw_rectangle(canvas, x + 40, y, x + 60, scene_height / 3 + 30, width=1, fill="orange4")
    draw_polygon(canvas, x - 25, y + height, x + width + 25, y + height, x + width / 2, y + height + 50, width=0,
                 fill="tan3")

    # Draw the cloud
    cloud_center_x = 600
    cloud_center_y = 390
    cloud_hight = 75
    draw_cloud(canvas, cloud_center_x,
               cloud_center_y, cloud_hight)

    cloud_center_x = 445
    cloud_center_y = 350
    cloud_hight = 50
    draw_cloud(canvas, cloud_center_x,
               cloud_center_y, cloud_hight)

    cloud_center_x = 300
    cloud_center_y = 400
    cloud_hight = 70
    draw_cloud(canvas, cloud_center_x,
               cloud_center_y, cloud_hight)

    cloud_center_x = 150
    cloud_center_y = 200
    cloud_hight = 50
    draw_cloud(canvas, cloud_center_x,
               cloud_center_y, cloud_hight)

    cloud_center_x = 700
    cloud_center_y = 300
    cloud_hight = 40
    draw_cloud(canvas, cloud_center_x,
               cloud_center_y, cloud_hight)


def draw_cloud(canvas, cloud_center_x, cloud_center_y, cloud_hight):
    x0 = cloud_center_x - cloud_hight  # 75
    y0 = cloud_center_y - cloud_hight / 3  # 25
    x1 = cloud_center_x + cloud_hight / 3  # 25
    y1 = cloud_center_y + cloud_hight / 3  # 25
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="white")

    x0 = cloud_center_x - cloud_hight / 3  # 25
    y0 = cloud_center_y - cloud_hight / 3  # 25
    x1 = cloud_center_x + cloud_hight  # 75
    y1 = cloud_center_y + cloud_hight / 3  # 25
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="white")

    x0 = cloud_center_x - cloud_hight / 3  # 25
    y0 = cloud_center_y - cloud_hight / 3.75  # 20
    x1 = cloud_center_x + cloud_hight / 1.5  # 50
    y1 = cloud_center_y + cloud_hight / 1.8  # 40
    draw_oval(canvas, x0, y0, x1, y1, width=0, fill="white")


def draw_bird(canvas, bird_center_x, bird_center_y, bird_hight):
    x0 = bird_center_x - bird_hight / 4  # (25)
    y0 = bird_center_y - bird_hight / 6  # 15
    x1 = bird_center_x + bird_hight / 20  # 5
    y1 = bird_center_y + bird_hight / 6  # 15
    draw_arc(canvas, x0, y0, x1, y1, start=400, extent=100)

    x0 = bird_center_x - bird_hight / 20  # 5
    y0 = bird_center_y - bird_hight / 6  # 15
    x1 = bird_center_x + bird_hight / 4  # 25
    y1 = bird_center_y + bird_hight / 6  # 15
    draw_arc(canvas, x0, y0, x1, y1, start=400, extent=100)


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
                   scene_width, scene_height / 3, width=0, fill="seagreen")

    # Draw a pine tree.
    tree_center_x = 380  # (x)
    tree_bottom = 150  # (y)
    tree_height = 50  # (tree height)
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

    tree_center_x = 160
    tree_bottom = 30
    tree_height = 180
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

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

    tree_center_x = 640
    tree_bottom = 30
    tree_height = 180
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)

    tree_center_x = 740
    tree_bottom = 0
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
                   tree_bottom, tree_height)
    # draw_passage
    draw_polygon(canvas, 200, 0, 600, 0, 400, scene_height / 3, fill="tan2")

    # draw_picket
    width = 15
    height = 50
    space = 5
    interval = width + space

    # Draw a row of 10 picket
    x = 0
    y = 0
    for i in range(10):
        draw_rectangle(canvas, x, y, x + width, y + height, width=0, fill="white")
        draw_polygon(canvas, x, y + height, x + width, y + height, x + width / 2, y + height + width, width=0,
                     outline="white", fill="white")
        x += interval

    x = 605
    y = 0
    for i in range(10):
        draw_rectangle(canvas, x, y, x + width, y + height, width=0, fill="white")
        draw_polygon(canvas, x, y + height, x + width, y + height, x + width / 2, y + height + width, width=0,
                     outline="white", fill="white")
        x += interval


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
