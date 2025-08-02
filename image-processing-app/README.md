# Image Processing Application

This project is an image processing application that allows users to upload images and convert them to grayscale using different methods. The application provides a graphical user interface (GUI) for ease of use, eliminating the need for terminal commands.

## Project Structure

```
image-processing-app
├── src
│   ├── imageLoading.py  # Main logic for loading and processing images
│   ├── ui.py            # User interface for the application
│   └── types
│       └── index.py     # Custom types and data structures
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Features

- Load images using OpenCV and PIL
- Convert images to grayscale
- Display original and processed images using matplotlib
- User-friendly GUI for image upload

## Requirements

To run this application, you need to install the following dependencies:

- OpenCV
- Pillow
- Matplotlib
- Tkinter or PyQt (for the GUI)

You can install the required packages using pip. Make sure to create a virtual environment for the project:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Install the required dependencies.
4. Run the application:

```bash
python src/ui.py
```

5. Use the graphical interface to upload an image and view the grayscale conversion results.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.