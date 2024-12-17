from .base_visualization import VisualizationDecorator

class PlotDecorator(VisualizationDecorator):
    def __init__(self, strategy: AnalysisStrategy, marker: str) -> None:
        super().__init__(strategy)
        self.marker = marker

    def apply(self, df: pd.DataFrame, **kwargs) -> Tuple[pd.DataFrame, int]:
        result = self.strategy.apply(df, **kwargs)

        if isinstance(result, tuple):
            modified, _ = result
        else:
            modified = result

        self._plot_data(df, modified, self.marker)

        return result

    def _plot_data(self, original: pd.DataFrame, modified: pd.DataFrame, marker: str) -> None:
        """Plot original and modified data."""

        plt.figure(figsize=(15, 7))
        plt.plot(original.index, original[marker], label=f'Original {marker}', color='lightblue', alpha=0.7)
        plt.plot(modified.index, modified[marker], label=f'Cleaned {marker}', color='blue')
        plt.legend(loc='upper right')
        plt.title(f'{marker} - Original vs Cleaned')
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.show()
