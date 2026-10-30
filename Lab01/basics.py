# Lab Task 01: Python Fundamentals
# Digital Image Processing Lab

# ==========================================
# Exercise 1: Variables and Data Types
# ==========================================
print("--- Exercise 1: Variables and Data Types ---")
width = 640
height = 480
image_name = "sample.png"
is_color = True

print(f"width: {width}, type: {type(width)}")
print(f"height: {height}, type: {type(height)}")
print(f"image_name: {image_name}, type: {type(image_name)}")
print(f"is_color: {is_color}, type: {type(is_color)}")

total_pixels = width * height
print(f"Total number of pixels (width * height): {total_pixels}")
print()

# ==========================================
# Exercise 2: if, elif, and else
# ==========================================
print("--- Exercise 2: if, elif, and else ---")
test_intensities = [-1, 0, 127, 128, 255, 256]

for intensity in test_intensities:
    if intensity < 0 or intensity > 255:
        label = "Invalid"
    elif intensity >= 128:
        label = "Bright pixel"
    else:
        label = "Dark pixel"
    print(f"Intensity {intensity}: {label}")
print()

# ==========================================
# Exercise 3: for and while Loops
# ==========================================
print("--- Exercise 3: for and while Loops ---")
pixels_list = [20, 130, 255]
print("For loop visiting pixel values:")
for val in pixels_list:
    if val >= 128:
        label = "Bright pixel"
    else:
        label = "Dark pixel"
    print(f"Pixel {val}: {label}")

print("\nWhile loop printing 0, 1, and 2:")
counter = 0
while counter < 3:
    print(counter)
    counter += 1
print()

# ==========================================
# Exercise 4: Functions
# ==========================================
print("--- Exercise 4: Functions ---")
def is_bright(pixel, threshold=128):
    return pixel >= threshold

print(f"is_bright(127): {is_bright(127)}")
print(f"is_bright(128): {is_bright(128)}")
print(f"is_bright(200, 210): {is_bright(200, 210)}")
print()

# ==========================================
# Exercise 5: Lists and Tuples
# ==========================================
print("--- Exercise 5: Lists and Tuples ---")
pixels = [0, 128, 255]
print(f"First item: {pixels[0]}")

# Replace the middle item (index 1) with 150
pixels[1] = 150

# Append 64
pixels.append(64)
print(f"Updated list: {pixels}")
print(f"Length of list: {len(pixels)}")

# Create size tuple and unpack into width and height
size = (640, 480)
w, h = size
print(f"Unpacked size -> Width: {w}, Height: {h}")

# Explanation comment:
# In Python, lists are mutable objects, meaning their elements can be modified, added,
# or removed in place without altering the object's identity in memory.
# In contrast, tuples are immutable data structures designed with fixed values; once created,
# their elements and size cannot be reassigned or modified.
print()

# ==========================================
# Exercise 6: Dictionaries and Sets
# ==========================================
print("--- Exercise 6: Dictionaries and Sets ---")
image = {"width": 640, "height": 480}
image["mode"] = "RGB"

print(f"Width: {image['width']}")
print(f"Mode: {image['mode']}")

labels = ["cat", "dog", "cat", "bird"]
unique_labels = set(labels)
print(f"Labels set: {unique_labels}")
print(f"Length of unique labels set: {len(unique_labels)}")
