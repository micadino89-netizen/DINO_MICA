def is_balanced(text):
    """Return True if every ()[]{} in text is properly matched and nested."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = LinkedStack()
    for ch in text:
        if ch in "([{":
            stack.push(ch)
        elif ch in pairs:
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False
    return stack.is_empty()       


def simulate_print_queue(jobs):
    """jobs: list of (job_id, pages). Prints them in FIFO order."""
    queue = LinkedQueue()
    for job in jobs:
        queue.enqueue(job)
        print(f"Enqueued job {job[0]} ({job[1]} pages)")
    print("\nPrinting in FIFO order:")
    order, total = 0, 0
    while not queue.is_empty():
        job_id, pages = queue.dequeue()
        order += 1
        total += pages
        print(f"  #{order}: printing {job_id} ({pages} pages) | total pages printed: {total}")
    print("All jobs printed.")


if __name__ == "__main__":
    print("=== Balanced parentheses ===")
    for s in ["()", "([]{})", "{[()]}", "(]", "((())", "())(", "a(b[c]{d})e", ""]:
        print(f"{s!r:15} -> {'balanced' if is_balanced(s) else 'NOT balanced'}")

    print("\n=== Print queue simulation ===")
    simulate_print_queue([("DOC-101", 5), ("DOC-102", 12), ("DOC-103", 1), ("DOC-104", 8)])
