def generate_task(cluster_id):
    tasks = {
        0: "Practice writing clean loops using list comprehensions.",
        1: "Refactor code into smaller functions.",
        2: "Solve recursion-based problems with base case emphasis."
    }
    return tasks.get(cluster_id, "General Python practice recommended.")
