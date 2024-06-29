import sys
from logger import logging

def ex_msg_detailed(ex_msg, ex_detail : sys):
    _, _, exc_tb = ex_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno
    ex_msg_detail = f'Exception occured in: \n\
        python script name: [{file_name}], \n\
        line number: [{lineno}], \n\
        error message: [{ex_msg}]'
    return ex_msg_detail
    
class CustomException(Exception):
    def __init__(self, ex_msg, ex_detail : sys):
        super().__init__(ex_msg)
        self.ex_msg = ex_msg_detailed(ex_msg, ex_detail)

    def __str__(self):
        return self.ex_msg
    
if __name__ == '__main__':
    try:
        logging.info('trying risky move')
        a = 1/0
    except Exception as e:
        logging.exception(e)
        raise CustomException(e, sys)