class Solution(object):
    def calculate(self, s: str):
        """
        :type operation["string"]: str
        :rtype: int
        """
        s = s.replace(" ", "")

        result = number = 0
        sign = 1
        op_stack = []

        # Convertion of the input s for cases of
        # consecutive operators '+-' and '--'
        # '+-n'     =>  '+(-n)'
        # '+-(...)' =>  '+(-(...))'
        # '--n'     =>  '-(-n)'
        # '--(...)' =>  '-(-(...))'
        s = self.process_consecutive_operators(s, "+-")
        s = self.process_consecutive_operators(s, "--")

        for char in s:
            if char.isdigit():
                number = 10 * number + int(char)

            elif char in "+-":
                result += sign * number

                sign = 1 if char == "+" else -1
                number = 0

            elif char == "(":
                op_stack.append(result)
                op_stack.append(sign)

                # No need to initialize number because "(" will not next to number
                result = 0
                sign = 1

            elif char == ")":
                result += sign * number

                sign = op_stack.pop()  # pop the recorded sign
                number = op_stack.pop()  # pop the recorded result

                result *= sign
                result += number

                # No need to initialize the sign because sign*0 is zero
                number = 0

        result += sign * number
        return result

    def process_consecutive_operators(self, s, operators_pattern):
        while s.find(operators_pattern) != -1:
            idx_ops = s.find(operators_pattern) + 2
            if s[idx_ops] == "(":
                tmp_s = s[idx_ops + 1 :]
                idx_right_paren = idx_ops + 1 + self.find_right_paren(tmp_s)

                # '...+'/'...-' + '(' + '-(...)' + ')' + '...'
                s = s[: idx_ops - 1] + "(" + s[idx_ops - 1 : idx_right_paren + 1] + ")" + s[idx_right_paren + 1 :]
            else:
                idx_digit = idx_ops
                while idx_digit < len(s) and s[idx_digit].isdigit():
                    idx_digit += 1

                # '...+'/'...-' + '(' + '-n' + ')' + '...'
                s = s[: idx_ops - 1] + "(" + s[idx_ops - 1 : idx_digit] + ")" + s[idx_digit:]

        return s

    def find_right_paren(self, s):
        parens_stack = []
        for idx_paraen_r, char in enumerate(s):
            if char == "(":
                parens_stack.append("(")
            elif char == ")":
                if len(parens_stack):
                    parens_stack.pop()
                else:
                    break
        return idx_paraen_r


if __name__ == "__main__":
    obj = Solution()

    s = "1-(-2)"  # 3
    print(obj.calculate(s))

    s = "-2 + 1"  # -1
    print(obj.calculate(s))

    s = "-(2-1) + 1"  # 0
    print(obj.calculate(s))

    s = "-(1+(4+5+2)-3)+(6+8)"  # 5
    print(obj.calculate(s))

    s = "-(1+(4+(5+2)-5+2)-3)+(6+8)"  # 8
    print(obj.calculate(s))

    s = "-(1+(4+5+-1)--3)+(6+8)"  # 2
    print(obj.calculate(s))

    s = "-(1+(4+-(5+-2)--5+2)-3)+(6+8)"  # 8
    print(obj.calculate(s))

    s = "1 + 1"  # 2
    print(obj.calculate(s))

    s = " 2-1 + 2 "  # 3
    print(obj.calculate(s))

    s = "(1+(4+5+2)-3)+(6+8)"  # 23
    print(obj.calculate(s))

    s = "(1+(4+(5+2)-5+2)-3)+(6+8)"  # 20
    print(obj.calculate(s))

    s = "(1+(4+5+-1)--3)+(6+8)"  # 26
    print(obj.calculate(s))

    s = "(1+(4+-(5+-2)--5+2)-3)+(6+8)"  # 20
    print(obj.calculate(s))

    s = "(1)"  # 1
    print(obj.calculate(s))
