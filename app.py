import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
st.set_page_config(page_title="Fire Detection AI", page_icon="🔥", layout="centered")
# CNN Model (must match training architecture)
class FireCNN(nn.Module):
    def __init__(self):
        super(FireCNN, self).__init__()

        self.conv_layers = nn.Sequential(
            nn.Conv2d(3, 16, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(16, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )

        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 16 * 16, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 2)
        )

    def forward(self, x):
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x


# Load model
model = FireCNN()
model.load_state_dict(torch.load("fire_detection_model.pth", map_location="cpu"))
model.eval()

# Transform
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
])

classes = ["fire", "nofire"]

# UI
st.title("🔥 Fire Detection System (CNN)")
st.write("Upload an image to detect fire or no fire")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, use_container_width=True)

    img = transform(image).unsqueeze(0)

    with torch.no_grad():
        output = model(img)

        probabilities = torch.nn.functional.softmax(output, dim=1)
        confidence, predicted = torch.max(probabilities, 1)

    st.subheader(f"Prediction: {classes[predicted.item()]}")
    st.write(f"Confidence: {confidence.item() * 100:.2f}%")

    st.bar_chart(probabilities.numpy())