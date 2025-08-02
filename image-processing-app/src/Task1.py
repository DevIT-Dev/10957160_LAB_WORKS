import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog

def load_and_convert_image(image_path):
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found!")
        return
    
    try:
        print("Loading image with OpenCV...")
        original_img = cv2.imread(image_path)
        
        if original_img is None:
            print(f"Error: Could not load image '{image_path}'. Check if it's a valid image file.")
            return
        
        original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
        grayscale_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
        
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(original_img_rgb)
        plt.title('Original Image')
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.imshow(grayscale_img, cmap='gray')
        plt.title('Grayscale Image')
        plt.axis('off')
        
        plt.tight_layout()
        plt.show()
        
        output_path = 'photo_gray.jpg'
        cv2.imwrite(output_path, grayscale_img)
        print(f"Grayscale image saved as '{output_path}'")
        
        print(f"\nImage Information:")
        print(f"Original image shape: {original_img_rgb.shape}")
        print(f"Grayscale image shape: {grayscale_img.shape}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

def alternative_pil_method(image_path):
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found!")
        return
    
    try:
        print("\nAlternative method using PIL...")
        original_img = Image.open(image_path)
        grayscale_img = original_img.convert('L')
        
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(original_img)
        plt.title('Original Image (PIL)')
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.imshow(grayscale_img, cmap='gray')
        plt.title('Grayscale Image (PIL)')
        plt.axis('off')
        
        plt.tight_layout()
        plt.show()
        
        output_path = 'photo_gray_pil.jpg'
        grayscale_img.save(output_path)
        print(f"Grayscale image saved as '{output_path}' using PIL")
        
    except Exception as e:
        print(f"An error occurred with PIL method: {e}")

def manual_grayscale_conversion(image_path):
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found!")
        return
    
    try:
        print("\nManual grayscale conversion method...")
        original_img = cv2.imread(image_path)
        original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
        
        grayscale_manual = np.dot(original_img_rgb[...,:3], [0.299, 0.587, 0.114])
        grayscale_manual = grayscale_manual.astype(np.uint8)
        
        plt.figure(figsize=(15, 5))
        plt.subplot(1, 3, 1)
        plt.imshow(original_img_rgb)
        plt.title('Original Image')
        plt.axis('off')
        
        grayscale_cv2 = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
        plt.subplot(1, 3, 2)
        plt.imshow(grayscale_cv2, cmap='gray')
        plt.title('OpenCV Grayscale')
        plt.axis('off')
        
        plt.subplot(1, 3, 3)
        plt.imshow(grayscale_manual, cmap='gray')
        plt.title('Manual Grayscale')
        plt.axis('off')
        
        plt.tight_layout()
        plt.show()
        
        cv2.imwrite('photo_gray_manual.jpg', grayscale_manual)
        print("Manual grayscale image saved as 'photo_gray_manual.jpg'")
        
    except Exception as e:
        print(f"An error occurred with manual method: {e}")

def upload_image():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    
    if image_path:
        load_and_convert_image(image_path)
        alternative_pil_method(image_path)
        manual_grayscale_conversion(image_path)
    else:
        print("No image selected.")

if __name__ == "__main__":
    print("Image Grayscale Conversion Script")
    print("=" * 40)
    upload_image()