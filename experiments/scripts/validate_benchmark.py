import json
import sys
from pathlib import Path

BENCHMARK = Path("experiments/datasets/coding_tasks.json")

def validate():
    if not BENCHMARK.exists():
        print("ERROR: Benchmark file not found.")
        return False

    with BENCHMARK.open() as file:
        data = json.load(file)

    assert data.get("benchmark"), "Missing benchmark name"
    assert data.get("version"), "Missing version"

    tasks = data.get("tasks", [])
    assert tasks, "No tasks found"

    ids = set()
    categories = {}

    for task in tasks:
        for field in ("id", "category", "prompt", "expected_behaviour"):
            assert field in task, f"Task missing field: {field}"

        assert task["id"] not in ids, f"Duplicate ID: {task['id']}"
        assert task["prompt"].strip(), f"Empty prompt: {task['id']}"
        assert task["expected_behaviour"], f"No criteria: {task['id']}"

        ids.add(task["id"])
        category = task["category"]
        categories[category] = categories.get(category, 0) + 1

    print("LOCALPILOT BENCHMARK VALID")
    print("Benchmark:", data["benchmark"])
    print("Version:", data["version"])
    print("Total tasks:", len(tasks))

    for category, count in sorted(categories.items()):
        print(f"  {category}: {count}")

    return True


if __name__ == "__main__":
    try:
        sys.exit(0 if validate() else 1)
    except (json.JSONDecodeError, AssertionError) as error:
        print("VALIDATION FAILED:", error)
        sys.exit(1)
