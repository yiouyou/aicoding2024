from pathlib import Path


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
LOG_ROOT = PROJECT_ROOT / '_log'


##### api
WORKSPACE_MODULE = PROJECT_ROOT / '_workspace' / 'module'
LOG_MODULE = LOG_ROOT / 'module.log'
###


WORKSPACE_RAG = WORKSPACE_MODULE
