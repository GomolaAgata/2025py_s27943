# ---------------------------------------------
# Program: Generator sekwencji DNA w formacie FASTA
# Autor: OpenAI / użytkownik
# Cel: Generowanie losowej sekwencji DNA o podanej długości
#      i zapisanie jej w formacie FASTA z uwzględnieniem ID, opisu i imienia użytkownika.
#
# Kontekst zastosowania:
# Program może być używany w celach edukacyjnych, bioinformatycznych oraz demonstracyjnych
# do testowania narzędzi pracujących z plikami FASTA oraz analizowania podstawowych cech sekwencji DNA.
# ---------------------------------------------

import random  # Moduł do generowania liczb i wyborów losowych

# Funkcja generująca losową sekwencję DNA złożoną z A, C, G, T
def generate_dna_sequence(length):
    return ''.join(random.choices(['A', 'C', 'G', 'T'], k=length))

# Funkcja wstawiająca imię użytkownika w losowe miejsce w sekwencji
# Zwraca zmodyfikowaną sekwencję oraz pozycję wstawienia
def insert_name(sequence, name):
    insert_pos = random.randint(0, len(sequence))  # Losowa pozycja do wstawienia imienia
    return sequence[:insert_pos] + name + sequence[insert_pos:], insert_pos

# Funkcja licząca statystyki sekwencji: procent A, C, G, T oraz zawartość C+G
def calculate_stats(sequence):
    # Usuwamy litery inne niż nukleotydy (np. imię)
    filtered_seq = ''.join([nt for nt in sequence if nt in 'ACGT'])
    total = len(filtered_seq)  # Długość rzeczywistej sekwencji DNA
    # Liczymy wystąpienia każdego nukleotydu
    counts = {nt: filtered_seq.count(nt) for nt in 'ACGT'}
    # Obliczamy procentową zawartość każdego nukleotydu
    percentages = {nt: (count / total) * 100 for nt, count in counts.items()}
    # Obliczamy procent C+G (ważny wskaźnik biologiczny)
    cg_content = ((counts['C'] + counts['G']) / total) * 100
    return percentages, cg_content

# Funkcja formatująca sekwencję DNA do linii po 60 znaków (zgodnie z konwencją FASTA)
def format_fasta_sequence(sequence, line_length=60):
    return '\n'.join([sequence[i:i+line_length] for i in range(0, len(sequence), line_length)])

# Funkcja główna programu
def main():
    # Pobieranie długości sekwencji od użytkownika z walidacją wejścia
    while True:
        try:
            length = int(input("Podaj długość sekwencji: "))  # Przekształcenie wejścia na liczbę
            if length <= 0:
                print("Długość musi być liczbą dodatnią.")  # Obsługa błędu dla liczby <= 0
                continue
            break
        except ValueError:
            print("Proszę podać poprawną liczbę całkowitą.")  # Obsługa błędu konwersji

    # Pobieranie ID sekwencji, opisu i imienia użytkownika
    seq_id = input("Podaj ID sekwencji: ")
    description = input("Podaj opis sekwencji: ")
    name = input("Podaj imię: ")

    # Generowanie losowej sekwencji DNA
    dna_seq = generate_dna_sequence(length)

    # Wstawienie imienia w losowe miejsce sekwencji
    seq_with_name, insert_pos = insert_name(dna_seq, name)

    # Obliczanie statystyk sekwencji (pomijając imię)
    percentages, cg_content = calculate_stats(seq_with_name)

    # Przygotowanie nazwy pliku FASTA na podstawie ID
    fasta_filename = f"{seq_id}.fasta"

    # Zapis sekwencji do pliku FASTA
    with open(fasta_filename, "w") as f:
        f.write(f">{seq_id} {description}\n")  # Nagłówek FASTA
        f.write(format_fasta_sequence(seq_with_name) + "\n")  # Sformatowana sekwencja

    # Wyświetlanie podsumowania i statystyk
    print(f"\nSekwencja została zapisana do pliku {fasta_filename}")
    print("Statystyki sekwencji:")
    for nt in 'ACGT':
        print(f"{nt}: {percentages[nt]:.1f}%")
    print(f"%CG: {cg_content:.1f}")
    print(f"Imię zostało wstawione na pozycji: {insert_pos}")

# Uruchomienie programu
if __name__ == "__main__":
    main()
