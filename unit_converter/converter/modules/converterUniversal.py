def comprimentos(value: float, first_choice: str, second_choice: str) -> float:
    comprimentos = ["km", "hm", "dam", "m", "dm", "cm", "mm",]

    first_index = [x for x in range(len(comprimentos)) if comprimentos[x] == first_choice.lower()][0]
    second_index = [x for x in range(len(comprimentos)) if comprimentos[x] == second_choice.lower()][0]

    distance = second_index - first_index

    return value * 10 ** distance

def pesos(value: float, first_choice: str, second_choice: str) -> float:
    pesos = ["kg", "hg", "dag", "g", "dg", "cg", "mg",]

    first_index = [x for x in range(len(pesos)) if pesos[x] == first_choice.lower()][0]
    second_index = [x for x in range(len(pesos)) if pesos[x] == second_choice.lower()][0]

    distance = second_index - first_index

    return value * 10 ** distance

if __name__ == "__main__":
    print(comprimentos(2, "m", "km"))
    print(comprimentos(5, "km", "m"))

    print(pesos(5, "g", "kg"))
    print(pesos(5, "kg", "mg"))
    print(pesos(22, "kg", "dag"))
