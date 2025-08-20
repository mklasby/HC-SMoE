from datasets import load_dataset
import pathlib
import json

# Define the full URL to the specific file on the Hugging Face Hub
# The '/resolve/main/' part is important for accessing the raw file data.
file_url = "https://huggingface.co/datasets/allenai/c4/resolve/main/en/c4-train.00000-of-01024.json.gz"

# Load the dataset using the 'json' builder, specifying the data file and streaming it
# We assign our single file to the 'train' split.
c4_single_file_dataset = load_dataset(
    "json",
    data_files={'train': file_url},
    split='train',
    streaming=False
)

# save dataset to disk
dataset_path = pathlib.Path.cwd() / "hcsmoe/data/c4-train.00000-of-01024.json"
c4_single_file_dataset.to_json(dataset_path)
# with open(dataset_path, 'w') as f:
#     json.dump(c4_single_file_dataset, f)