import tkinter as tk
from tkinter import filedialog, messagebox
import imageLoading

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="Upload an Image for Processing", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.process_button = tk.Button(root, text="Process Image", command=self.process_image, state=tk.DISABLED)
        self.process_button.pack(pady=10)

        self.image_path = None

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(title="Select an Image",
                                                      filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
        if self.image_path:
            messagebox.showinfo("Image Selected", f"Image uploaded: {self.image_path}")
            self.process_button.config(state=tk.NORMAL)

    def process_image(self):
        if self.image_path:
            imageLoading.load_and_convert_image(self.image_path)
        else:
            messagebox.showwarning("No Image", "Please upload an image first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()