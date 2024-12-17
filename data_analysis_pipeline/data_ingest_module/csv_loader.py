import pandas as pd
from typing import List, Tuple

from .base_loader import DataLoader

@DataLoaderFactory.register_loader("csv")
class CSVLoader(DataLoader):
    def __init__(self, base_path: str, subject_name: str, condition_name: str) -> None:
        super().__init__(base_path, subject_name, condition_name)
        self.extension: str = ".csv"
        self.file_path: str = self._find_file()
        self.skiprows_headers: int = 2
        self.skiprows_data: int = 5
        self.header_main_row: int = 2

    def _extract_headers(self) -> List[str]:
        """Extract and combine main headers and axis."""
        try:
            csv_preview = pd.read_csv(
                self.file_path, 
                skiprows=self.header_main_row, 
                header=None, 
                nrows=1
            )

            main_headers = csv_preview.iloc[0].tolist()
        except Exception as e:
            raise ValueError(f"Error reading headers from file: {e}")

        combined_headers = ["Index", "Time"]
        for i in range(2, len(main_headers)):
            if pd.notna(main_headers[i]):
                combined_headers.extend([f"{main_headers[i]} {axis}" for axis in ['X', 'Y', 'Z']])

        return combined_headers

    def load(self) -> Tuple[pd.DataFrame, List[str]]:
        """Load data from .csv and drop NaN."""
        headers = self._extract_headers()

        try:
            data = pd.read_csv(
                self.file_path,
                skiprows=self.skiprows_data,
                header=None,
                names=headers,
                usecols=range(2, len(headers))
            )
        except Exception as e:
            raise ValueError(f"Error loading data: {e}")

        data = data.dropna(axis=0)  # Drop rows with NaN

        return data, headers