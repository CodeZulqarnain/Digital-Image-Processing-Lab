"""
Department of Software Engineering
The University of Azad Jammu and Kashmir
Digital Image Processing Lab (Session 2024-28)
Lab Task # 02 — Digital Images, Pixels, Color, and Basic Transformations

Student Name: Zulqarnain Mohi Ud Din
Roll Number: 2024-SE-07 (2024-SET-07)
Instructor: Engr. Fahad Nisar
"""

import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def main():
    print("=" * 70)
    print("DIP Lab Task # 02: Digital Images, Pixels, Color, and Transformations")
    print("Student: Zulqarnain Mohi Ud Din | Roll No: 2024-SE-07")
    print("=" * 70)

    # -------------------------------------------------------------------------
    # Step 2: Load the Image
    # -------------------------------------------------------------------------
    print("\n--- Step 2: Load the Image ---")
    image_path = "input_image.jpg"
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found at path: {image_path}")

    image = cv.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Failed to load image at path: {image_path}")

    print(f"Image Path: {image_path}")
    print(f"Image Shape: {image.shape}")
    print(f"Image Data Type: {image.dtype}")

    # -------------------------------------------------------------------------
    # Step 3: Inspect the Image
    # -------------------------------------------------------------------------
    print("\n--- Step 3: Inspect the Image ---")
    height, width, channels = image.shape
    print(f"Height (Rows): {height}")
    print(f"Width (Columns): {width}")
    print(f"Number of Channels: {channels}")

    # Top-left and center pixels using [row, column] indexing
    top_left_pixel = image[0, 0]
    center_row = height // 2
    center_col = width // 2
    center_pixel = image[center_row, center_col]

    print(f"Top-Left Pixel [row=0, col=0] (BGR): {top_left_pixel}")
    print(f"Center Pixel [row={center_row}, col={center_col}] (BGR): {center_pixel}")

    # Global min/max
    global_min = int(image.min())
    global_max = int(image.max())
    print(f"Global Minimum Pixel Value: {global_min}")
    print(f"Global Maximum Pixel Value: {global_max}")

    # Per-channel min/max (OpenCV default order is Blue, Green, Red)
    channel_names = ["Blue (Channel 0)", "Green (Channel 1)", "Red (Channel 2)"]
    for i, name in enumerate(channel_names):
        ch_min = int(image[:, :, i].min())
        ch_max = int(image[:, :, i].max())
        print(f"{name} -> Min: {ch_min}, Max: {ch_max}")

    # -------------------------------------------------------------------------
    # Step 4: Convert Colors and Separate Channels
    # -------------------------------------------------------------------------
    print("\n--- Step 4: Convert Colors and Separate Channels ---")
    # Convert BGR to RGB for Matplotlib
    image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    # Convert BGR to Grayscale
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Separate Red, Green, and Blue channels from the RGB image
    red_channel = image_rgb[:, :, 0]
    green_channel = image_rgb[:, :, 1]
    blue_channel = image_rgb[:, :, 2]

    # Convert center pixel RGB to HEX
    center_rgb = image_rgb[center_row, center_col]
    center_hex = "#{:02X}{:02X}{:02X}".format(center_rgb[0], center_rgb[1], center_rgb[2])
    print(f"Center Pixel [row={center_row}, col={center_col}] (RGB): {center_rgb}")
    print(f"Center Pixel HEX Value: {center_hex}")

    # 2x3 Figure displaying: RGB, Red, Green, Blue, Grayscale, and unconverted BGR
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    fig.suptitle("Step 4: Color Conversions and Channel Separation", fontsize=14, fontweight='bold')

    # Row 1
    axes[0, 0].imshow(image_rgb)
    axes[0, 0].set_title("1. Converted RGB Image")
    axes[0, 0].axis('off')

    axes[0, 1].imshow(red_channel, cmap='gray')
    axes[0, 1].set_title("2. Red Channel (Gray Colormap)")
    axes[0, 1].axis('off')

    axes[0, 2].imshow(green_channel, cmap='gray')
    axes[0, 2].set_title("3. Green Channel (Gray Colormap)")
    axes[0, 2].axis('off')

    # Row 2
    axes[1, 0].imshow(blue_channel, cmap='gray')
    axes[1, 0].set_title("4. Blue Channel (Gray Colormap)")
    axes[1, 0].axis('off')

    axes[1, 1].imshow(image_gray, cmap='gray')
    axes[1, 1].set_title("5. Grayscale Image")
    axes[1, 1].axis('off')

    axes[1, 2].imshow(image)  # Directly passing BGR to Matplotlib
    axes[1, 2].set_title("6. Unconverted BGR Image (Distorted)")
    axes[1, 2].axis('off')

    plt.tight_layout()
    channel_fig_path = "channels_comparison.png"
    plt.savefig(channel_fig_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved 2x3 color channel figure to: {channel_fig_path}")

    # -------------------------------------------------------------------------
    # Step 5: Crop, Resize, and Save
    # -------------------------------------------------------------------------
    print("\n--- Step 5: Crop, Resize, and Save ---")
    # Crop an exact 100 x 100 region centered in the image
    y_start = (height - 100) // 2
    y_end = y_start + 100
    x_start = (width - 100) // 2
    x_end = x_start + 100

    cropped_rgb = image_rgb[y_start:y_end, x_start:x_end]
    print(f"Cropped Region Slices: y=[{y_start}:{y_end}], x=[{x_start}:{x_end}]")
    print(f"Cropped Region Shape: {cropped_rgb.shape}")

    # Resize crop to 200 x 200 pixels
    resized_rgb = cv.resize(cropped_rgb, (200, 200), interpolation=cv.INTER_LINEAR)
    print(f"Resized Region Shape: {resized_rgb.shape}")

    # Display Original, Cropped, and Resized images side-by-side
    fig2, axes2 = plt.subplots(1, 3, figsize=(13, 5))
    fig2.suptitle("Step 5: Crop, Resize, and Coordinate Transform", fontsize=14, fontweight='bold', y=0.98)

    axes2[0].imshow(image_rgb)
    axes2[0].set_title(f"Original Image\n({width} x {height})", pad=10)
    # Draw a bounding rectangle indicator on original for clarity
    rect = plt.Rectangle((x_start, y_start), 100, 100, linewidth=2, edgecolor='red', facecolor='none')
    axes2[0].add_patch(rect)
    axes2[0].axis('off')

    axes2[1].imshow(cropped_rgb)
    axes2[1].set_title("Cropped Region\n(100 x 100)", pad=10)
    axes2[1].axis('off')

    axes2[2].imshow(resized_rgb)
    axes2[2].set_title("Resized Region\n(200 x 200)", pad=10)
    axes2[2].axis('off')

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    crop_fig_path = "crop_resize_comparison.png"
    plt.savefig(crop_fig_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved crop & resize comparison figure to: {crop_fig_path}")

    # Convert the resized RGB image back to BGR and save it as resized_crop.png
    resized_bgr = cv.cvtColor(resized_rgb, cv.COLOR_RGB2BGR)
    save_filename = "resized_crop.png"
    save_success = cv.imwrite(save_filename, resized_bgr)
    print(f"cv.imwrite('{save_filename}') saved successfully: {save_success}")

    # -------------------------------------------------------------------------
    # Step 6: Create a Histogram
    # -------------------------------------------------------------------------
    print("\n--- Step 6: Create a Histogram ---")
    # Flatten grayscale image
    flattened_gray = image_gray.ravel()

    plt.figure(figsize=(9, 5))
    plt.hist(flattened_gray, bins=256, range=[0, 256], color='#1f77b4', alpha=0.85, edgecolor='black', linewidth=0.2)
    plt.title("Grayscale Intensity Histogram (256 Bins)", fontsize=13, fontweight='bold')
    plt.xlabel("Pixel Intensity Level (0 = Pure Black, 255 = Pure White)", fontsize=11)
    plt.ylabel("Number of Pixels (Frequency)", fontsize=11)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.xlim([0, 256])

    # Mark mean intensity
    mean_val = float(np.mean(flattened_gray))
    median_val = float(np.median(flattened_gray))
    plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=1.5, label=f'Mean Intensity: {mean_val:.2f}')
    plt.axvline(median_val, color='green', linestyle='dotted', linewidth=1.5, label=f'Median Intensity: {median_val:.2f}')
    plt.legend(loc='upper right')

    hist_filename = "grayscale_histogram.png"
    plt.savefig(hist_filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved grayscale histogram plot to: {hist_filename}")
    print(f"Histogram Statistics -> Mean: {mean_val:.2f}, Median: {median_val:.2f}")

    # Evaluation of brightness
    if mean_val < 85:
        tone_description = "mainly dark"
    elif mean_val > 170:
        tone_description = "mainly bright"
    else:
        tone_description = "well balanced"

    explanation_hist = (
        f"Histogram Tone Evaluation:\n"
        f"The image exhibits an overall {tone_description} intensity distribution with a mean pixel value of {mean_val:.2f} "
        f"and median value of {median_val:.2f} across the [0, 255] spectrum. "
        f"The histogram displays noticeable peaks across low-to-mid tones corresponding to the patterned butterfly wings "
        f"and vibrant leaf background, alongside highlights reaching the upper intensity range for the white wing spots."
    )
    print(explanation_hist)

    # -------------------------------------------------------------------------
    # Step 7: Demonstrate Bit Depth
    # -------------------------------------------------------------------------
    print("\n--- Step 7: Demonstrate Bit Depth ---")
    # Create an 8-bit horizontal grayscale gradient from 0 to 255 (height=80, width=256)
    gradient_row = np.linspace(0, 255, 256, dtype=np.uint8)
    gradient_8bit = np.tile(gradient_row, (80, 1))

    # Quantize to 1-bit, 2-bit, and 4-bit intensity levels
    # 1-bit: 2 levels (0 and 255)
    gradient_1bit = (gradient_8bit // 128) * 255

    # 2-bit: 4 levels (0, 85, 170, 255) -> step size 85
    gradient_2bit = (gradient_8bit // 64) * 85

    # 4-bit: 16 levels (0, 17, 34, ..., 255) -> step size 17
    gradient_4bit = (gradient_8bit // 16) * 17

    # Count unique values
    unique_8bit = len(np.unique(gradient_8bit))
    unique_1bit = len(np.unique(gradient_1bit))
    unique_2bit = len(np.unique(gradient_2bit))
    unique_4bit = len(np.unique(gradient_4bit))

    print(f"8-bit Gradient Unique Intensity Values Count: {unique_8bit}")
    print(f"1-bit Quantized Unique Intensity Values Count: {unique_1bit}")
    print(f"2-bit Quantized Unique Intensity Values Count: {unique_2bit}")
    print(f"4-bit Quantized Unique Intensity Values Count: {unique_4bit}")

    # Display original and three quantized gradients in one figure
    fig3, axes3 = plt.subplots(4, 1, figsize=(10, 8))
    fig3.suptitle("Step 7: Bit Depth Quantization Comparison", fontsize=14, fontweight='bold', y=0.98)

    levels_info = [
        (axes3[0], gradient_8bit, f"8-bit Gradient (256 Intensity Levels — Unique Values: {unique_8bit})"),
        (axes3[1], gradient_4bit, f"4-bit Quantized Gradient (16 Intensity Levels — Unique Values: {unique_4bit})"),
        (axes3[2], gradient_2bit, f"2-bit Quantized Gradient (4 Intensity Levels — Unique Values: {unique_2bit})"),
        (axes3[3], gradient_1bit, f"1-bit Quantized Gradient (2 Intensity Levels — Unique Values: {unique_1bit})"),
    ]

    for ax, grad, title in levels_info:
        ax.imshow(grad, cmap='gray', vmin=0, vmax=255)
        ax.set_title(title, pad=6, fontsize=11)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_edgecolor('#555555')
            spine.set_linewidth(1.2)

    plt.tight_layout(rect=[0, 0, 1, 0.94])
    bitdepth_fig_path = "bit_depth_comparison.png"
    plt.savefig(bitdepth_fig_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved bit depth comparison figure to: {bitdepth_fig_path}")

    # Explanation of Resolution vs Bit Depth
    diff_explanation = (
        "Explanation of Spatial Resolution vs. Bit Depth:\n"
        "- Spatial Resolution defines the spatial detail of an image represented by the total number of pixels "
        "(width x height, e.g., 640x480 or 1920x1080), which governs fine spatial structures and sharpness.\n"
        "- Bit Depth (Radiometric Resolution) defines the amount of color/tonal information stored per pixel, "
        "determined by the number of bits allocated (e.g., 1-bit yields 2 levels, 8-bit yields 256 levels). "
        "It governs subtle tonal transitions and prevents false contouring (color banding)."
    )
    print(diff_explanation)

    print("\n" + "=" * 70)
    print("Execution completed successfully! All required steps finished without errors.")
    print("=" * 70)


if __name__ == "__main__":
    main()
