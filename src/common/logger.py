import logging
import os
from datetime import datetime
from src.common.config import Config

class Logger:
    """日志管理类，支持控制台和文件输出，按日期分割日志文件"""
    
    def __init__(self):
        # 读取配置
        self.config = Config()
        self.log_level = self._get_log_level()
        self.log_format = self.config.get_log_format()
        
        # 创建日志目录
        self.log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'logs')
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
            
        # 日志文件名按日期生成
        self.log_file = os.path.join(self.log_dir, f"test_{datetime.now().strftime('%Y-%m-%d')}.log")
        
        # 初始化logger
        self.logger = logging.getLogger('web_automation')
        self.logger.setLevel(self.log_level)
        
        # 避免重复添加handler
        if not self.logger.handlers:
            self._set_handlers()
    
    def _get_log_level(self):
        """将配置的日志级别字符串转换为logging模块对应的级别"""
        level_str = self.config.get_log_level().upper()
        level_mapping = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        return level_mapping.get(level_str, logging.INFO)
    
    def _set_handlers(self):
        """设置日志处理器，包括文件和控制台输出"""
        # 格式化器
        formatter = logging.Formatter(self.log_format)
        
        # 文件handler
        file_handler = logging.FileHandler(self.log_file, encoding='utf-8')
        file_handler.setLevel(self.log_level)
        file_handler.setFormatter(formatter)
        
        # 控制台handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.log_level)
        console_handler.setFormatter(formatter)
        
        # 添加handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def get_logger(self):
        """获取logger实例"""
        return self.logger

# 单例模式，全局使用同一个logger实例
logger = Logger().get_logger()
    