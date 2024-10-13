
# Workspace Analysis App

This is a web-based application that uses machine learning to analyze workspace images. The app allows users to upload images of their workspace, which are then analyzed for various factors such as object count, back support, and screen distance. The app provides a user-friendly interface for submitting images and viewing analysis results.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Methods and Libraries](#methods-and-libraries)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the Repository**
   ```
   https://github.com/Awezsk/Mind-lens-app.git
   cd workspace-analysis-app
   ```

2. **Install the Required Libraries**
   Use `pip` to install the necessary libraries:
   ```
   pip install -r requirements.txt
   ```
   Create a `requirements.txt` file with the following contents:
   ```
   Flask
   numpy
   Pillow
   tensorflow
   keras
   matplotlib
   opencv-python
   ```

3. **Running the Application**
   ```
   python app.py
   ```

   The app will be accessible at `http://localhost:5000` in your web browser.

## Usage

1. Open the app in your web browser (`http://localhost:5000`).
2. Upload an image of your workspace using the provided form.
3. Click "Analyze Workspace" to submit the image for analysis.
4. The app will analyze the uploaded image and display the results, including object count, back support assessment, and screen distance information.

## Features

- **Object Count**: Detects and counts various objects in the workspace image.
- **Back Support Analysis**: Analyzes the presence and type of back support.
- **Screen Distance Measurement**: Estimates the distance between the screen and the user.
- **Real-Time Feedback**: Displays analysis results, including the processed image.

## Methods and Libraries

### Python Scripts

- **`app.py`**: The main Flask application that handles image uploads and analysis requests.
- **`image_analysis.py`**: Contains functions for analyzing the uploaded images, including object detection, back support analysis, and screen distance estimation.

### JavaScript

- **Frontend Interaction**: The JavaScript in the `index.html` handles form submission, loading states, and displaying results to the user.
- **Fetch API**: Used to send the uploaded image to the server for analysis.

### Libraries

- **Flask**: For creating the web server and handling requests.
- **NumPy**: For numerical operations on image data.
- **Pillow (PIL)**: For image processing.
- **TensorFlow/Keras**: Used for any deep learning models applied in the analysis.
- **Matplotlib**: Optional, for visualizing image processing results.
- **OpenCV**: For image processing tasks.

## File Structure

```
workspace-analysis-app/
├── app.py                   # Main server script
├── image_analysis.py        # Image processing and analysis functions
├── templates/
│   └── index.html           # Main HTML file for the app
├── static/
│   ├── css/                 # Stylesheets (if any)
│   └── images/              # Default images for the app
└── requirements.txt         # Required Python libraries
```

## Contributing

1. Fork the project.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

##Output Example for one of the image
![Alt Text](images/workspace-example.png)

## License

This project is licensed under the MIT License.

