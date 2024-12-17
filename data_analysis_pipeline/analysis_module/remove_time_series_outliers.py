import pandas as pd
from typing import Tuple

from .base_strategy import AnalysisStrategy

class OutlierRemovalStrategy(AnalysisStrategy):
    def apply(
        self, 
        df: pd.DataFrame, 
        marker: str, 
        window: int = 50, 
        threshold: float = 3
    ) -> Tuple[pd.DataFrame, int]:
        """
        Remove outliers using a moving average and standard deviation method.

        Parameters:
        - df: DataFrame containing the data.
        - marker: The name of the column/marker to process.
        - window: The window size for the moving average and std calculation.
        - threshold: The number of standard deviations from the mean to consider an outlier.

        Returns:
        - DataFrame with outliers removed.
        - Number of outliers removed.
        """
        rolling_mean = df[marker].rolling(window=window).mean()
        rolling_std = df[marker].rolling(window=window).std()

        outliers = (df[marker] < (rolling_mean - threshold * rolling_std)) | \
                   (df[marker] > (rolling_mean + threshold * rolling_std))

        num_outliers = outliers.sum()
        df_outliers_removed = df[~outliers]

        return df_outliers_removed, num_outliers
