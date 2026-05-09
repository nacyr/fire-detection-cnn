🔥 Fire Detection System using CNN (PyTorch + Streamlit)
📌 Project Overview

This project is a deep learning-based Fire Detection System built using a Convolutional Neural Network (CNN) in PyTorch. The model classifies images into two categories:

🔥 Fire
🌫 No Fire

The system is deployed using Streamlit, allowing users to upload images and receive real-time predictions with confidence scores.

🌐 Live Demo

👉 https://fire-detection-cnn-d9ejbubagpxkpkpyqznjo2.streamlit.app/

🧠 Problem Statement

Fire incidents in industrial environments such as oil & gas facilities can lead to severe damage, loss of life, and financial loss. This project aims to develop an AI-based system for early fire detection using image classification, improving response time and safety.

⚙️ Tech Stack
Python 🐍
PyTorch 🤖
Convolutional Neural Networks (CNN)
Streamlit 🌐
Computer Vision 👁️
📊 Model Performance
Test Accuracy: ~93%
High Recall for Fire Detection (important for safety systems)
Reliable classification of fire vs no-fire images
🏗️ Model Architecture

The CNN model consists of:

3 Convolutional Layers
ReLU Activation Functions
MaxPooling Layers
Fully Connected Layers
Dropout for Regularization
Output Layer (2 classes: fire / nofire)
🚀 Features
Upload image for prediction
Real-time fire detection
Confidence score display
Probability visualization
Simple and interactive UI
📂 Project Structure
fire-detection-cnn/
│
├── app.py                     # Streamlit application
├── fire_detection_model.pth   # Trained CNN model
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/nacyr/fire-detection-cnn.git
cd fire-detection-cnn
2. Install dependencies
pip install -r requirements.txt
3. Run the application
streamlit run app.py
📸 How It Works
User uploads an image
Image is preprocessed (resized and normalized)
CNN model predicts class (fire / nofire)
Output is displayed with confidence score
🔥 Real-World Application

This system can be used in:

Oil & Gas safety monitoring
Industrial fire detection systems
Smart surveillance cameras
Emergency response systems
📈 Key Learnings
Building CNN models using PyTorch
Image preprocessing techniques
Model evaluation (accuracy, precision, recall)
Deployment using Streamlit
End-to-end AI system development
⚠️ Limitations
Performance depends on dataset quality
May produce false positives in complex environments
Requires improvement with larger datasets
🚀 Future Improvements
Integrate video-based fire detection
Use advanced models (ResNet, EfficientNet)
Improve UI design
Add real-time camera detection
Deploy on scalable cloud infrastructure
🙏 Acknowledgements

Special thanks to:

Open-source deep learning community
Dataset providers
AI/ML learning platforms
👨‍💻 Author

Nasir Armiyau

📌 Conclusion

This project demonstrates an end-to-end AI system for fire detection using deep learning. It successfully integrates model training, evaluation, and deployment into a real-world usable application.
