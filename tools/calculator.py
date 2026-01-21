from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    
    """
    This function evaluates a mathematical expression and return the result as a string.
    
    Args:
        expression (str): A string containing a mathematical expression to be evaluated.
        
    Returns:
        str: The result of the evaluated expression as a string.
    """
    
    try:
        result  = eval(expression)
        return str(result)
    except ZeroDivisionError:
        return "Error evaluating expression: division by zero"
    except SyntaxError:
        return "Error evaluating expression: invalid syntax"
    except Exception as e:
        return f"Error evaluating expression: {e}"
    