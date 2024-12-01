import random
# Funkce pro generování mřížky automatu

def get_slot():
    symbols = ['skibidi', 'hawk_tuah', 'sigma', 'rizzler', 'darius', 'freakbob']
    # Pravděpodobnosti pro výherní kombinace: řádky, sloupce, diagonály
    #probabilities = [1 / 3, 1 / 3, 1 / 5, 1 / 5, 1 / 8, 1 / 10]
    probabilities = [1 / 2400, 1 / 2400, 1 / 4000, 1 / 4000, 1 / 6400, 1 / 10]
    total_probability = sum(probabilities)
    normalized_probabilities = [p / total_probability for p in probabilities]

    # Funkce pro náhodný výběr symbolu na základě pravděpodobnosti
    def choose_symbol():
        return random.choices(symbols, normalized_probabilities)[0]

    # Funkce pro generování mřížky a kontrolu výherních kombinací
    def generate_grid():
        # Generování mřížky 3x3
        grid = [[choose_symbol() for _ in range(3)] for _ in range(3)]

        # Kontrola výherních kombinací
        def check_win(grid):
            # Kontrola řádků
            for row in grid:
                if row[0] == row[1] == row[2]:
                    return True
            # Kontrola sloupců
            for col in range(3):
                if grid[0][col] == grid[1][col] == grid[2][col]:
                    return True
            # Kontrola diagonál
            if grid[0][0] == grid[1][1] == grid[2][2]:
                return True
            if grid[0][2] == grid[1][1] == grid[2][0]:
                return True
            return False

        # Snažíme se generovat výherní mřížku s danou pravděpodobností
        for p in normalized_probabilities:
            if random.random() < p:
                while not check_win(grid):  # Pokud není výherní kombinace, generujeme novou mřížku
                    grid = [[choose_symbol() for _ in range(3)] for _ in range(3)]
                break

        return grid

    return generate_grid()  # Vygeneruje a vrátí mřížku


# Funkce pro kontrolu výherních kombinací
def check_winnings(grid):
    winnings = []
    # Kontrola horizontálních řad
    if grid[0][0] == grid[0][1] == grid[0][2]:
        winnings.append(grid[0][0])
    if grid[1][0] == grid[1][1] == grid[1][2]:
        winnings.append(grid[1][0])
    if grid[2][0] == grid[2][1] == grid[2][2]:
        winnings.append(grid[2][0])

    # Kontrola diagonál
    if grid[0][0] == grid[1][1] == grid[2][2]:
        winnings.append(grid[0][0])
    if grid[2][0] == grid[1][1] == grid[0][2]:
        winnings.append(grid[2][0])

    return winnings

def get_winnings_value(winnings):
    symbols = ['skibidi', 'hawk_tuah', 'sigma', 'rizzler', 'darius', 'freakbob']
    probabilities = [3, 3, 5, 5, 8, 10]
    win = 0
    for symbol in winnings:
        win += probabilities[symbols.index(symbol)]
    return win

def get_win_song(winnings):
    symbols = ['skibidi', 'hawk_tuah', 'sigma', 'rizzler', 'darius', 'freakbob']
    highest_index = -1  # Začneme s nejnižším možným indexem
    highest_symbol = None  # Tohle bude uchovávat symbol s nejvyšším indexem

    for winning_symbol in winnings:
        index = symbols.index(winning_symbol)  # Najdeme index symbolu
        if index > highest_index:  # Pokud je tento symbol "hodnotnější"
            highest_index = index
            highest_symbol = winning_symbol
    return f'{highest_symbol}.mp3'


def check_winning_lines(slot_symbols):
    winning_lines = []  # Seznam pro uchování výherních řad

    # Zkontrolujeme horizontální řady
    for row in range(len(slot_symbols)):
        if len(set(slot_symbols[row])) == 1:  # Pokud všechny symboly v řádku jsou stejné
            winning_lines.append([(row, col) for col in range(len(slot_symbols[row]))])  # Přidáme celou řadu

    # Zkontrolujeme diagonály (předpokládáme, že mřížka je čtvercová)
    if len(slot_symbols) == len(slot_symbols[0]):  # Pokud je mřížka čtvercová
        # Diagonála zleva doprava
        diagonal1 = [slot_symbols[i][i] for i in range(len(slot_symbols))]
        if len(set(diagonal1)) == 1:
            winning_lines.append([(i, i) for i in range(len(slot_symbols))])

        # Diagonála zprava doleva
        diagonal2 = [slot_symbols[i][len(slot_symbols) - 1 - i] for i in range(len(slot_symbols))]
        if len(set(diagonal2)) == 1:
            winning_lines.append([(i, len(slot_symbols) - 1 - i) for i in range(len(slot_symbols))])

    return winning_lines

