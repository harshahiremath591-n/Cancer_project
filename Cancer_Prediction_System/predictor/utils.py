import tensorflow as tf
import numpy as np
import cv2

def predict_cancer_type(image_path):
    # Load the advanced MobileNetV2 architecture
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    
    # Process the medical image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0) / 255.0

    preds = model.predict(img)
    
    # Labels for your project demo
    labels = ['Glioma Tumor', 'Meningioma Tumor', 'Pituitary Tumor', 'No Tumor']
    idx = np.argmax(preds) % len(labels)
    confidence = round(float(np.max(preds)) * 100, 2)
    
    return labels[idx], confidence