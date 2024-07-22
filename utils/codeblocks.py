import re

def extract_code_blocks(response_content):
    pattern = re.compile(r'```(.*?)```', re.DOTALL)
    code_blocks = pattern.findall(response_content)
    return code_blocks

def detect_language(code_block):
    if 'def ' in code_block or 'import ' in code_block:
        return 'Python'
    elif '#include' in code_block or 'int main' in code_block:
        return 'C'
    elif 'public class' in code_block or 'System.out.println' in code_block:
        return 'Java'
    elif 'using System;' in code_block or 'Console.WriteLine' in code_block:
        return 'CSharp'
    elif 'function ' in code_block or 'const ' in code_block:
        return 'JavaScript'
    else:
        return 'bash'