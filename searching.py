from pathlib import Path
import json

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

    if sv_data is not None:
        print(f"Načtená data: {sv_data}")
        vysledek = linear_search(sv_data, number)
        print(f"Číslo {number} nalezeno sekvencne na indexech: {vysledek}")
        bin_ser = binary_search(sv_data, number)
        print(bin_ser)


if __name__ == "__main__":
    main()