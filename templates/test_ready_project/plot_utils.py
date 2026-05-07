from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def save_target_histogram(
    df: pd.DataFrame, target_column: str, output_dir: Path
) -> None:
    plt.figure(figsize=(8, 4))
    df[target_column].hist(bins=20)
    plt.title(f"Distribution of {target_column}")
    plt.xlabel(target_column)
    plt.ylabel("count")
    plt.tight_layout()
    plt.savefig(output_dir / f"{target_column}_hist.png")
    plt.close()


def save_feature_scatter(
    df: pd.DataFrame, feature_column: str, target_column: str, output_dir: Path
) -> None:
    plt.figure(figsize=(8, 4))
    plt.scatter(df[feature_column], df[target_column], alpha=0.7)
    plt.title(f"{feature_column} vs {target_column}")
    plt.xlabel(feature_column)
    plt.ylabel(target_column)
    plt.tight_layout()
    plt.savefig(output_dir / f"{feature_column}_vs_{target_column}.png")
    plt.close()


def save_quick_plots(df: pd.DataFrame, target_column: str, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    if target_column not in numeric_columns:
        return

    save_target_histogram(df, target_column, output_dir)

    feature_candidates = [
        column for column in numeric_columns if column != target_column
    ]
    if not feature_candidates:
        return

    first_feature = feature_candidates[0]
    save_feature_scatter(df, first_feature, target_column, output_dir)
