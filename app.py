import streamlit as st
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from streamlit_drawable_canvas import st_canvas

# Load model
model = load_model("best_mnist_model2.keras", compile=False)

st.title(" Draw a Digit - ML number predictor")

st.markdown("Draw a digit (0–9) below. The model will predict it in real time.")


col1, col2 = st.columns([1, 1])  # Adjust the ratio if needed
with col1:
    canvas_result = st_canvas(
        fill_color="#000000",
        stroke_width=15,
        stroke_color="#FFFFFF",
        background_color="#000000",
        height=280,
        width=280,
        drawing_mode="freedraw",
        # key=canvas_key
    )



if canvas_result.image_data is not None:

    # 1. Convert canvas RGBA to grayscale
    img = Image.fromarray((canvas_result.image_data[:, :, 0])).convert("L")
    img = np.array(img)
    img = 255 - img  # White digit on black background

    # 2. Normalize contrast (optional but good for cleaning)
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

    # 3. Strong binary threshold
    _, img_bin = cv2.threshold(255-img, 50, 255, cv2.THRESH_BINARY)

    # 4. Get bounding box of non-zero region
    coords = cv2.findNonZero(img_bin)
    if coords is not None:
        x, y, w, h = cv2.boundingRect(coords)

        # 5. Crop to bounding box
        digit_crop = img_bin[y:y+h, x:x+w]

        # 6. Pad to square
        # Step 1: Pad to square (so resize won't stretch)
        side = max(w, h)
        square = np.zeros((side, side), dtype=np.uint8)
        x_offset = (side - w) // 2
        y_offset = (side - h) // 2
        square[y_offset:y_offset+h, x_offset:x_offset+w] = digit_crop

        # Step 2: Add extra margin around the digit
        padding = 16  # or 8 depending on how much space you want
        padded = cv2.copyMakeBorder(
            square,
            top=padding,
            bottom=padding,
            left=padding,
            right=padding,
            borderType=cv2.BORDER_CONSTANT,
            value=0  # black background
        )

        # 7. Resize to 28x28
        digit_resized = cv2.resize(padded, (28, 28), interpolation=cv2.INTER_AREA)

        # 8. Normalize & reshape
        img_array = digit_resized / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)

        # 9. Predict
        prediction = model.predict(img_array)
        predicted_digit = np.argmax(prediction)
        confidence = prediction[0][predicted_digit] * 100

        st.subheader(f"Prediction: **{predicted_digit}**")
        st.caption(f"Confidence: {confidence:.2f}%")

        # # 🔍 Debug: Show all steps
        # st.image(digit_crop, caption="digit_crop (raw)", width=100)
        # st.image(padded, caption="padded", width=100)
        # st.image(digit_resized, caption="final 28x28", width=100)
    else:
        st.warning("Couldn't detect a digit. Try drawing again.")




with col2:
    if prediction is not None:
        # Plot the horizontal bar chart here
        fig, ax = plt.subplots(figsize=(6, 4))
        bars = ax.barh(range(10), prediction[0], color='skyblue')
        bars[predicted_digit].set_color('orange')

        for i, v in enumerate(prediction[0]):
            ax.text(v + 0.01, i, f"{v*100:.1f}%", va='center', fontsize=8)

        ax.set_yticks(range(10))
        ax.set_yticklabels([str(i) for i in range(10)])
        ax.set_xlabel("Confidence")
        ax.set_title("Confidence for Each Digit")

        # Optional: match dark mode
        ax.set_facecolor('#0e1117')  # dark background
        fig.patch.set_facecolor('#0e1117')
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')

        st.pyplot(fig)
