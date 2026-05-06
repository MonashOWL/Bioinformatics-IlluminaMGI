# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 16:34:39 2025

@author: Timothy

Note that this is only applicable for folder that contains stout1 to stout5 (i.e., standard SourceTracker output) 
Please do not use this script for Leave one out compilation
v1.3: Omission of RSD>=1 results, with a sheet to track which ones got omitted using words/warning
"""

import os
import pandas as pd
import numpy as np

# --- Specify paths here ---
input_base_dir = r""
output_dir = r""
output_path = os.path.join(output_dir, "stout_results.xlsx")
source_sample_id = "Unknown"
# ---------------------------

def process_stout_data(base_dir):
    proportion_dfs = []
    std_dfs = []
    relative_contrib_runs = []

    # --- Load stout1 to stout5 ---
    for i in range(1, 6):
        folder = os.path.join(base_dir, f"stout{i}")
        prop_path = os.path.join(folder, "mixing_proportions.txt")
        std_path = os.path.join(folder, "mixing_proportions_stds.txt")

        if not (os.path.exists(prop_path) and os.path.exists(std_path)):
            print(f"Missing files in {folder}")
            continue

        prop_df = pd.read_csv(prop_path, sep="\t", index_col=0)
        std_df = pd.read_csv(std_path, sep="\t", index_col=0)

        proportion_dfs.append(prop_df)
        std_dfs.append(std_df)

        # Relative contributions (excluding Unknown)
        df_no_unknown = prop_df.drop(columns=[source_sample_id], errors="ignore")
        sum_sources = df_no_unknown.sum(axis=1).replace(0, np.nan)
        rel_contrib = df_no_unknown.div(sum_sources, axis=0)
        relative_contrib_runs.append(rel_contrib)

    if len(proportion_dfs) < 5:
        print("⚠️ Warning: Fewer than 5 replicates found. Median calculations may be limited.")

    # --- Median raw proportions ---
    all_props_stack = pd.concat(proportion_dfs, keys=range(len(proportion_dfs)))
    median_props = all_props_stack.groupby(level=1).median()

    # --- Median relative contributions ---
    rel_contrib_stack = pd.concat(relative_contrib_runs, keys=range(len(relative_contrib_runs)))
    median_rel_contrib = rel_contrib_stack.groupby(level=1).median()

    # --- Compute RSD for each run ---
    rel_std_runs = []
    for prop_df, std_df in zip(proportion_dfs, std_dfs):
        rel_std = std_df / prop_df.replace(0, np.nan)
        rel_std_runs.append(rel_std)

    # --- Average RSD across runs ---
    avg_rel_std = pd.concat(rel_std_runs, keys=range(len(rel_std_runs))).groupby(level=1).mean()

    # --- Identify NaN RSD (division by zero) ---
    rsd_nan_mask = avg_rel_std.isna()

    # --- Masking rules ---
    mask_flags_raw = (avg_rel_std >= 1)
    mask_flags_rel = avg_rel_std.drop(columns=[source_sample_id], errors="ignore") \
                                .reindex_like(median_rel_contrib) >= 1

    # --- Apply masks to medians ---
    median_props_masked = median_props.mask(mask_flags_raw)
    median_rel_contrib_masked = median_rel_contrib.mask(mask_flags_rel)

    # --- Build mask log sheet ---
    mask_log_raw = pd.DataFrame("", index=avg_rel_std.index, columns=avg_rel_std.columns)

    # Flag RSD ≥ 1
    mask_log_raw[mask_flags_raw] = "⚠️ RSD ≥ 1"

    # Mark NaN RSD as "NA"
    mask_log_raw[rsd_nan_mask] = "NA"

    # --- Convert NaN RSD to "NA" in the RSD sheet ---
    avg_rel_std_display = avg_rel_std.copy()
    avg_rel_std_display = avg_rel_std_display.where(~rsd_nan_mask, other="NA")

    return {
        "Median Contributions": median_props_masked,
        "Median Relative Contributions": median_rel_contrib_masked,
        "Average Relative StdDev": avg_rel_std_display,
        "Masked Entries (RSD ≥ 1 & NA)": mask_log_raw
    }

# --- Run and export ---
results = process_stout_data(input_base_dir)
os.makedirs(output_dir, exist_ok=True)

with pd.ExcelWriter(output_path) as writer:
    for sheet_name, df in results.items():
        df.to_excel(writer, sheet_name=sheet_name)

print(f"✅ Results saved to: {output_path}")