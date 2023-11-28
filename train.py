import os
import flor


training_data = flor.pivot("page_path", "first_page")
training_data["page_path"] = training_data["page_path"].apply(os.path.relpath)
print(training_data.values)
