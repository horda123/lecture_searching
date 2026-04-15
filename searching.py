from pathlib import Path
import json
import time

def binary_search(sekvence, number):
    while len(sekvence) > 0:
        mid = len(sekvence)//2
        if number == sekvence[mid]:
            return True
        elif number < sekvence[mid]:
            sekvence = sekvence[:mid]
        elif number > sekvence[mid]:
            sekvence = sekvence[mid + 1:]
    return False

def linear_search(sekvence, number):
    if not sekvence:
        return []

    indices = []
    for index, value in enumerate(sekvence):
        if value == number:
            indices.append(index)
    return indices

def read_data(file_name, field):
    cwd_path = Path.cwd()
    file_path = cwd_path / file_name

    with open(file_path, "r") as file:
         data = json.load(file)

    if field in data:
        return data[field]
    else:
        return None

def main():
    file_name = "sequential.json"
    field = "ordered_numbers"
    number = 14
    sv_data = read_data(file_name, field)

    print(f"Načtená data: {sv_data}")
    start = time.perf_counter()
    vysledek = linear_search(sv_data, number)
    end = time.perf_counter()
    print(f"Číslo {number} nalezeno sekvencne na indexech: {vysledek}")
    b_start = time.perf_counter()
    bin_ser = binary_search(sv_data, number)
    b_end = time.perf_counter()
    print(bin_ser)
    duration = end - start
    b_duration = b_end - b_start
    print(f"Sekvencni hledac bezel {duration:.8f} s")
    print(f"Binarni hledac bezel {b_duration:.8f} s")
    a = b_duration/duration * 100
    print(round(a, 1))

if __name__ == "__main__":
    main()