
import pyautogui
from logger import logger
from aip import AipOcr

APP_ID = '19967553'
API_KEY = 'SRUGlg4OCzCfqQ27uHCw6Qv9'
SECRET_KEY = 'NNp5CuV3FPnawyAv5qbF8yXGTiPQyBSl'
ocr_client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


class BApi:
    @staticmethod
    def find_text(path):
        image = get_file_content(path)
        res = ocr_client.basicGeneral(image)
        print(res)
        if len(res['words_result']) == 0:
            logger.launch_logger('baidu ocr 未识别到文字')
            return None
        else:
            logger.launch_logger('识别文字成功:' + str(res))
        return res




