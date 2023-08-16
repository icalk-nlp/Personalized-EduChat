
import sys
from pathlib import Path

from loguru import logger as _logger

def get_project_root():
    """逐级向上寻找项目根目录"""
    current_path = Path.cwd()
    while True:
        if (current_path / '.git').exists() or \
           (current_path / '.project_root').exists() or \
           (current_path / '.gitignore').exists():
            return current_path
        parent_path = current_path.parent
        if parent_path == current_path:
            raise Exception("Project root not found.")
        current_path = parent_path

PROJECT_ROOT = get_project_root()



def define_log_level(print_level="INFO", logfile_level="DEBUG"):
    """调整日志级别到level之上
       Adjust the log level to above level
    """
    _logger.remove()
    _logger.add(sys.stderr, level=print_level)
    _logger.add(PROJECT_ROOT / 'logs/log.txt', level=logfile_level)
    return _logger


logger = define_log_level()
