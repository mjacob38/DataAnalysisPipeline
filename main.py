from data_analysis_pipeline.data_ingest_module.loader_factory import DataLoaderFactory
from data_analysis_pipeline.analysis_module.context import AnalysisContext
from data_analysis_pipeline.analysis_module.strategies import LowPassFilterStrategy, OutlierRemovalStrategy
from data_analysis_pipeline.visualization_module.decorators import PlotDecorator

def main():
    factory = DataLoaderFactory()

    csv_loader = factory.create_data_loader(
        base_path="/home/<USERNAME>/MoCap_data",
        subject_name="P06",
        condition_name="Optimal",
        file_format="csv"
    )

    data, headers = csv_loader.load()

    context = AnalysisContext(strategy=LowPassFilterStrategy())
    filtered_data = context.apply_strategy(
        data, 
        cutoff=10, 
        sample_rate=100, 
        order=4
    )

    decorated_strategy = PlotDecorator(OutlierRemovalStrategy(), marker="Marker_1")
    context.set_strategy(decorated_strategy)
    cleaned_data, num_outliers = context.apply_strategy(
        filtered_data, 
        marker="<MARKERNAME>", 
        window=50, 
        threshold=3
    )

    print(f"Number of outliers removed: {num_outliers}")

if __name__ == "__main__":
    main()