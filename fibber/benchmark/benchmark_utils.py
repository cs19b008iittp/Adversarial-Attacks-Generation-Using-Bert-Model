import os
import pandas as pd

from fibber import get_root_dir


def update_detailed_result(aggregated_result):
    """Read dataset detailed results and add a row to the file. Create a new file if the table
    does not exist.

    Args:
        aggregated_result (dict): the aggregated result as a dictionary.
    """
    result_dir = os.path.join(get_root_dir(), "results")
    os.makedirs(result_dir, exist_ok=True)
    result_filename = os.path.join(result_dir, "detail.csv")
    if os.path.exists(result_filename):
        results = pd.read_csv(result_filename)
    else:
        results = pd.DataFrame()

    results = results.append(aggregated_result, ignore_index=True)
    results.to_csv(result_filename, index=None)


def load_detailed_result():
    """Read detailed results from file.

    Returns:
        (DataFrame): Return an empty DataFrame if file does not exist.
    """
    result_dir = os.path.join(get_root_dir(), "results")
    result_filename = os.path.join(result_dir, "detail.csv")
    if os.path.exists(result_filename):
        return pd.read_csv(result_filename)
    else:
        return pd.DataFrame()


def update_overview_result(overview_result):
    """write overview result to file.

    Args:
        overview_result (DataFrame): the overview result.
    """
    result_dir = os.path.join(get_root_dir(), "results")
    os.makedirs(result_dir, exist_ok=True)
    result_filename = os.path.join(result_dir, "overview.csv")
    overview_result.to_csv(result_filename, index=None)