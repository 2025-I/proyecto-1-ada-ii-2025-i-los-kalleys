from enum import Enum
import tkinter as tk
from tkinter import filedialog
from typing import Callable
from utils.normalize import normalizer
from palindrome.brute_force_solution import max_subsequence_palindrome
from palindrome.dinamic_solution import max_dynamic_palindrome
from palindrome.greedy_solution import greedy_palindromic_substring
from party.brute_force_solution import brute_force_party
from party.dinamic_solution import max_dinamic_invite_values


class AlgorithmOptions(str, Enum):
    BRUTE_FORCE = "Fuerza Bruta"
    DYNAMIC = "Dinámica"
    GREEDY = "Voraz"


class FileReaderApp:
    def __init__(self, root):
        self.__root = root
        self.__root.title("Lector de archivos .txt")

        self.__file1_path = ""
        self.__file2_path = ""

        self.__file1_type = tk.StringVar(value=AlgorithmOptions.BRUTE_FORCE.value)
        self.__file2_type = tk.StringVar(value=AlgorithmOptions.BRUTE_FORCE.value)

        self.__create_widgets()

    def __create_widgets(self):
        self.__file1_label = tk.Label(
            self.__root, text="Selecciona el archivo del problema 1:"
        )
        self.__file1_label.pack()

        self.__file1_entry = tk.Entry(self.__root, width=50)
        self.__file1_entry.pack()

        self.__file1_button = tk.Button(
            self.__root, text="Abrir archivo", command=self.__open_file1
        )
        self.__file1_button.pack()

        tk.OptionMenu(
            self.__root,
            self.__file1_type,
            AlgorithmOptions.BRUTE_FORCE.value,
            AlgorithmOptions.DYNAMIC.value,
            AlgorithmOptions.GREEDY.value,
        ).pack()

        self.__file2_label = tk.Label(
            self.__root, text="Selecciona el archivo del problema 2:"
        )
        self.__file2_label.pack()

        self.__file2_entry = tk.Entry(self.__root, width=50)
        self.__file2_entry.pack()

        self.__file2_button = tk.Button(
            self.__root, text="Abrir archivo", command=self.__open_file2
        )
        self.__file2_button.pack()

        tk.OptionMenu(
            self.__root,
            self.__file2_type,
            AlgorithmOptions.BRUTE_FORCE.value,
            AlgorithmOptions.DYNAMIC.value,
            AlgorithmOptions.GREEDY.value,
        ).pack()

        self.__read_button = tk.Button(
            self.__root, text="Leer archivos", command=self.__read_files
        )
        self.__read_button.pack()

    def __open_file1(self):
        file_path: str = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        if file_path:
            self.__file1_path = file_path
            self.__file1_entry.delete(0, tk.END)
            self.__file1_entry.insert(0, file_path)

    def __open_file2(self):
        file_path: str = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        if file_path:
            self.__file2_path = file_path
            self.__file2_entry.delete(0, tk.END)
            self.__file2_entry.insert(0, file_path)

    def __read_file(self, file_path):
        try:
            file = open(file_path, "r")
            return file
        except Exception as e:
            print(f"Error al leer el archivo {file_path}: {e}")
            return []

    def __get_palindrome_solution(self, file) -> None:
        len_lines = int(file.readline().strip())
        actions: dict[str, Callable] = {
            AlgorithmOptions.BRUTE_FORCE.value: max_subsequence_palindrome,
            AlgorithmOptions.DYNAMIC.value: max_dynamic_palindrome,
            AlgorithmOptions.GREEDY.value: greedy_palindromic_substring,
        }

        option: str = self.__file1_type.get()
        action: Callable | None = actions.get(option)

        if action is None:
            return None

        for _ in range(len_lines):
            text: str = normalizer(file.readline())
            print(action(text))

        file.close()

    def __get_party_solution(self, file) -> None:
        len_problems = int(file.readline().strip())
        actions: dict[str, Callable] = {
            AlgorithmOptions.BRUTE_FORCE.value: brute_force_party,
            AlgorithmOptions.DYNAMIC.value: max_dinamic_invite_values,
        }

        option: str = self.__file2_type.get()
        action = actions.get(option)

        if action is None:
            return None

        for _ in range(len_problems):
            len_matrix = int(file.readline().strip())
            matrix: list[list[int]] = []
            weights: list[int] = []

            for _ in range(len_matrix):
                row = list(map(int, file.readline().strip().split()))

                if len(row) != len_matrix:
                    print("Error: la matriz no es cuadrada")
                    return None

                matrix.append(row)

            weights = list(map(int, file.readline().strip().split()))
            result = action(matrix, weights)
            print(" ".join(str(x) for x in result))

        file.close()

    def __read_files(self):
        if self.__file1_path:
            file1 = self.__read_file(self.__file1_path)
            option: str = self.__file1_type.get()

            print(
                f"Contenido del archivo del problema 1 con {option} ({self.__file1_path}):"
            )
            self.__get_palindrome_solution(file1)

        if self.__file2_path:
            file2 = self.__read_file(self.__file2_path)
            option: str = self.__file2_type.get()
            print(
                f"Contenido del archivo del problema 2 {option} ({self.__file2_path}):"
            )

            self.__get_party_solution(file2)
