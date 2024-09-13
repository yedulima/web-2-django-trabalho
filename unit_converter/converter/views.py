from django.shortcuts import render
from .forms import Temperature, Length, Weight
from .modules import converterUniversal

description_texts: dict = {
    "Temperatura": "A temperatura é uma medida da energia térmica de um objeto ou substância. Ela pode ser expressa em diferentes escalas, sendo as mais comuns Celsius (°C), Fahrenheit (°F) e Kelvin (K). No sistema métrico, o Celsius é amplamente utilizado, enquanto o Kelvin é a unidade oficial no Sistema Internacional (SI), essencial na ciência por começar no zero absoluto, o ponto onde todas as partículas param de se mover. O Fahrenheit é mais comum em alguns países como os Estados Unidos. A conversão entre essas unidades é importante para garantir precisão em áreas como ciência, saúde e meteorologia.",
    "Tamanho": "O tamanho, ou comprimento, refere-se à dimensão linear de um objeto. No Sistema Internacional de Unidades (SI), a unidade básica de medida de comprimento é o metro (m). No entanto, também usamos submúltiplos como o centímetro (cm) e o milímetro (mm) para medir objetos menores, e múltiplos como o quilômetro (km) para distâncias maiores. Outras unidades, como a polegada e a milha, são usadas em sistemas diferentes, como o anglo-saxão. A conversão entre essas unidades é essencial em áreas como construção, design e física.",
    "Peso": "O peso é uma medida que representa a força gravitacional exercida sobre um objeto com massa. Ele é comumente medido em unidades como quilogramas (kg), gramas (g) e toneladas (t). No Sistema Internacional de Unidades (SI), o quilograma é a unidade padrão para medir a massa. Para facilitar conversões em diferentes contextos, usamos múltiplos e submúltiplos, como o grama, que é equivalente a um milésimo de quilograma. A escolha da unidade de medida depende da precisão necessária, com valores maiores geralmente sendo medidos em quilogramas ou toneladas, e menores em gramas ou miligramas.",
}

def temperature(req):
    actual_temperature: float = 0

    if req.method == "POST":
        form = Temperature(req.POST)

        if form.is_valid():
            first_choice: str = form.cleaned_data['first_choice']
            second_choice: str = form.cleaned_data['second_choice']
            value: float = form.cleaned_data['value']

            actual_temperature = value

            if first_choice == second_choice:
                actual_temperature = value
            elif first_choice == "Celsius" and second_choice == "Fahrenheit":
                actual_temperature = value * 1.8 + 32
            elif first_choice == "Fahrenheit" and second_choice == "Celsius":
                actual_temperature = ((value - 32) * 5)/9
            elif first_choice == "Celsius" and second_choice == "Kelvin":
                actual_temperature = value + 273
            elif first_choice == "Fahrenheit" and second_choice == "Kelvin":
                actual_temperature = ((value - 32) * 5)/9
            elif first_choice == "Kelvin" and second_choice == "Celsius":
                actual_temperature = value - 273
            elif first_choice == "Kelvin" and second_choice == "Fahrenheit":
                actual_temperature = (((value - 273.15) * 9)/5) + 32
    
    else:
        actual_temperature: float = 0
        first_choice = ''
        second_choice = ''
        form = Temperature()

    return render(req, 'converter/calculator.html', {
        "key_word": "Temperatura",
        "form": form,
        "description": description_texts["Temperatura"],
        "actual_value": actual_temperature,
        "first_choice": first_choice.lower(),
        "second_choice": second_choice.lower(),
    })

def lenght(req):
    actual_lenght: float = 0
    
    if req.method == "POST":
        form = Length(req.POST)

        if form.is_valid():
            first_choice: str = form.cleaned_data['first_choice']
            second_choice: str = form.cleaned_data['second_choice']
            value: float = form.cleaned_data['value']

            actual_lenght = converterUniversal.comprimentos(value, first_choice, second_choice)
    
    else:
        actual_lenght: float = 0
        first_choice = ''
        second_choice = ''
        form = Length()

    return render(req, 'converter/calculator.html', {
        "key_word": "Tamanho",
        "form": form,
        "description": description_texts["Tamanho"],
        "actual_value": actual_lenght,
        "first_choice": first_choice.lower(),
        "second_choice": second_choice.lower(),
    })

def weight(req):
    actual_weight: float = 0
    
    if req.method == "POST":
        form = Weight(req.POST)

        if form.is_valid():
            first_choice: str = form.cleaned_data['first_choice']
            second_choice: str = form.cleaned_data['second_choice']
            value: float = form.cleaned_data['value']

            actual_weight = converterUniversal.pesos(value, first_choice, second_choice)
    
    else:
        actual_weight: float = 0
        first_choice = ''
        second_choice = ''
        form = Weight()

    return render(req, 'converter/calculator.html', {
        "key_word": "Peso",
        "form": form,
        "description": description_texts["Peso"],
        "actual_value": actual_weight,
        "first_choice": first_choice.lower(),
        "second_choice": second_choice.lower(),
    })
