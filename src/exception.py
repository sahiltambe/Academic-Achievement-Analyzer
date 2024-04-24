import sys
import logging

def error_message_detail(error,error_detail:sys):
    # exc_tb we will get which file and which line the exception has occure
    # exc_tb.tb_frame.f_code.co_filename we will get the file name
    # exc_tb.tb_lineno we will get the line number
    # str(error) we will get the error message
    # we will get the file name, line number and error message
    # we will return the error message
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
# Testing Exception handling working
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)