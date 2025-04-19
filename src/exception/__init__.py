import sys
import logging

def error_message_detail(error:Exception, error_detail: sys)-> str:
    """
    Exctracts detailed information including file name,line number, and the error message.
    
    :param error: The Exception that occured.
    :param error_details: The sys module to access traceback calls.
    :return: A formatted error message string.
    """
    
    _, _, exc_tb = error_detail.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]: {str(error)}"
    logging.error_message
    
    return error_message

class MyException(Exception):
    """Custom exception class for handling errors"""
    
    def __init__(self, error_message: str, error_detail: sys):
        """Initializes the Exception with error message
        
        :param error_message: A string describing the error.
        :param error_detail: The sys module to access traceback details.
        """
        
        super().__init__(error_message)
        
        self.error_message = error_message_detail(error_message, error_detail)
    
    def __str__(self) -> str:
        """Returns the string representation of the error message."""
        
        return self.error_message