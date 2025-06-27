```
---
title: MNIST Digit Classifier
emoji: 🔢
colorFrom: indigo
colorTo: pink
sdk: streamlit
sdk_version: "1.33.0"
app_file: app.py
pinned: false
---

# 🧠 MNIST Digit Classifier - Streamlit App

A clean and interactive Streamlit app that lets you **draw a digit (0–9)** and get a **real-time prediction** from a Convolutional Neural Network trained on the MNIST dataset.

> 🖌️ Draw. 🔍 Predict. 📊 Visualize.

---

## 🚀 Live Demo

Try the hosted app here on [Hugging Face Spaces](https://huggingface.co/spaces/your-username/mnist-digit-classifier)  
*(replace with your real Space URL)*

---

## 🧩 Features

- ✍️ Freehand canvas to draw digits
- 🔢 Trained CNN model predicts drawn digit
- 📈 Confidence bar chart visualizing prediction probabilities
- 🎨 Dark theme matching chart
- 🧠 Custom pre-processing: auto-cropping, centering, padding
- 🌐 Fully deployed on Hugging Face Spaces

---

## 🛠️ Technologies Used

- **TensorFlow / Keras** – CNN model training
- **OpenCV** – Digit extraction, padding, resizing
- **NumPy, Pillow** – Image handling
- **Streamlit** – Web UI
- **Matplotlib** – Horizontal confidence bar chart
- **streamlit-drawable-canvas** – User drawing interface

---

## 📦 Setup Instructions (Local)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mnist-digit-classifier.git
cd mnist-digit-classifier
````


---

## 💾 Model

The model (`best_mnist_model2.h5`) is:

* Trained on the MNIST dataset
* Optimized with dropout, batch norm, ReLU
* Achieves \~99.2% validation accuracy

---

## 📁 File Structure

```
.
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── best_mnist_model2.h5    # Trained CNN model
└── README.md               # This file
```

---

## 🧠 How It Works

1. User draws a digit on the canvas
2. Image is:

   * Converted to grayscale
   * Cropped tightly around the digit
   * Padded & resized to 28x28
3. The processed image is passed to the model
4. Model predicts digit and confidence for all classes
5. Bar chart displays prediction breakdown

---

## 🌍 Deployment

This app is deployed on Hugging Face Spaces using the `streamlit` SDK.
Python 3.10 and TensorFlow 2.12.0 are used to ensure maximum compatibility.

---

## ✨ Future Improvements

* Add support for EMNIST (letters + digits)
* Allow download of canvas as PNG
* Add auto-clear after prediction
* Add webcam digit capture option

---

## 🙌 Author

**Zesha (Zeno Kiv)**
CSE student | ML & Robotics enthusiast
Built during [NullClass](https://nullclass.com) training project

---

## 📜 License

MIT License – use it, remix it, share it 🙌

---

*“Digitally drawing intelligence into the cloud.”*

```

---

Let me know if you'd like:
- A badge layout (accuracy, license, Hugging Face live badge)
- Animated preview or screenshots
- GitHub action to auto-deploy to Hugging Face or rebuild docs

Once you add your Hugging Face Space link and GitHub repo name, I can finalize and beautify it more!
```
