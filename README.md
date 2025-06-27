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

---

## 🚀 Live Demo

[Click here to try the app](https://huggingface.co/spaces/your-username/mnist-digit-classifier)

---

## 🧩 Features

- ✍️ Freehand drawing canvas
- 🔢 Real-time digit classification
- 📈 Horizontal confidence bar chart
- 🧠 Auto-cropping, centering, and padding
- 🌐 Deployed on Hugging Face Spaces

---

## 📦 Tech Stack

- TensorFlow / Keras
- OpenCV
- Streamlit
- Matplotlib
- streamlit-drawable-canvas

---

## 📁 Project Structure
├── app.py
├── requirements.txt
├── best_mnist_model2.h5
└── README.md


---

## 🧠 How It Works

1. User draws a digit
2. Image is cleaned, centered, padded, resized to 28×28
3. CNN model predicts digit class + confidence
4. Result and confidence bar chart are shown

---

## ✨ Future Ideas

- Add support for EMNIST (letters)
- Enable webcam-based digit input
- Auto-clear canvas after prediction

---

## 🙌 Author

**Zesha (Zeno Kiv)**  
CSE + ML + Robotics  
Built during NullClass training

---

## 📜 License

MIT
