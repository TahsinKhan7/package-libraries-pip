import os

working_dir = os.getcwd()


# def return_user_id():
#     return os.getuid()
#
# print(working_dir)
# print(return_user_id())

def encode_py(file):
    return os.fsencode(file)
def decode_py(file):
    return os.fsencode(file)


encode_name = encode_py('py_lib.py')
print(encode_name)

decode_name = decode_py(encode_name)
print(decode_name)
