#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import json
import pathlib
import logging
import logging.config

"""
Выполнить индивидуальное задание 1 лабораторной работы 2.19,
добавив возможность работы с исключениями и логгирование.
"""


class MyStudents:
    def __init__(self, line):
        self.line = line

    def select_student(self, undergraduates):
        """
        Выбрать cтудентов с заданной оценкой.
        """
        print(self.line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "No",
                "Ф.И.О.",
                "Группа",
                "Успеваемость"))
        print(self.line)
        for pupil in undergraduates:
            evaluations = pupil.get('progress')
            list_of_rating = list(evaluations)
            for i in list_of_rating:
                if i == '2':
                    print(
                        '| {:<4} | {:<30} | {:<20} | {:<15} |'.format(
                            i,
                            pupil.get('name', ''),
                            pupil.get('group', ''),
                            pupil.get('progress', 0)))
        print(self.line)

    def display(self, students):
        """
        Отобразить список студентов.
        """
        print(self.line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                "No",
                "Ф.И.О.",
                "Группа",
                "Успеваемость"))
        print(self.line)
        for idx, student in enumerate(students, 1):
            print(
                '| {:<4} | {:<30} | {:<20} | {:<15} |'.format(
                    idx,
                    student.get('name', ''),
                    student.get('group', ''),
                    student.get('progress', 0)
                )
            )
        print(self.line)

    def add_student(self, students, name, group, progress):
        students.append(
            {
                'name': name,
                'group': group,
                'progress': progress,
            }
        )
        return students

    def save_student(self, file_name, undergraduates):
        with open(file_name, "w", encoding="utf-8") as file_out:
            json.dump(undergraduates, file_out, ensure_ascii=False, indent=4)
        logging.info(f"Данные сохранены в файл: {file_name}")

    def load_student(self, file_name):
        with open(file_name, "r", encoding="utf-8") as f_in:
            return json.load(f_in)


def main(command_line=None):
    logging.basicConfig(
        filename='students.log',
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s"
    )

    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    st = MyStudents(line)

    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "filename",
        action="store",
    )
    parser = argparse.ArgumentParser("students")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )
    subparsers = parser.add_subparsers(dest="command")
    add = subparsers.add_parser(
        "add",
        parents=[file_parser]
    )
    add.add_argument(
        "-n",
        "--name",
        action="store",
        required=True,
    )
    add.add_argument(
        "-g",
        "--group",
        action="store",
        required=True,
    )
    add.add_argument(
        "-p",
        "--progress",
        action="store",
        required=True,
    )
    _ = subparsers.add_parser(
        "display",
        parents=[file_parser],
    )
    select = subparsers.add_parser(
        "select",
        parents=[file_parser],
    )
    select.add_argument(
        "-e",
        "--estimation",
        action="store",
        required=False,
    )
    args = parser.parse_args(command_line)
    is_dirty = False
    name = args.filename
    home = pathlib.Path.cwd() / name

    try:
        students = st.load_student(home)
        logging.info("Файл найден")
    except FileNotFoundError:
        students = []
        logging.warning("Файл не найден, создается новый")

    if args.command == "add":
        students = st.add_student(students, args.name, args.group, args.progress)
        is_dirty = True
        logging.info("Добавлен студент")
    elif args.command == 'display':
        st.display(students)
        logging.info("Отображён список студентов")
    elif args.command == "select":
        st.select_student(students)
        logging.info("Выбраны студенты с нужными оценками")

    if is_dirty:
        st.save_student(args.filename, students)


if __name__ == '__main__':
    main()
