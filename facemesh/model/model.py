# facemesh/model.py

import torch.nn as nn

class FaceMeshTransformer(nn.Module):
    def __init__(self, input_dim=3, model_dim=64, num_heads=4, num_layers=2, num_classes=5):
        super(FaceMeshTransformer, self).__init__()
        self.embedding = nn.Linear(input_dim, model_dim)
        encoder_layer = nn.TransformerEncoderLayer(d_model=model_dim, nhead=num_heads)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(468 * model_dim, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        x = self.embedding(x)             # (batch, 468, model_dim)
        x = x.permute(1, 0, 2)            # (468, batch, model_dim)
        x = self.transformer_encoder(x)   # (468, batch, model_dim)
        x = x.permute(1, 0, 2)            # (batch, 468, model_dim)
        return self.classifier(x)
