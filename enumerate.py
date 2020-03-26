#! /usr/bin/python3

import argparse
import os


class Main:
    def __init__(self):
        self.text_content = ''
        self.out = None

    def file_enum(self, args):
        folder = args.folder
        recursive = args.recursive
        output = args.output

        if not os.path.exists(folder):
            raise Exception(f'Folder {folder} does not exists!')

        self.create_result_file(folder, output)
        self.print_folder_content(folder, recursive)
        self.close_output_file()

    def print_folder_content(self, path, recursive):
        if os.path.exists(path):
            for root, dir, files in os.walk(path):
                self.print_root_name(root)
                for file in files:
                    self.print_file_name(file)

    def print_root_name(self, root):
        try:
            self.out.write(f'- {root}\n')
            self.out.flush()
        except Exception as ex:
            print(ex)

    def print_file_name(self, file):
        try:
            self.out.write(f'\t-\t{file}\n')
            self.out.flush()
        except Exception as ex:
            print(ex)

    def close_output_file(self):
        self.out.close()

    def create_result_file(self, root_dir, output):
        output_path = os.path.join(root_dir, output)
        if os.path.exists(output_path):
            os.remove(output_path)
        self.out = open(output_path, 'w+', encoding='utf-8')


parser = argparse.ArgumentParser(description='Extract file names recursively (-r) starting from specified folder.',
                                 prog='enumerate.py', usage='%(prog)s [options] folder output_txt', add_help=True)
parser.add_argument('folder', help='starting folder')
parser.add_argument('-r', '--recursive', action='store_true', help='recursively list top-down folders', default=False)
parser.add_argument('-o', '--output', help='output file', default='enumerator_results.txt')
args = parser.parse_args()

main = Main()
main.file_enum(args)
