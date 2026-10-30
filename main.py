from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def show_state(ds, kind):
    items = ds.to_list()
    if kind == "stack":
        print(f"State (top -> bottom): {items}")
        if isinstance(ds, ArrayStack):
            print(f"Raw array: {ds.data}  top index: {ds.top}")
    else:
        print(f"State (front -> rear): {items}")
        if isinstance(ds, ArrayQueue):
            print(f"Raw array: {ds.data}  front index: {ds.front}  size: {ds.size}")


def choose_structure():
    print("\nChoose an implementation:")
    print("  1. ArrayStack\n  2. LinkedStack\n  3. ArrayQueue (circular)\n  4. LinkedQueue\n  0. Exit")
    choice = read_int("Choice: ")
    if choice == 0:
        return None, None
    if choice in (1, 3):
        cap = read_int("Capacity: ")
        while cap <= 0:
            cap = read_int("Capacity must be positive: ")
        return (ArrayStack(cap), "stack") if choice == 1 else (ArrayQueue(cap), "queue")
    if choice == 2:
        return LinkedStack(), "stack"
    if choice == 4:
        return LinkedQueue(), "queue"
    print("Invalid choice.")
    return choose_structure()


def operate(ds, kind):
    if kind == "stack":
        names = ["push", "pop", "peek", "is_empty", "is_full"]
    else:
        names = ["enqueue", "dequeue", "peek_front", "is_empty", "is_full"]
    while True:
        print(f"\nOperations: " + ", ".join(f"{i+1}. {n}" for i, n in enumerate(names)) + ", 6. switch structure")
        op = read_int("Operation: ")
        try:
            if op == 1:
                value = input("Value: ")
                getattr(ds, names[0])(value)
                print(f"{names[0]}({value!r}) done.")
            elif op in (2, 3):
                print(f"{names[op-1]}() -> {getattr(ds, names[op-1])()!r}")
            elif op == 4:
                print("is_empty() ->", ds.is_empty())
            elif op == 5:
                print("is_full() ->", ds.is_full())
            elif op == 6:
                return
            else:
                print("Invalid operation.")
                continue
        except (IndexError, OverflowError) as err:
            print("Error:", err)
        show_state(ds, kind)


def main():
    while True:
        ds, kind = choose_structure()
        if ds is None:
            print("Goodbye!")
            return
        operate(ds, kind)


if __name__ == "__main__":
    main()
