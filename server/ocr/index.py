
from aip import AipOcr

APP_ID = '19967553'
API_KEY = 'SRUGlg4OCzCfqQ27uHCw6Qv9'
SECRET_KEY = 'NNp5CuV3FPnawyAv5qbF8yXGTiPQyBSl'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


def get_text_from_image(path):
    try:
        image = get_file_content(path)
        res = client.basicGeneral(image)
        # print(res['words_result'])
        if len(res['words_result']) == 0:
            print('ocr 未识别到文字')
            return None
        return res
    except:
        print('ocr 图片识别异常')
        return None



