import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.gridspec import GridSpec
import tkinter as tk
from tkinter import filedialog

def load_and_convert_color_spaces(image_path):
    """
    Load an image and convert it to different color spaces: Grayscale, HSV, and LAB.
    Display all the converted images.
    
    Args:
        image_path (str): Path to the input image file
    """
    
    # Check if image file exists
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found!")
        return
    
    try:
        # Load the original image
        print(f"Loading image: {image_path}")
        original_bgr = cv2.imread(image_path)
        
        if original_bgr is None:
            print(f"Error: Could not load image '{image_path}'. Check if it's a valid image file.")
            return
        
        # Convert BGR to RGB for proper display
        original_rgb = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2RGB)
        
        # Color space conversions
        print("Converting to different color spaces...")
        
        # 1. Grayscale conversion
        grayscale = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2GRAY)
        
        # 2. HSV conversion
        hsv = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2HSV)
        
        # 3. LAB conversion
        lab = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2LAB)
        
        # Display all images in a grid
        display_color_spaces(original_rgb, grayscale, hsv, lab)
        
        # Display individual channels for HSV and LAB
        display_hsv_channels(hsv)
        display_lab_channels(lab)
        
        # Save converted images
        save_converted_images(grayscale, hsv, lab, image_path)
        
        # Print image information
        print_image_info(original_rgb, grayscale, hsv, lab)
        
    except Exception as e:
        print(f"An error occurred: {e}")

def display_color_spaces(original, grayscale, hsv, lab):
    """
    Display original and converted images in a 2x2 grid.
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Color Space Conversions', fontsize=16, fontweight='bold')
    
    # Original RGB
    axes[0, 0].imshow(original)
    axes[0, 0].set_title('Original (RGB)', fontweight='bold')
    axes[0, 0].axis('off')
    
    # Grayscale
    axes[0, 1].imshow(grayscale, cmap='gray')
    axes[0, 1].set_title('Grayscale', fontweight='bold')
    axes[0, 1].axis('off')
    
    # HSV (Note: HSV needs special handling for display)
    hsv_display = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    axes[1, 0].imshow(hsv_display)
    axes[1, 0].set_title('HSV (converted back to RGB for display)', fontweight='bold')
    axes[1, 0].axis('off')
    
    # LAB (Note: LAB needs special handling for display)
    lab_display = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    axes[1, 1].imshow(lab_display)
    axes[1, 1].set_title('LAB (converted back to RGB for display)', fontweight='bold')
    axes[1, 1].axis('off')
    
    plt.tight_layout()
    plt.show()

def display_hsv_channels(hsv):
    """
    Display individual HSV channels.
    """
    # Split HSV channels
    h, s, v = cv2.split(hsv)
    
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    fig.suptitle('HSV Color Space - Individual Channels', fontsize=16, fontweight='bold')
    
    # Full HSV
    hsv_display = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    axes[0].imshow(hsv_display)
    axes[0].set_title('HSV Combined', fontweight='bold')
    axes[0].axis('off')
    
    # Hue channel
    axes[1].imshow(h, cmap='hsv')
    axes[1].set_title('Hue Channel', fontweight='bold')
    axes[1].axis('off')
    
    # Saturation channel
    axes[2].imshow(s, cmap='gray')
    axes[2].set_title('Saturation Channel', fontweight='bold')
    axes[2].axis('off')
    
    # Value channel
    axes[3].imshow(v, cmap='gray')
    axes[3].set_title('Value Channel', fontweight='bold')
    axes[3].axis('off')
    
    plt.tight_layout()
    plt.show()

def display_lab_channels(lab):
    """
    Display individual LAB channels.
    """
    # Split LAB channels
    l, a, b = cv2.split(lab)
    
    fig, axes = plt.subplots(1, 4, figsize=(16, 4))
    fig.suptitle('LAB Color Space - Individual Channels', fontsize=16, fontweight='bold')
    
    # Full LAB
    lab_display = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    axes[0].imshow(lab_display)
    axes[0].set_title('LAB Combined', fontweight='bold')
    axes[0].axis('off')
    
    # L channel (Lightness)
    axes[1].imshow(l, cmap='gray')
    axes[1].set_title('L Channel (Lightness)', fontweight='bold')
    axes[1].axis('off')
    
    # A channel (Green-Red)
    axes[2].imshow(a, cmap='RdYlGn_r')
    axes[2].set_title('A Channel (Green-Red)', fontweight='bold')
    axes[2].axis('off')
    
    # B channel (Blue-Yellow)
    axes[3].imshow(b, cmap='RdYlBu_r')
    axes[3].set_title('B Channel (Blue-Yellow)', fontweight='bold')
    axes[3].axis('off')
    
    plt.tight_layout()
    plt.show()

def create_color_space_comparison(original_rgb, grayscale, hsv, lab):
    """
    Create a comprehensive comparison showing original and all conversions.
    """
    fig = plt.figure(figsize=(20, 15))
    gs = GridSpec(4, 4, figure=fig)
    
    # Original image (larger)
    ax_orig = fig.add_subplot(gs[0, :2])
    ax_orig.imshow(original_rgb)
    ax_orig.set_title('Original RGB Image', fontsize=14, fontweight='bold')
    ax_orig.axis('off')
    
    # Grayscale
    ax_gray = fig.add_subplot(gs[0, 2:])
    ax_gray.imshow(grayscale, cmap='gray')
    ax_gray.set_title('Grayscale Conversion', fontsize=14, fontweight='bold')
    ax_gray.axis('off')
    
    # HSV channels
    h, s, v = cv2.split(hsv)
    ax_h = fig.add_subplot(gs[1, 0])
    ax_h.imshow(h, cmap='hsv')
    ax_h.set_title('HSV - Hue', fontweight='bold')
    ax_h.axis('off')
    
    ax_s = fig.add_subplot(gs[1, 1])
    ax_s.imshow(s, cmap='gray')
    ax_s.set_title('HSV - Saturation', fontweight='bold')
    ax_s.axis('off')
    
    ax_v = fig.add_subplot(gs[1, 2])
    ax_v.imshow(v, cmap='gray')
    ax_v.set_title('HSV - Value', fontweight='bold')
    ax_v.axis('off')
    
    ax_hsv = fig.add_subplot(gs[1, 3])
    hsv_display = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    ax_hsv.imshow(hsv_display)
    ax_hsv.set_title('HSV Combined', fontweight='bold')
    ax_hsv.axis('off')
    
    # LAB channels
    l, a, b = cv2.split(lab)
    ax_l = fig.add_subplot(gs[2, 0])
    ax_l.imshow(l, cmap='gray')
    ax_l.set_title('LAB - Lightness', fontweight='bold')
    ax_l.axis('off')
    
    ax_a = fig.add_subplot(gs[2, 1])
    ax_a.imshow(a, cmap='RdYlGn_r')
    ax_a.set_title('LAB - A (Green-Red)', fontweight='bold')
    ax_a.axis('off')
    
    ax_b = fig.add_subplot(gs[2, 2])
    ax_b.imshow(b, cmap='RdYlBu_r')
    ax_b.set_title('LAB - B (Blue-Yellow)', fontweight='bold')
    ax_b.axis('off')
    
    ax_lab = fig.add_subplot(gs[2, 3])
    lab_display = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    ax_lab.imshow(lab_display)
    ax_lab.set_title('LAB Combined', fontweight='bold')
    ax_lab.axis('off')
    
    plt.suptitle('Complete Color Space Analysis', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.show()

def save_converted_images(grayscale, hsv, lab, original_path):
    """
    Save the converted images to disk.
    """
    base_name = os.path.splitext(os.path.basename(original_path))[0]
    
    # Save grayscale
    cv2.imwrite(f'{base_name}_grayscale.jpg', grayscale)
    
    # Save HSV (convert back to BGR for saving)
    hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite(f'{base_name}_hsv.jpg', hsv_bgr)
    
    # Save LAB (convert back to BGR for saving)
    lab_bgr = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    cv2.imwrite(f'{base_name}_lab.jpg', lab_bgr)
    
    print(f"\nSaved converted images:")
    print(f"- {base_name}_grayscale.jpg")
    print(f"- {base_name}_hsv.jpg")
    print(f"- {base_name}_lab.jpg")

def print_image_info(original, grayscale, hsv, lab):
    """
    Print information about the images and color spaces.
    """
    print(f"\n{'='*50}")
    print("IMAGE INFORMATION")
    print(f"{'='*50}")
    print(f"Original RGB shape: {original.shape}")
    print(f"Grayscale shape: {grayscale.shape}")
    print(f"HSV shape: {hsv.shape}")
    print(f"LAB shape: {lab.shape}")
    
    print(f"\n{'='*50}")
    print("COLOR SPACE INFORMATION")
    print(f"{'='*50}")
    print("RGB: Red, Green, Blue - Standard color representation")
    print("Grayscale: Single channel representing luminance")
    print("HSV: Hue, Saturation, Value - More intuitive for color manipulation")
    print("  - Hue: Color type (0-179 in OpenCV)")
    print("  - Saturation: Color purity (0-255)")
    print("  - Value: Color brightness (0-255)")
    print("LAB: Lightness, A (green-red), B (blue-yellow) - Perceptually uniform")
    print("  - L: Lightness (0-100, scaled to 0-255 in OpenCV)")
    print("  - A: Green-Red axis (-128 to +127, scaled to 0-255)")
    print("  - B: Blue-Yellow axis (-128 to +127, scaled to 0-255)")

def analyze_color_distribution(original_rgb, hsv, lab):
    """
    Create histograms for different color spaces.
    """
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    fig.suptitle('Color Distribution Analysis', fontsize=16, fontweight='bold')
    
    # RGB histograms
    colors = ['red', 'green', 'blue']
    for i, color in enumerate(colors):
        axes[0, i].hist(original_rgb[:,:,i].ravel(), bins=256, color=color, alpha=0.7)
        axes[0, i].set_title(f'RGB - {color.capitalize()} Channel')
        axes[0, i].set_xlabel('Pixel Value')
        axes[0, i].set_ylabel('Frequency')
    
    # HSV histograms
    hsv_labels = ['Hue', 'Saturation', 'Value']
    hsv_colors = ['rainbow', 'gray', 'gray']
    for i, (label, color) in enumerate(zip(hsv_labels, hsv_colors)):
        if i == 0:  # Hue channel
            axes[1, i].hist(hsv[:,:,i].ravel(), bins=180, color='purple', alpha=0.7)
        else:
            axes[1, i].hist(hsv[:,:,i].ravel(), bins=256, color='purple', alpha=0.7)
        axes[1, i].set_title(f'HSV - {label}')
        axes[1, i].set_xlabel('Pixel Value')
        axes[1, i].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.show()

def select_image_via_ui():
    """
    Open a file dialog for the user to select an image.
    Returns the selected image path or None.
    """
    root = tk.Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")]
    )
    return image_path if image_path else None

if __name__ == "__main__":
    print("Color Space Conversion Script")
    print("=" * 50)

    # Use UI to select image
    image_filename = select_image_via_ui()
    if not image_filename:
        print("No image selected. Exiting.")
    elif os.path.exists(image_filename):
        # Load and convert the image
        load_and_convert_color_spaces(image_filename)

        # For additional analysis, reload the image for histogram analysis
        original_bgr = cv2.imread(image_filename)
        if original_bgr is not None:
            original_rgb = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2RGB)
            hsv = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2HSV)
            lab = cv2.cvtColor(original_bgr, cv2.COLOR_BGR2LAB)

            # Create comprehensive comparison
            create_color_space_comparison(original_rgb,
                                         cv2.cvtColor(original_bgr, cv2.COLOR_BGR2GRAY),
                                         hsv, lab)

            # Analyze color distribution
            analyze_color_distribution(original_rgb, hsv, lab)
    else:
        print(f"Image file '{image_filename}' not found. Please check the file path.")
        print("\nTo use this script:")
        print("1. Place an image file named 'photo.jpg' in the same directory, or")
        print("2. Run the script and enter the path to your image file when prompted")