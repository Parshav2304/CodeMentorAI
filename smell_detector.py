def detect_smells(metrics):
    smells = []

    if metrics["complexity"] > 10:
        smells.append("High complexity")

    if metrics["nesting"] > 4:
        smells.append("Deep nesting")

    if metrics["loops"] > 5:
        smells.append("Loop-heavy logic")

    if metrics["exceptions"] == 0:
        smells.append("No exception handling")

    return smells
