from flask import Flask, request, jsonify
import torch
import numpy as np
from model import FaceMeshTransformer  # import your model class
import json

# Load label classes
with open("label_classes.json", "r") as f:
    emotion_classes = json.load(f)

# Load model
model = FaceMeshTransformer(num_classes=len(emotion_classes))
model.load_state_dict(torch.load("facemesh_transformer.pth", map_location=torch.device("cpu")))
model.eval()

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    landmarks = np.array(data["landmarks"]).reshape(468, 3)
    input_tensor = torch.tensor(landmarks, dtype=torch.float32).unsqueeze(0)
    
    with torch.no_grad():
        output = model(input_tensor)
        pred = torch.argmax(output, dim=1).item()
        emotion = emotion_classes[pred]
    
    return jsonify({"emotion": emotion})

if __name__ == "__main__":
    app.run(debug=True)
