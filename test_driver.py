from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def attempt(label, func):
    try:
        print(f"{label} -> {func()!r}")
    except (IndexError, OverflowError) as err:
        print(f"{label} -> {type(err).__name__}: {err}")


def test_stack(stack, name):
    print(f"\n--- {name} ---")
    for x in "ABC":
        stack.push(x)
    print("After push A, B, C (top->bottom):", stack.to_list())
    attempt("pop()", stack.pop)
    attempt("peek()", stack.peek)
    print("State:", stack.to_list())
    attempt("pop()", stack.pop)
    attempt("pop()", stack.pop)
    attempt("pop() on empty (underflow)", stack.pop)
    attempt("peek() on empty", stack.peek)


def test_queue(queue, name):
    print(f"\n--- {name} ---")
    for x in "ABC":
        queue.enqueue(x)
    print("After enqueue A, B, C (front->rear):", queue.to_list())
    attempt("dequeue()", queue.dequeue)
    attempt("peek_front()", queue.peek_front)
    attempt("dequeue()", queue.dequeue)
    attempt("dequeue()", queue.dequeue)
    attempt("dequeue() on empty (underflow)", queue.dequeue)


if __name__ == "__main__":
    s = ArrayStack(3)
    print("--- ArrayStack overflow ---")
    for x in (1, 2, 3):
        s.push(x)
    print("Full?", s.is_full(), s.to_list())
    attempt("push(4) on full (overflow)", lambda: s.push(4))

    test_stack(ArrayStack(5), "ArrayStack")
    test_stack(LinkedStack(), "LinkedStack")
  
    print("\n--- ArrayQueue wrap-around (capacity 4) ---")
    q = ArrayQueue(4)
    for x in "ABCD":
        q.enqueue(x)
    print("Full:", q.data, "front =", q.front, "size =", q.size)
    attempt("enqueue('E') on full (overflow)", lambda: q.enqueue("E"))
    attempt("dequeue()", q.dequeue)
    attempt("dequeue()", q.dequeue)
    q.enqueue("E")     
    q.enqueue("F")     
    print("After dequeue x2 and enqueue E, F:")
    print("Raw array:", q.data, "front =", q.front, "size =", q.size)
    print("Logical order (front->rear):", q.to_list())

    test_queue(ArrayQueue(5), "ArrayQueue")
    test_queue(LinkedQueue(), "LinkedQueue")

    print("\n--- LinkedQueue rear reset ---")
    lq = LinkedQueue()
    lq.enqueue(1)
    lq.dequeue()
    print("front:", lq.front, "rear:", lq.rear)
    lq.enqueue(2)
    print("After enqueue(2):", lq.to_list())
