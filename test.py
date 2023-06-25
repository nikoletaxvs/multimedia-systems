def run_length_encode(image):
    encoded_image = []
    current_pixel = image[0][0]
    count = 0

    for row in image:
        for pixel in row:
            if pixel == current_pixel:
                count += 1
            else:
                encoded_image.append((count, current_pixel))
                current_pixel = pixel
                count = 1

    # Add the last run of pixels to the encoded image
    encoded_image.append((count, current_pixel))

    return encoded_image


def run_length_decode(encoded_image):
    decoded_image = []

    for run in encoded_image:
        count, pixel = run
        decoded_image.extend([pixel] * count)

    return decoded_image


# Example usage
image = "VideoFramesFolder/frame0.jpg"

encoded_image = run_length_encode(image)
print(encoded_image)  # Output: [(3, [255, 255, 255]), (3, [0, 0, 0]), (3, [255, 255, 255])]

decoded_image = run_length_decode(encoded_image)
print(
    decoded_image)  # Output: [[255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255]]
