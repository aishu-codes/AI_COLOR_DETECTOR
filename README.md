# 🎨 AI Color Detector

A professional Computer Vision application that identifies over 800+ color names in real-time by analyzing pixel data from images. This project uses mathematical distance algorithms to map RGB values to human-readable color names.

## 📖 Project Overview
This tool allows users to interact with any image and instantly retrieve the **Color Name**, **HEX Code**, and **RGB values** of any specific pixel. It is designed with a high-resolution fullscreen interface for a premium user experience.

## ✨ Key Features
- **Delta-E Distance Algorithm:** Accurately calculates the closest color match from a dataset of 865 colors.
- **Interactive UI:** Double-click functionality to pick colors instantly.
- **Dynamic Text Overlay:** Smart text rendering that changes color (Black/White) based on background brightness for maximum readability.
- **Auto-Scaling:** Automatically resizes images to fit 1080p displays without distortion.

## 🚀 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd AI-Color-Detector
   ```

2. **Install Dependencies:**
   ```bash
   pip install opencv-python pandas
   ```

3. **Run the App:**
   ```bash
   python main.py
   ```
   *Note: Double-click anywhere on the image to detect the color. Press **'Esc'** to exit.*

## 🛠️ Tech Stack
- **Python**: Core logic.
- **OpenCV**: Image processing and window management.
- **Pandas**: Efficient handling of the `colors.csv` dataset.
- **NumPy**: Matrix operations for pixel data.

## 📁 Dataset
The project uses a standard `colors.csv` dataset containing:
- Color Name
- Hexadecimal Code
- RGB (Red, Green, Blue) values

---
Developed by [aishu.codes](https://github.com) 🚀
