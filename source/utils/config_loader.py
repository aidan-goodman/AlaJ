import os
import json


class ConfigLoader:
    def __init__(self, config_path: str = ""):
        """
        初始化配置加载器。

        :param config_path: JSON 配置文件路径，默认为 '/config/config.json'
        """
        if not config_path:
            config_path = os.getcwd() + "/config/config.json"
        self.config_path = config_path
        self.config = {}
        self.load_config()

    def load_config(self):
        """
        加载 JSON 配置文件
        """
        try:
            with open(self.config_path, "r") as file:
                self.config = json.load(file)
        except FileNotFoundError:
            print(f"Warning: Config file {self.config_path} not found.")
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse config file {self.config_path}: {e}")

        self.config = self._flatten_dict(self.config)

    def _flatten_dict(self, d: dict, parent_key: str = "", sep: str = ".") -> dict:
        """
        将嵌套字典转换为扁平化字典，键使用分隔符连接。

        :param d: 需要扁平化的字典
        :param parent_key: 父键前缀
        :param sep: 分隔符，默认为 '.'
        :return: 扁平化后的字典
        """
        items = {}
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.update(self._flatten_dict(v, new_key, sep=sep))
            else:
                items[new_key] = v
        return items

    def get(self, key: str, default=None):
        """
        获取配置项的值，支持嵌套键访问（点号分隔）。

        :param key: 配置项的键（支持嵌套键，如 'database.host'）
        :param default: 如果配置项不存在，则返回的默认值
        :return: 配置项的值或默认值
        """
        if isinstance(self.config, dict) and key in self.config:
            return self.config[key]
        else:
            return default
