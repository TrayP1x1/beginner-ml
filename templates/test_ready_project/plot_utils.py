from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_quick_plots(df: pd.DataFrame, target_column: str, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    if target_column not in numeric_columns:
        return

    plt.figure(figsize=(8, 4))
    df[target_column].hist(bins=20)
    plt.title(f"Distribution of {target_column}")
    plt.xlabel(target_column)
    plt.ylabel("count")
    plt.tight_layout()
    plt.savefig(output_dir / f"{target_column}_hist.png")
    plt.close()

    feature_candidates = [column for column in numeric_columns if column != target_column]
    if not feature_candidates:
        return

    first_feature = feature_candidates[0]
    plt.figure(figsize=(8, 4))
    plt.scatter(df[first_feature], df[target_column], alpha=0.7)
    plt.title(f"{first_feature} vs {target_column}")
    plt.xlabel(first_feature)
    plt.ylabel(target_column)
    plt.tight_layout()
    plt.savefig(output_dir / f"{first_feature}_vs_{target_column}.png")
    plt.close()
