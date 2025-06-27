# 🎲 Number Gusser CNN 🎲
An interactive Streamlit app that lets you **draw a digit (0–9)** and get real-time predictions from a Convolutional Neural Network trained on the MNIST dataset.

---

## 🚀 Live Demo

Try the app here: [Number Gusser CNN on Hugging Face Spaces](https://huggingface.co/spaces/Hardik-z1/NumberGuesserCNN)

---

## ✨ Features

- Freehand canvas to draw digits
- Real-time digit prediction
- Bar chart for confidence visualization
- Custom pre-processing (cropping, padding, centering)

---

## 🛠️ Built With

- **Streamlit** – for the UI
- **TensorFlow/Keras** – for training and inference
- **OpenCV** – for image processing
- **Matplotlib** – for plotting prediction confidences

---

## 📁 Folder Structure  
├── app.py                # Main Streamlit application  
├── requirements.txt      # Python dependencies  
├── best_mnist_model2.h5  # Trained CNN model  
└── README.md             # Info


---

## 🎲 How It Works

1. User draws a digit on canvas
2. Image is:
   - Converted to grayscale
   - Auto-cropped, padded, and resized to 28x28
3. Model trained on the MNIST dataset predicts the digit with probabilities
4. Prediction and confidence bar chart are displayed

---

## 💾 Model

- Dataset: MNIST (70000 samples of [28×28] grayscale digits)
- Accuracy: ~99.2% on validation
- Architecture: 2 Conv blocks + Dropout + Dense layer

---

## ⚙️ Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/mnist-digit-classifier.git
cd mnist-digit-classifier
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the app
```bash
streamlit run app.py
```

Author  
[Hardik (hardik_z1)](https://github.com/hardik-z1/)  
CSE student • ML & Robotics enthusiast
