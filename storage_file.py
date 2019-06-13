import os

base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, 'data')


def storage_file(filename, data):
    abs_filename = os.path.join(data_dir, filename)

    with open(abs_filename, 'wb') as f:
        f.write(data)

    return abs_filename


if __file__ == '__main__':
    storage_file()
