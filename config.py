# -*- coding:utf-8 -*-

import settings
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
token = settings.TOKEN_TG  # token = 'your token'
