def comprimentos(value: float, first_choice: str, second_choice: str) -> float:
    comprimentos = ["quilometro", "hectometro", "decametro", "metro", "decimetro", "centimetro", "milimetro",]

    first_index = [x for x in range(len(comprimentos)) if comprimentos[x] == first_choice.lower()][0]
    second_index = [x for x in range(len(comprimentos)) if comprimentos[x] == second_choice.lower()][0]

    distance = second_index - first_index

    return value * 10 ** distance

def pesos(value: float, first_choice: str, second_choice: str) -> float:
    pesos = ["quilograma", "hectograma", "decagrama", "grama", "decagrama", "centigrama", "miligrama",]

    first_index = [x for x in range(len(pesos)) if pesos[x] == first_choice.lower()][0]
    second_index = [x for x in range(len(pesos)) if pesos[x] == second_choice.lower()][0]

    distance = second_index - first_index

    return value * 10 ** distance

if __name__ == "__main__":
    print(comprimentos(2, "metro", "quilometro"))
    print(comprimentos(5, "quilometro", "metro"))

    print(pesos(5, "grama", "quilograma"))
    print(pesos(5, "quilograma", "miligrama"))