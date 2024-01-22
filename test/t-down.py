from datasets import Dataset


def down_data(dataset_name, destination_folder):
    dataset = Dataset.load_dataset(dataset_name)
    dataset.download(destination_folder=destination_folder)


down_data('Trelis/function_calling_v3', './function_calling_v4')




