from abc import ABC, abstractmethod
import pandas as pd

class AnalysisStrategy(ABC):
    @abstractmethod
    def apply(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        """
        Apply the analysis strategy to the given DataFrame.

        Parameters:
        - df: Input DataFrame to be processed.

        Returns:
        - Processed DataFrame.
        """
        pass
