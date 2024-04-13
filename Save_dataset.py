import torch

train_data = {
    'slides': ["CV19-4091.qptiff", "CV20-1400.qptiff"],
    'grid': [
        [(0, 0), (0, 1), (1, 0), (1, 1)],
        [(0, 0), (0, 1), (1, 0), (1, 1)]
        ],
    'targets': [0, 1],
    'mult': 1,
    'level': 0
}

val_data = {
    'slides': ["CV20-6314.qptiff"],
    'grid': [
        [(0, 0), (0, 1), (1, 0), (1, 1)]
        ],
    'targets': [1],
    'mult': 1,
    'level': 0
}

torch.save(train_data, "train_data.pth")
torch.save(val_data, "val_data.pth")