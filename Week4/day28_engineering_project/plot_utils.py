from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_target_plot(df: pd.DataFrame, target_column: str, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    plot_path = output_dir / f"{target_column}_distribution.png"

    plt.figure(figsize=(8, 4))
    if pd.api.types.is_numeric_dtype(df[target_column]):
        df[target_column].hist(bins=20)
        plt.ylabel("count")
    else:
        df[target_column].value_counts().plot(kind="bar")
        plt.ylabel("frequency")

    plt.title(f"Distribution of {target_column}")
    plt.xlabel(target_column)
    plt.tight_layout()
    plt.savefig(plot_path)
    plt.close()
    return plot_path
