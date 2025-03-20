def main():

    print("Siema \n Co masz do zrobienia?\n ele ele oo")

    # Początkowa lista zadań
    tasks = []

    # 1: gadka
    print("\nPodaj swoje zadania. \n By zakończyc wprowadzanie Enter")


    while True:
        task = input("> ")
        if task.strip() == "":
            break
        tasks.append(task)

    # Główna pętla, umożliwiająca zarządzanie lista
    while True:
        print("\nZadania:")
        if not tasks:
            print("Fajrant")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

        print("\nOpcje:")
        print("1. Dodaj nowe zadanie")
        print("2. Zrobione")
        print("3. Zakończ program")

        choice = input("\nTwój wybór: ").strip()

        if choice == "1":
            # Dodawanie nowego zadania
            new_task = input("Podaj treść nowego zadania: ")
            if new_task.strip():#strip usuwa spacje brak czegogolwiek zwroci flase
                tasks.append(new_task)
                print("Dodano zadanie do listy.")
            else:
                print("Nie podano żadnego zadania, powrót do menu.")

        elif choice == "2":
            # Usuwanie wybranego zadania
            if not tasks:
                print("Brak zadań do usunięcia.")
            else:
                task_number = input("Podaj numer zadania, które chcesz usunąć: ")
                if task_number.isdigit():# isdigit() to sprawdza czy sa same cyfry
                    task_number = int(task_number) #przypisuje int
                    if task_number > 0 and task_number <= len(tasks): #ograniczenie do wielkosci tabeli
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Zadanie \"{removed_task}\" zostało usunięte.")
                    else:
                        print("Niepoprawny numer zadania.")
                else:
                    print("Wprowadzony tekst nie jest liczbą.")

        elif choice == "3":
            # Zakończenie programu
            print("Dziękuję za skorzystanie z programu. Do zobaczenia!")
            break

        else:
            print("Nie rozpoznano polecenia. Spróbuj ponownie.")


if __name__ == "__main__":
    main()