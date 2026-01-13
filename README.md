# Computer Vision Hub: Face & Hand Tracking 🚀

This repository contains two real-time computer vision applications built with **OpenCV**, **Mediapipe**, and **CVZone**. These projects demonstrate the practical application of AI in human-computer interaction.

## 📌 Projects Overview

### 1. Finger Distance Detection
* **Description:** Tracks hand landmarks and calculates the Euclidean distance between the thumb (Landmark 4) and index finger (Landmark 8).
* **Use Case:** Can be extended for volume control, zooming, or virtual sliders.

### 2. Face Mesh & Detection
* **Description:** Detects faces in real-time and overlays a 468-point 3D face mesh.
* **Use Case:** Useful for AR filters, emotion recognition, and face orientation tracking.

## 🛠 Tech Stack
* **Python 3.10+**
* **OpenCV:** For image processing and camera handling.
* **Mediapipe:** Google's framework for high-fidelity body tracking.
* **CVZone:** A wrapper library to simplify Mediapipe implementations.

## 🚀 How to Run

### Prerequisites
Ensure you have Python installed. It is highly recommended to use a virtual environment.

```bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate the environment
# On Windows:
.\venv\Scripts\activate

# 3. Install dependencies
pip install opencv-python cvzone mediapipe
