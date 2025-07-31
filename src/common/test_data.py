import os
import json
import yaml
import pandas as pd
from src.common.logger import logger

class TestData:
    """测试数据管理类，支持JSON、YAML和Excel格式的数据读取"""
    
    def __init__(self):
        # 测试数据目录路径
        self.data_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            'test_data'
        )
        
        # 确保测试数据目录存在
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            logger.warning(f"测试数据目录不存在，已自动创建: {self.data_dir}")
    
    def _get_data_path(self, filename):
        """获取数据文件的完整路径"""
        return os.path.join(self.data_dir, filename)
    
    def load_json(self, filename):
        """加载JSON格式的测试数据"""
        try:
            file_path = self._get_data_path(filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logger.info(f"成功加载JSON测试数据: {filename}")
            return data
        except FileNotFoundError:
            logger.error(f"JSON测试数据文件不存在: {filename}")
            raise
        except json.JSONDecodeError:
            logger.error(f"JSON测试数据格式错误: {filename}")
            raise
    
    def load_yaml(self, filename):
        """加载YAML格式的测试数据"""
        try:
            file_path = self._get_data_path(filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            logger.info(f"成功加载YAML测试数据: {filename}")
            return data
        except FileNotFoundError:
            logger.error(f"YAML测试数据文件不存在: {filename}")
            raise
        except yaml.YAMLError:
            logger.error(f"YAML测试数据格式错误: {filename}")
            raise
    
    def load_excel(self, filename, sheet_name=0):
        """加载Excel格式的测试数据"""
        try:
            file_path = self._get_data_path(filename)
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            # 转换为列表字典格式
            data = df.to_dict('records')
            logger.info(f"成功加载Excel测试数据: {filename}, 工作表: {sheet_name}")
            return data
        except FileNotFoundError:
            logger.error(f"Excel测试数据文件不存在: {filename}")
            raise
        except Exception as e:
            logger.error(f"加载Excel测试数据失败: {str(e)}")
            raise
    
    def get_test_case_data(self, data_file, case_id):
        """
        从测试数据中获取指定用例ID的数据
        适用于包含多个测试用例的数据集
        """
        # 根据文件扩展名判断数据格式
        if data_file.endswith('.json'):
            all_data = self.load_json(data_file)
        elif data_file.endswith('.yaml') or data_file.endswith('.yml'):
            all_data = self.load_yaml(data_file)
        elif data_file.endswith('.xlsx') or data_file.endswith('.xls'):
            all_data = self.load_excel(data_file)
        else:
            raise ValueError(f"不支持的数据文件格式: {data_file}")
        
        # 查找指定case_id的数据
        for item in all_data:
            if str(item.get('case_id')) == str(case_id):
                logger.info(f"找到测试用例数据: {data_file} -> {case_id}")
                return item
        
        logger.error(f"未找到测试用例数据: {data_file} -> {case_id}")
        raise ValueError(f"测试用例数据不存在: {case_id}")

# 单例实例
test_data = TestData()
    