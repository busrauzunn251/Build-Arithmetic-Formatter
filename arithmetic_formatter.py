def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    
    for problem in problems:
        split = problem.split()
        num1 = split[0]
        operator = split[1]
        num2 = split[2]
        
        # Error: Operator must be '+' or '-'
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."
        
        # Error: Numbers must only contain digits
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        # Error: Numbers cannot be more than four digits
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Determine the maximum length of the operands for formatting
        max_length = max(len(num1), len(num2))
        
        # Build each line of the arranged problem
        line1 += num1.rjust(max_length + 2) + '    '
        line2 += operator + num2.rjust(max_length + 1) + '    '
        line3 += '-' * (max_length + 2) + '    '
        
        # Calculate answers if show_answers is True
        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            elif operator == '-':
                answer = str(int(num1) - int(num2))
            line4 += answer.rjust(max_length + 2) + '    '
    
    # Remove trailing spaces from each line
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    line4 = line4.rstrip()
    
    # Combine all lines with four spaces between problems
    arranged_problems = '\n'.join([line1, line2, line3])
    if show_answers:
        arranged_problems += '\n' + line4
    
    return arranged_problems
