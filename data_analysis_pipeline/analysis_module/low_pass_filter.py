from scipy.signal import butter, filtfilt
import pandas as pd

from .base_strategy import AnalysisStrategy

class LowPassFilterStrategy(AnalysisStrategy):
    def apply(self, df: pd.DataFrame, cutoff=10, sample_rate=100, order=4) -> pd.DataFrame:
        """
        Apply a low-pass Butterworth filter to the data.

        Parameters:
        - df: DataFrame containing the data to be filtered
        - cutoff: Cutoff frequency of the filter (default is 10Hz)
        - sample_rate: Sampling rate of the data (default is 100 samples per second)
        - order: Order of the Butterworth filter (default is 4)

        Returns:
        - Filtered data as a DataFrame with the same structure as the input
        """
        nyquist = 0.5 * sample_rate
        normalized_cutoff = cutoff / nyquist
        b, a = butter(order, normalized_cutoff, btype='low', analog=False)

        filtered_df = df.apply(lambda col: filtfilt(b, a, col))

        return filtered_df
