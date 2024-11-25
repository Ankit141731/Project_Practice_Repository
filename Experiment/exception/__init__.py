import os , sys

def error_message_detail(error , error_detail:sys):

    _,_,exc_tb = error_detail.exc_info()

    TRY_BLOCK_LINE_NO = exc_tb.tb_frame.f_lineno 
    EXC_BLOCK_LINE_NO = exc_tb.tb_lineno 
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = f"""Error Occured in python script {file_name} Try block Line no {TRY_BLOCK_LINE_NO} and
                       exception block line no {EXC_BLOCK_LINE_NO}  error {error}"""
    
    return error_message

class CustomException(Exception):
    def __init__(self , error_message , error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(

            error_message , error_detail = error_detail
        )

    def __str__(self):
        return self.error_message