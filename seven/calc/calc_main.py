import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)

        self.text = str()
        self.was_op_pushed = True
        self.can_push_digit = True
        self.dot_pushed = []  # для каждого числа должно проверяться есть ли у него уже точка или нет
        self.pushed_brackets = []  # для каждой скобки, чтобы закрыть ее должно выполниться действие:
        # должно быть введено минимум два числа и знак операции м/у ними
        self.ops = '+-*/'

        self.pushButton_0.clicked.connect(lambda: self.push_dig(0))
        self.pushButton_1.clicked.connect(lambda: self.push_dig(1))
        self.pushButton_2.clicked.connect(lambda: self.push_dig(2))
        self.pushButton_3.clicked.connect(lambda: self.push_dig(3))
        self.pushButton_4.clicked.connect(lambda: self.push_dig(4))
        self.pushButton_5.clicked.connect(lambda: self.push_dig(5))
        self.pushButton_6.clicked.connect(lambda: self.push_dig(6))
        self.pushButton_7.clicked.connect(lambda: self.push_dig(7))
        self.pushButton_8.clicked.connect(lambda: self.push_dig(8))
        self.pushButton_9.clicked.connect(lambda: self.push_dig(9))

        self.pushButton_Lbracket.clicked.connect(lambda: self.push_bracket('('))
        self.pushButton_Rbracket.clicked.connect(lambda: self.push_bracket(')'))

        self.pushButton_plus.clicked.connect(lambda: self.push_op('+'))
        self.pushButton_minus.clicked.connect(lambda: self.push_op('-'))
        self.pushButton_mult.clicked.connect(lambda: self.push_op('*'))
        self.pushButton_div.clicked.connect(lambda: self.push_op('/'))

        self.pushButton_dot.clicked.connect(self.push_dot)

        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_del.clicked.connect(self.delete)

        self.pushButton_eq.clicked.connect(self.equal)

    def push_dig(self, num):
        if self.can_push_digit:
            if self.was_op_pushed and len(self.text) > 0 and self.text[len(self.text) - 1] != '(' and len(
                    self.pushed_brackets) > 0:
                self.pushed_brackets[len(self.pushed_brackets) - 1] = True

            if num == 0 and (len(self.text) == 0 or self.text[len(self.text) - 1] in self.ops):
                return
            self.text += str(num)

            if self.was_op_pushed:
                self.dot_pushed.append(False)

            self.was_op_pushed = False

            self.print_text()

    def push_bracket(self, bracket):
        if bracket == '(' and self.was_op_pushed:
            self.text += bracket
            self.was_op_pushed = True
            self.pushed_brackets.append(False)
        elif bracket == ')' and len(self.pushed_brackets) > 0 and self.pushed_brackets[len(self.pushed_brackets) - 1]:
            self.text += bracket
            self.pushed_brackets.pop()
            self.was_op_pushed = False
            self.can_push_digit = False
        self.print_text()

    def push_op(self, op_symbol):
        if not self.was_op_pushed:
            self.text += op_symbol
        self.was_op_pushed = True
        self.can_push_digit = True
        self.print_text()

    def push_dot(self):
        if len(self.text) == 0 or self.text[len(self.text) - 1] in self.ops:
            self.text += '0.'
            self.dot_pushed.append(True)
        elif not self.dot_pushed[len(self.dot_pushed) - 1]:
            self.text += '.'
        else:
            self.print_text()
            return
        self.dot_pushed[len(self.dot_pushed) - 1] = True
        self.print_text()

    def clear(self):
        self.text = ''
        self.was_op_pushed = True
        self.can_push_digit = True
        self.dot_pushed = []
        self.pushed_brackets = []
        self.print_text()

    def delete(self):
        if len(self.text) > 0:
            if self.text[len(self.text) - 1] == ')':
                self.pushed_brackets.append(True)
                self.can_push_digit = True
            elif self.text[len(self.text) - 1] == '(':
                self.can_push_digit = True
                self.pushed_brackets.pop()
            elif self.text[len(self.text) - 1] in self.ops:
                self.was_op_pushed = False
                self.can_push_digit = True
            elif self.text[len(self.text) - 1] == '.':
                self.dot_pushed[len(self.dot_pushed) - 1] = False

        self.text = self.text[:len(self.text) - 1]

        if self.text[len(self.text) - 1] == '0' and (len(self.text) == 1 or self.text[len(self.text) - 2] in self.ops):
            self.text = self.text[:len(self.text) - 1]

        if len(self.text) > 0 and self.text[len(self.text) - 1] in self.ops:
            self.was_op_pushed = True
            self.dot_pushed.pop()


        self.print_text()

    def equal(self):
        try:
            self.text = str(eval(self.text))
            self.print_text()
        except ZeroDivisionError:
            self.Tab.setText('Нельзя делить на ноль')
        except:
            self.Tab.setText('Ошибка')

        self.dot_pushed = []
        if '.' in self.text:
            self.dot_pushed.append(True)

    def print_text(self):
        self.Tab.setText(self.text)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
