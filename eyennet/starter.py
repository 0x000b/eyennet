# MIT License

# Copyright (c) 2023 Henrique Cavalcante

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# Python Imports
from termcolor import colored
import socket
import platform

def logo():
    print(' ______     __  __     ______     __   __     __   __     ______     ______ ')
    print(f'/\  ___\   /\ \_\ \   /\  ___\   /\ "-.\ \   /\ "-.\ \   /\  ___\   /\__  _\ ')
    print(f'\ \  __\   \ \____ \  \ \  __\   \ \ \-.  \  \ \ \-.  \  \ \  __\   \/_/\ \/')
    print(f' \ \_____\  \/\_____\  \ \_____\  \ \_\\\ \_\  \ \_\\\ \_\  \ \_____\    \ \_\ ')
    print(f'  \/_____/   \/_____/   \/_____/   \/_/ \/_/   \/_/ \/_/   \/_____/     \/_/')
    print(f'\n@Github' + colored(' 0x000b \n', "green"))

def userInfo():
    print(colored("[Local IP Address] ","blue")+ socket.gethostbyname(socket.gethostname))
    print(colored("[FQDN] ", "blue")+ socket.getfqdn())
    print(colored("[Platform] ","blue")+ platform.system())
    