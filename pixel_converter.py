import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def find_animal_crossing_color(original_color):
    colortable = [
        [225, 47, 47],
        [225, 118, 50],
        [230, 240, 37],
        [120, 228, 44],
        [30, 138, 29],
        [55, 182, 214],
        [45, 143, 206],
        [66, 62, 221],
        [136, 75, 230],
        [230, 91, 202],
        [227, 167, 153],
        [137, 81, 64],
        [229, 229, 229],
        [110, 110, 110],
        [20, 20, 20]
    ]
    chart = []
    for i in range(15):
        d = 0
        for j in range(3):
            d += abs(original_color[j] - colortable[i][j])
        chart.append(d)
    idx = chart.index(min(chart))
    return colortable[idx]


def convert(filename):
    original_img = mpimg.imread(filename)
    h = original_img.shape[0]
    w = original_img.shape[1]
    # change to int 0 - 255 RGB data type
    if type(original_img[0][0][0]) == np.float32:
        for i in range(h):
            for j in range(w):
                original_img[i][j][0] = round(original_img[i][j][0] * 255)
                original_img[i][j][1] = round(original_img[i][j][1] * 255)
                original_img[i][j][2] = round(original_img[i][j][2] * 255)

    pixel_img = np.zeros((640, 640, 3), dtype=np.int)
    animal_crossing_img = np.zeros((640, 640, 3), dtype=np.int)

    for i in range(32):
        for j in range(32):
            h_pixel_n = h // 32
            w_pixel_n = w // 32
            r_sum, g_sum, b_sum = 0, 0, 0
            for x in range(h_pixel_n):
                for y in range(w_pixel_n):
                    r_sum += original_img[i *
                                          h_pixel_n + x][j * w_pixel_n + y][0]
                    g_sum += original_img[i *
                                          h_pixel_n + x][j * w_pixel_n + y][1]
                    b_sum += original_img[i *
                                          h_pixel_n + x][j * w_pixel_n + y][2]
            r_avg = round(r_sum / (h_pixel_n * w_pixel_n))
            g_avg = round(g_sum / (h_pixel_n * w_pixel_n))
            b_avg = round(b_sum / (h_pixel_n * w_pixel_n))
            animal_crossing_rgb = find_animal_crossing_color(
                [r_avg, g_avg, b_avg])
            for x in range(20):
                for y in range(20):
                    pixel_img[i * 20 + x][j * 20 + y][0] = r_avg
                    pixel_img[i * 20 + x][j * 20 + y][1] = g_avg
                    pixel_img[i * 20 + x][j * 20 + y][2] = b_avg
                    animal_crossing_img[i * 20 + x][j * 20 +
                                                    y][0] = animal_crossing_rgb[0]
                    animal_crossing_img[i * 20 + x][j * 20 +
                                                    y][1] = animal_crossing_rgb[1]
                    animal_crossing_img[i * 20 + x][j * 20 +
                                                    y][2] = animal_crossing_rgb[2]
                    if x == 0 or x == 19 or y == 0 or y == 19:
                        pixel_img[i * 20 + x][j * 20 + y][:] = 250
                        animal_crossing_img[i * 20 + x][j * 20 + y][:] = 250
    '''
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 3, 1)
    plt.title('Original Image')
    plt.imshow(original_img)
    plt.axis('off')
    plt.subplot(1, 3, 2)
    plt.title('Pixel Image')
    plt.imshow(pixel_img)
    plt.axis('off')
    plt.subplot(1, 3, 3)
    plt.title('Animal Crossing Image')
    plt.imshow(animal_crossing_img)
    plt.axis('off')
    plt.savefig('Comparasion_' + filename,
                dpi=300, pad_inches=0.0)
    '''
    plt.imshow(pixel_img)
    plt.axis('off')
    plt.savefig('pixel_' + filename, dpi=300, transparent=True, pad_inches=0.0)
    plt.imshow(animal_crossing_img)
    plt.axis('off')
    plt.savefig('animal_crossing_' + filename,
                dpi=300, transparent=True, pad_inches=0.0)


filename = '1975.jpg'
#filename = 'meandyou.jpg'
convert(filename)
