from PIL import Image
import struct

def encode(pixels, width, height):
    length = len(pixels)
    output = []
    left = 0

    while left < length:
        right = left

        while right + 1 < length and pixels[right] == pixels[right + 1]:
            right += 1

        count = (right - left) + 1
        value = 1 if pixels[left] == 255 else 0
        output.append((count, value))

        left = right + 1

    output.append((width, height))

    return output


def decode(file, output_image="reconstructed.png"):
    with open(file, "r") as f:
        lines = f.readlines()

    decoded_pixels = []
    for line in lines[:-1]:  
        count, value = map(int, line.strip().split(","))
        decoded_pixels.extend([value * 255] * count)

    width, height = map(int, lines[-1].strip().split(","))

    img = Image.new("1", (width, height))  
    img.putdata(decoded_pixels)
    img.save(output_image)
    print(f"Image reconstructed and saved as {output_image}")


def save_to_file(encoded_data, filename="compressed.rle"):
    with open(filename, "w") as f:

        for count, value in encoded_data[:-1]: 
            f.write(f"{count},{value}\n")
        f.write(f"{encoded_data[-1][0]},{encoded_data[-1][1]}\n")

    with open(filename, "wb") as f:

        for count, value in encoded_data[:-1]:

            f.write(struct.pack("H", count))
            f.write(struct.pack("B", value))


img = Image.open("example2.jpg").convert("1") 
width, height = img.size
pixels = list(img.getdata())

encoded_data = encode(pixels, width, height)
save_to_file(encoded_data, "example2.rle")

decode("example2.rle", "reconstructed-example2.png")
