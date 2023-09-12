from typing import Dict


def django_filter(obj: Model) -> Dict[str, object]:
    # Get the model's fields as a dictionary
    model_dict = obj.__dict__.copy()

    # Remove internal Django fields that start with an underscore
    for key in list(model_dict.keys()):
        if key.startswith("_"):
            del model_dict[key]

    # Optionally, you can customize the dictionary further if needed
    # For example, renaming fields or processing data

    return model_dict
