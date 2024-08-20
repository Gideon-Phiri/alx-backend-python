# 0x01-python_async_function

## Overview

This project demonstrates the use of Python's `asyncio` module to handle asynchronous operations. The tasks in this project cover the basics of async programming, including creating coroutines, running them concurrently, measuring runtime, and working with asyncio tasks.

## Table of Contents

- [Project Setup](#project-setup)
- [Tasks](#tasks)
  - [Task 0: The Basics of Async](#task-0-the-basics-of-async)
  - [Task 1: Let's Execute Multiple Coroutines at the Same Time with Async](#task-1-lets-execute-multiple-coroutines-at-the-same-time-with-async)
  - [Task 2: Measure the Runtime](#task-2-measure-the-runtime)
  - [Task 3: Tasks](#task-3-tasks)
  - [Task 4: More Tasks](#task-4-more-tasks)
- [Testing the Project](#testing-the-project)
- [License](#license)

## Project Setup

**Clone the repository:**

   ```bash
   git clone https://github.com/Gideon-Phiri/alx-backend-python.git
   cd 0x01-python_async_function
   ```

## Tasks

### Task 0: The Basics of Async

- **Objective:** Create an asynchronous coroutine `wait_random` that takes in an integer `max_delay` (default 10) and waits for a random delay between 0 and `max_delay` (inclusive) seconds. It returns the actual delay.

- **File:** `0-basic_async_syntax.py`

 - **Usage Example:**

  ```bash
  bob@dylan:~$ cat 0-main.py
  #!/usr/bin/env python3

  import asyncio

  wait_random = __import__('0-basic_async_syntax').wait_random

  print(asyncio.run(wait_random()))
  print(asyncio.run(wait_random(5)))
  print(asyncio.run(wait_random(15)))

  ```

  ```bash
  ./0-main.py
  ```

### Task 1: Let's Execute Multiple Coroutines at the Same Time with Async

- **Objective:** Create an async routine `wait_n` that takes two integers `n` and `max_delay`. It spawns `wait_random` `n` times with the specified `max_delay` and returns the list of all delays in ascending order.

- **File:** `1-concurrent_coroutines.py`

### Task 2: Measure the Runtime

- **Objective:** Create a function `measure_time` that measures the total execution time for `wait_n(n, max_delay)` and returns `total_time / n`.

- **File:** `2-measure_runtime.py`

### Task 3: Tasks

- **Objective:** Create a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

- **File:** `3-tasks.py`

### Task 4: More Tasks

- **Objective:** Modify the `wait_n` function to create a new function `task_wait_n`, which is similar but uses `task_wait_random` instead of `wait_random`.

- **File:** `4-tasks.py`

## Testing the Project

To test the project, you can use `pytest` for unit testing and `mypy` for type checking:

1. **Run tests:**

   ```bash
   pytest
   ```

2. **Check type annotations:**

   ```bash
   mypy --strict .
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

---
