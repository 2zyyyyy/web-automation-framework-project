import os
import sys
import pytest
from src.common.config import Config
from src.common.logger import logger

def main():
    """测试执行入口函数"""
    # 读取配置
    config = Config()
    
    # 构建pytest命令行参数
    pytest_args = [
        "src/tests",  # 默认测试目录
        "--alluredir", config.get_allure_report_dir(),  # allure报告数据目录
        "-v"  # 详细输出
    ]
    
    # 如果有命令行参数，使用用户指定的参数
    if len(sys.argv) > 1:
        pytest_args = sys.argv[1:] + ["--alluredir", config.get_allure_report_dir()]
    
    logger.info(f"开始执行测试，参数: {pytest_args}")
    
    # 执行测试
    exit_code = pytest.main(pytest_args)
    
    # 生成并打开allure报告（如果配置了）
    if config.generate_allure():
        logger.info("测试执行完成，开始生成allure报告")
        report_dir = config.get_allure_report_dir()
        html_report_dir = os.path.join(report_dir, "html")
        
        # 生成HTML报告
        os.system(f"allure generate {report_dir} -o {html_report_dir} --clean")
        
        # 打开报告
        os.system(f"allure open {html_report_dir}")
    
    logger.info(f"测试执行结束，退出码: {exit_code}")
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
    