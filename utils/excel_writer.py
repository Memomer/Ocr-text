import pandas as pd
import os

def write_lines_to_excel(line_data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.DataFrame(line_data)
    df.to_excel(output_path, index=False)
