from typing import Type

from .base_loader import DataLoader
from .csv_loader import CSVLoader

class DataLoaderFactory:
    loaders = {}

    @classmethod
    def register_loader(cls, file_format: str):
        def decorator(loader_cls):
            cls.loaders[file_format] = loader_cls
            return loader_cls
        return decorator

    @classmethod
    def create_data_loader(cls, base_path: str, subject_name: str, condition_name: str, file_format: str) -> DataLoader:
        if file_format not in cls.loaders:
            raise ValueError(f"Unsupported file format: {file_format}")
        return cls.loaders[file_format](base_path, subject_name, condition_name)
