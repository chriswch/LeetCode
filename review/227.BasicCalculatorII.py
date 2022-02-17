class Solution(object):
    def calculate(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")

        stack_operands = []
        operator = "+"
        number = ""
        for char in s + " ":
            if char.isdigit():
                number += char
            else:
                number = int(number)
                if operator in "+-":
                    stack_operands.append(number if operator == "+" else -number)

                elif operator in "*/":
                    stack_operands[-1] = (
                        stack_operands[-1] * number if operator == "*" else int(float(stack_operands[-1]) / number)
                    )
                operator = char
                number = ""

        return sum(stack_operands)

    def calculate_myself(self, s: str):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")

        number = 0
        stack_operands = []
        stack_operators = []

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            else:
                stack_operands.append(number)
                number = 0

                # Check whether to do multiplication or division first
                if len(stack_operators) and stack_operators[-1] in "*/":
                    opr = stack_operators.pop()
                    rvalue = stack_operands.pop()
                    lvalue = stack_operands.pop()

                    result = lvalue * rvalue if opr == "*" else lvalue // rvalue
                    stack_operands.append(result)

                # Addition and Substraction
                if char in "+-":
                    if len(stack_operators) and stack_operators[-1] in "+-":
                        opr = stack_operators.pop()
                        rvalue = stack_operands.pop()
                        lvalue = stack_operands.pop()

                        result = lvalue + rvalue if opr == "+" else lvalue - rvalue
                        stack_operands.append(result)

                    stack_operators.append(char)

                # Multiplication and Division
                else:
                    stack_operators.append(char)

        # The last operand
        stack_operands.append(number)

        if len(stack_operators):
            opr = stack_operators.pop()
            rvalue = stack_operands.pop()
            lvalue = stack_operands.pop()
            if opr == "*":
                result = lvalue * rvalue
            elif opr == "/":
                result = lvalue // rvalue
            elif opr == "+":
                result = lvalue + rvalue
            else:
                result = lvalue - rvalue
            stack_operands.append(result)

        # Must be addition or substraction
        if len(stack_operators):
            opr = stack_operators.pop()
            rvalue = stack_operands.pop()
            lvalue = stack_operands.pop()

            result = lvalue + rvalue if opr == "+" else lvalue - rvalue
            stack_operands.append(result)

        return stack_operands[-1]


if __name__ == "__main__":
    obj = Solution()

    # s = "3+2*2"  # 7
    # print(obj.calculate(s))

    # s = " 3/2 "  # 1
    # print(obj.calculate(s))

    # s = " 3+5 / 2 "  # 5
    # print(obj.calculate(s))

    # s = "0"  # 0
    # print(obj.calculate(s))

    # s = "1+1+1"  # 3
    # print(obj.calculate(s))

    s = "14-3/2"
    print(obj.calculate(s))

    s = "1*2-3/4+5*6-7*8+9/10"
    print(obj.calculate(s))
