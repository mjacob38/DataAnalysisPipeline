from abc import ABC
import pandas as pd
from typing import Tuple
import matplotlib.pyplot as plt
from ..analysis_module.base_strategy import AnalysisStrategy

class VisualizationDecorator(AnalysisStrategy, ABC):
    def __init__(self, strategy: AnalysisStrategy) -> None:
        self.strategy = strategy

    def apply(self, df: pd.DataFrame, **kwargs) -> Tuple[pd.DataFrame, int]:
        return self.strategy.apply(df, **kwargs)
