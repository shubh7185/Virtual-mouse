# AI Virtual Mouse Project

This project implements an AI-based virtual mouse using hand gestures detected through a webcam. The project leverages OpenCV for video capture, MediaPipe for hand tracking, and Autopy for controlling mouse movements. The virtual mouse can move the cursor and perform click actions based on the position of your fingers.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-virtual-mouse.git
   cd ai-virtual-mouse
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure your webcam is connected and accessible.**

## Usage

1. **Run the AI Virtual Mouse script:**
   ```bash
   python AiVirtualMouseProject.py
   ```

2. **Use your hand gestures to control the mouse:**
   - **Index Finger Up**: Move the cursor.
   - **Index and Middle Finger Up**: Click action when fingers are brought together.

3. **Press `q` to exit the program.**

## Features

- Real-time hand tracking using MediaPipe.
- Smooth cursor movement using a custom smoothing algorithm.
- Click detection based on finger distance.
- Adjustable frame size and sensitivity.

## Dependencies

- **Python 3.7+**
- **OpenCV**
- **MediaPipe**
- **NumPy**
- **Autopy**

You can install these dependencies using the `requirements.txt` file provided.

## How It Works

The AI Virtual Mouse uses a combination of computer vision and AI techniques:

1. **Hand Tracking**: MediaPipe's hand tracking solution detects hand landmarks in real-time.
2. **Gesture Recognition**: Based on the landmarks, specific gestures (like fingers up) are recognized.
3. **Cursor Movement**: The detected gestures are used to control the mouse cursor's movement and clicking actions using Autopy.

## Troubleshooting

- **ImportError with `matplotlib`**: If you encounter errors related to `matplotlib`, ensure that the package is properly installed in your virtual environment. Try reinstalling it with:
  ```bash
  pip uninstall matplotlib
  pip install matplotlib
  ```

- **Webcam not detected**: Ensure your webcam is connected and properly recognized by the system. Check if it works with other applications.

## Contributing

Contributions are welcome! Please fork this repository, create a new branch, and submit a pull request with your changes.
