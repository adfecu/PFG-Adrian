import torch

tile_size = 224

x_coords = list(range(2500, 45000, tile_size))
y_coords = list(range(16000, 60000, tile_size))

coordinates = [(x, y) for y in y_coords for x in x_coords]

train_data = {
    'slides': ["CV19-4091.qptiff", "CV20-1400.qptiff"],
    'grid': [
        [coordinates for _ in range(2)]
    ],
    'targets': [0, 1],
    'mult': 1,
    'level': 0
}

val_data = {
    'slides': ["CV20-6314.qptiff"],
    'grid': [
        [coordinates for _ in range(1)]
    ],
    'targets': [1],
    'mult': 1,
    'level': 0
}

torch.save(train_data, "train_data.pth")
torch.save(val_data, "val_data.pth")