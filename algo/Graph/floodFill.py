"""
    
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
    
"""
# Dfs approach


def floodFill(image, sr, sc, color):
    cur_color = image[sr][sc]
    # First check if there is work to be done. I.E cur_color is different from newColor
    if cur_color == color:
        return image
    height, width = len(image), len(image[0])

    def dfs(sr, sc):
        if 0 <= sr < height and 0 <= sc < width and image[sr][sc] == cur_color and image[sr][sc] != color:
            image[sr][sc] = color
            dfs(sr+1, sc)
            dfs(sr-1, sc)
            dfs(sr, sc + 1)
            dfs(sr, sc - 1)

    dfs(sr, sc)

    return image
