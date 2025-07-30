# web-automation-framework-project

# Web 自动化测试框架

一个基于 Python + Selenium + pytest + allure 的 Web 自动化测试框架，用于快速搭建和执行 Web 端自动化测试。

## 框架特点

- 采用 Page Object 设计模式，提高代码复用性和可维护性
- 集成 pytest 测试框架，支持丰富的测试用例组织方式
- 集成 allure 报告，生成美观详细的测试报告
- 完善的日志记录功能，便于问题定位
- 灵活的配置管理，支持不同环境和参数设置
- 自动截图功能，在测试失败时自动捕获屏幕截图

## 环境要求

- Python 3.7+
- 浏览器（Chrome 或 Firefox）
- 对应浏览器的 WebDriver（chromedriver 或 geckodriver）
- Allure 命令行工具（用于生成测试报告）

## 安装步骤

1. 克隆或下载本项目到本地

2. 安装依赖包
   ```
   pip install -r requirements.txt
   ```

3. 安装 allure 报告工具
   - 下载地址：https://github.com/allure-framework/allure2/releases
   - 解压后将 bin 目录添加到系统环境变量

4. 配置浏览器驱动
   - 将 chromedriver 或 geckodriver 放入 drivers 目录
   - 确保驱动版本与浏览器版本匹配
   - 将 drivers 目录添加到系统环境变量

## 框架结构
```
web-automation-framework-project/
├── src/                      # 源代码目录
│   ├── common/               # 公共工具类
│   │   ├── logger.py         # 日志配置
│   │   ├── config.py         # 配置文件处理
│   │   └── utils.py          # 通用工具函数
│   ├── page_objects/         # 页面对象模式
│   │   ├── base_page.py      # 基础页面类
│   │   └── ...               # 其他页面类
│   ├── test_data/            # 测试数据
│   │   └── ...
│   └── tests/                # 测试用例
│       ├── conftest.py       # pytest 配置
│       ├── test_example.py   # 示例测试用例
│       └── ...
├── reports/                  # 测试报告目录
│   └── allure/               # allure 报告
├── logs/                     # 日志文件目录
├── configs/                  # 配置文件
│   ├── config.ini            # 主要配置
│   └── ...
├── drivers/                  # 浏览器驱动
│   └── ...
├── screenshots/              # 截图目录
├── requirements.txt          # 项目依赖
├── run_tests.py              # 测试运行入口
└── README.md                 # 项目说明文档
```

## 配置说明

配置文件位于 `configs/config.ini`，可根据需要修改以下配置：

- `[browser]`: 浏览器相关配置
  - `type`: 浏览器类型，支持 chrome 和 firefox
  - `headless`: 是否启用无头模式，true 或 false
  - `window_size`: 浏览器窗口大小，如 1920,1080

- `[test]`: 测试相关配置
  - `base_url`: 测试的基础 URL
  - `timeout`: 超时时间（秒）

- `[log]`: 日志相关配置
  - `level`: 日志级别，如 INFO, DEBUG
  - `format`: 日志格式

- `[report]`: 报告相关配置
  - `generate_allure`: 是否生成 allure 报告，true 或 false
  - `allure_report_dir`: allure 报告目录

## 运行测试

执行以下命令运行测试：
python run_tests.py
测试完成后，会自动生成并打开 allure 测试报告。

## 编写测试用例

1. 在 `src/page_objects` 目录下创建页面对象类，继承 BasePage
2. 在 `src/tests` 目录下创建测试文件，命名以 `test_` 开头
3. 使用 pytest 装饰器组织测试用例，如 `@allure.feature`, `@allure.story`
4. 使用 `src/tests/conftest.py` 中定义的 fixture，如 `driver`, `base_url`

示例测试用例可参考 `src/tests/test_example.py`

## 查看报告

测试报告位于 `reports/allure/html` 目录下，可通过以下命令手动打开：
allure open reports/allure/html
## 查看日志

日志文件位于 `logs` 目录下，按日期命名，如 `test_2023-06-01.log`

## 截图

测试过程中产生的截图位于 `screenshots` 目录下，主要在测试失败时自动生成
