class AnalysisContext:
    def __init__(self, strategy: AnalysisStrategy) -> None:
        self.strategy = strategy

    def set_strategy(self, strategy: AnalysisStrategy) -> None:
        self.strategy = strategy

    def apply_strategy(self, df: pd.DataFrame, **kwargs) -> pd.DataFrame:
        return self.strategy.apply(df, **kwargs)
