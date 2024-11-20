def decifra_cesare(messaggio, chiave):
    alfabeto = "ABCDEFGHILMNOPQRSTUVZ"
    risultato = ""

    for char in messaggio:
        if char.isalpha():
            is_upper = char.isupper()
            base = alfabeto.upper() if is_upper else alfabeto.lower()

            index = base.find(char)
            if index != -1:
                new_index = (index - chiave) % len(alfabeto)
                risultato += base[new_index]
            else:
                risultato += char

        else:
            risultato += char

    return risultato


def brute_force_cesare(messaggio):
    alfabeto = "ABCDEFGHILMNOPQRSTUVZ"

    print("\nTentativi di decifratura:")
    for chiave in range(len(alfabeto)):
        decifrato = decifra_cesare(messaggio, chiave)
        print(f"Chiave {chiave}: {decifrato}")


messaggio_cifrato = input("Inserisci il messaggio cifrato: ")

brute_force_cesare(messaggio_cifrato)