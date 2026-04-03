import asyncio

from proc_scheduler import Process, Scheduler, go
import aioconsole
import os

scheduler = Scheduler()
gorutines = []


async def myainput(prompt: str, state: dict) -> bool:
    if state.get("input") is None:
        if not state.get("wait_for_input", False):
            state["wait_for_input"] = True
            answer = await aioconsole.ainput(prompt)
            state["input"] = answer
            return True
    else:
        return True
    return False

@go
async def factorial(state: dict):
    n = state.get("number", 1)
    print("Starting factorial process", n)
    result = 1

    for i in range(n, 10**10):
        result += i
        state["number"] = i
        await asyncio.sleep(0)
    state["result"] = result
    return n == 10**10


@go
async def notes(state: dict):
    if state.get("input") is not None:
        res = str(state["input"])

        if len(res.split()) != 3:
            print("Usage: <номер действия> <ключ> <значение>")
        else:
            if res.startswith("1"):
                state[res.split()[1]] = res.split()[-1]
            elif res.startswith("2"):
                print(state.get(res.split()[1]))
            else:
                return True

        del state["input"]
        del state["wait_for_input"]

    await myainput(
        "Доступные действия:\n1 - Добавить заметку\n2 - Прочитать заметку", state
    )
    return False


@go
async def flag(state: dict):
    print("Flag process started")
    state["flag"] = os.environ.get("FLAG", "gis{***********}")
    return True


def menu():
    print("\n==============================")
    print("         Мои Горутины         ")
    print("==============================")
    print("1. Запустить все горутины")
    print("2. Добавить горутину")
    print("3. Выход")
    print("\nДоступные сервисы:")
    print("- Факториал")
    print("- Флаг")
    print("- Заметки")


def choose_go():
    print("\nКакую горутину добавить?")
    print("1. Факториал")
    print("2. Флаг")
    print("3. Заметки")
    print("4. Назад")
    choice = input("Введите номер варианта: ").strip()

    if choice == "1":
        if factorial in gorutines:
            print("\n⚠️ Факториал уже добавлен!")
        else:
            while True:
                pid_input = input("Введите PID для горутины (целое число): ").strip()
                if pid_input.isdigit():
                    pid = int(pid_input)
                    break
                else:
                    print("Некорректный PID. Попробуйте снова.")
            gorutines.append(factorial)
            scheduler.add_process(Process(f"Факториал {pid}", pid, factorial))
            print(f"Горутина 'Факториал' с PID {pid} успешно добавлена!")
    elif choice == "2":
        if flag in gorutines:
            print("\n⚠️ Флаг уже добавлен!")
        else:
            while True:
                pid_input = input("Введите PID для горутины (целое число): ").strip()
                if pid_input.isdigit():
                    pid = int(pid_input)
                    break
                else:
                    print("Некорректный PID. Попробуйте снова.")
            gorutines.append(flag)
            scheduler.add_process(Process(f"Флаг {pid}", pid, flag))
            print(f"Горутина 'Флаг' с PID {pid} успешно добавлена!")
    elif choice == "3":
        if notes in gorutines:
            print("\n⚠️ Заметки уже добавлены!")
        else:
            while True:
                pid_input = input("Введите PID для горутины (целое число): ").strip()
                if pid_input.isdigit():
                    pid = int(pid_input)
                    break
                else:
                    print("Некорректный PID. Попробуйте снова.")
            gorutines.append(notes)
            scheduler.add_process(Process(f"Заметки {pid}", pid, notes))
            print(f"Горутина 'Заметки' с PID {pid} успешно добавлена!")
    elif choice == "4":
        print("Возврат в главное меню...")
    else:
        print("Неверный выбор. Попробуйте снова.")


async def main():
    while True:
        menu()
        choice = input("\nВведите номер действия: ").strip()
        if choice == "1":
            if not gorutines:
                print("\nНет добавленных горутин. Сначала добавьте хотя бы одну!")
            else:
                print("\nЗапуск всех горутин...")
                await scheduler.run()
        elif choice == "2":
            choose_go()
        elif choice == "3":
            print("\nВыход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    asyncio.run(main())
