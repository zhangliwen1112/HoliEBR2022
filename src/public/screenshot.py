import time
import os
from functools import wraps
import logging


def get_image(function):
    """
    用例执行出错时进行截图，此为python装饰器，需要在每条用例前添加 @get_image
    """
    @wraps(function)
    def get_error_image(self, *args, **kwargs):
        try:
            function(self, *args, **kwargs)
        except Exception:
            base_dir = os.getcwd()
            base = base_dir.split(r"\HoliEBR")[0]
            file_path = base + "\\HoliEBR\\report\\image\\" + function.__name__ + '_' + time.strftime("%Y%m%d%H%M%S") + '.png'
            self.driver.get_screenshot_as_file(file_path)
            raise
        else:
            logging.info(u'%s pass' % function.__name__)
    return get_error_image
