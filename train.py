import os
import flor

from torch.utils.data import Dataset, DataLoader
from PIL import Image
import pandas as pd
from torchvision import transforms
from sklearn.model_selection import train_test_split


training_data = flor.pivot("page_path", "first_page")
training_data["page_path"] = training_data["page_path"].apply(os.path.relpath)
training_data = training_data[training_data["filename"] == "infer.py"]
training_data = training_data[training_data["tstamp"] == training_data["tstamp"].max()]
# print(training_data.head(n=len(training_data)))

test_size = flor.arg("test_size", 0.2)
train_data, val_data = train_test_split(training_data, test_size=test_size)
print(val_data.head(n=len(val_data)))


class PDFPagesDataset(Dataset):
    def __init__(self, dataframe, transform=None):
        """
        Args:
            dataframe (Pandas DataFrame): DataFrame with image paths and labels.
            transform (callable, optional): Optional transform to be applied on a sample.
        """
        self.dataframe = dataframe
        self.transform = transform

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, idx):
        img_name = self.dataframe.iloc[
            idx, self.dataframe.columns.index("page_path")
        ]  # adjust column index based on your DataFrame structure
        image = Image.open(img_name)
        label = int(
            self.dataframe.iloc[idx, self.dataframe.columns.index("first_page")]
        )  # adjust column index for labels

        if self.transform:
            image = self.transform(image)

        return image, label


# Define your transformations
transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.RandomCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ]
)

train_dataset = PDFPagesDataset(dataframe=train_data, transform=transform)
val_dataset = PDFPagesDataset(dataframe=val_data, transform=transform)

# Data loaders
batch_size = flor.arg("batch_size", 4)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size)
print(train_loader)
