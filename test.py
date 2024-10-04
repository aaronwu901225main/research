import os
import yaml  # 確保已導入必要的庫

from parameters import parser, YML_PATH

# 確認使用的資料集
dataset_name = 'mit-states'  # 或從 argparse 獲取
config_path = YML_PATH[dataset_name]
print(f"Loading configuration from: {config_path}")

# 加載 YAML 文件
with open(config_path, 'r') as stream:
    config = yaml.safe_load(stream)
