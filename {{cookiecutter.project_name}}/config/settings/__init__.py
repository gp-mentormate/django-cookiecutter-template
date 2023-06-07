import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

if env("ENV") == 'production':
    from config.settings.production import * # noqa
else:
    from config.settings.local import * # noqa
