import os
import flor

from torch.utils.data import Dataset
from PIL import Image
import pandas as pd

training_data = flor.pivot("page_path", "first_page")
training_data["page_path"] = training_data["page_path"].apply(os.path.relpath)
training_data = training_data[training_data["filename"] == "infer.py"]
training_data = training_data[training_data["tstamp"] == training_data["tstamp"].max()]
print(training_data.head(n=len(training_data)))
