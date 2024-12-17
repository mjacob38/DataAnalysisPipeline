from abc import ABC, abstractmethod
from typing import Optional
import os

class DataLoader(ABC):
    def __init__(self, base_path: str, subject_name: str, condition_name: str) -> None:
        self.base_path: str = base_path
        self.subject_name: str = subject_name
        self.condition_name: str = condition_name
        self.extension: Optional[str] = None  # To be defined in subclass
        self.file_path: Optional[str] = None  # Set by `_find_file`

    def _find_file(self) -> str:
        """
        Locate the target file in the directory structure based on subject and condition.
        Returns the full file path.
        """
        subject_dir = os.path.join(self.base_path, self.subject_name)
        if not os.path.exists(subject_dir):
            raise FileNotFoundError(f"Subject folder '{subject_dir}' not found.")

        file_name = f"{self.condition_name}{self.extension}"
        file_path = os.path.join(subject_dir, file_name)
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_name}' not found in '{subject_dir}'.")

        return file_path

    @abstractmethod
    def load(self) -> object:
        """Implementation in subclasses."""
        pass