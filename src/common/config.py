import configparser
import os
from src.common.logger import logger

class Config:
    """配置管理类，负责解析和提供配置文件中的各项配置"""
    
    def __init__(self):
        # 配置文件路径
        self.config_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
            'configs', 'config.ini'
        )
        
        # 初始化配置解析器
        self.config = configparser.ConfigParser()
        self._load_config()
        
        # 确保所有必要的配置项存在
        self._check_configs()
    
    def _load_config(self):
        """加载配置文件"""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"配置文件不存在: {self.config_path}")
        
        try:
            self.config.read(self.config_path, encoding='utf-8')
            logger.info(f"成功加载配置文件: {self.config_path}")
        except Exception as e:
            logger.error(f"加载配置文件失败: {str(e)}")
            raise
    
    def _check_configs(self):
        """检查必要的配置项是否存在"""
        required_sections = ['browser', 'test', 'log', 'report']
        for section in required_sections:
            if not self.config.has_section(section):
                raise ValueError(f"配置文件缺少必要的部分: {section}")
    
    # 浏览器相关配置
    def get_browser_type(self):
        """获取浏览器类型"""
        return self.config.get('browser', 'type', fallback='chrome').lower()
    
    def is_headless(self):
        """是否启用无头模式"""
        return self.config.getboolean('browser', 'headless', fallback=False)
    
    def get_window_size(self):
        """获取浏览器窗口大小"""
        return self.config.get('browser', 'window_size', fallback='1920,1080')
    
    # 测试相关配置
    def get_base_url(self):
        """获取测试基础URL"""
        return self.config.get('test', 'base_url', fallback='')
    
    def get_timeout(self):
        """获取超时时间(秒)"""
        return self.config.getint('test', 'timeout', fallback=10)
    
    # 日志相关配置
    def get_log_level(self):
        """获取日志级别"""
        return self.config.get('log', 'level', fallback='INFO')
    
    def get_log_format(self):
        """获取日志格式"""
        return self.config.get(
            'log', 'format', 
            fallback='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    # 报告相关配置
    def generate_allure(self):
        """是否生成allure报告"""
        return self.config.getboolean('report', 'generate_allure', fallback=True)
    
    def get_allure_report_dir(self):
        """获取allure报告目录"""
        return self.config.get('report', 'allure_report_dir', fallback='reports/allure')
    