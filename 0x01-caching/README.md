# Caching Systems

This project implements various caching algorithms in Python. Each caching system inherits from a base class `BaseCaching` and implements different cache replacement policies.

## File Overview

- **`base_caching.py`**: Contains the `BaseCaching` class with basic cache management methods.
- **`0-basic_cache.py`**: Implements a basic caching system with no limits.
- **`1-fifo_cache.py`**: Implements a FIFO (First-In-First-Out) caching system.
- **`2-lifo_cache.py`**: Implements a LIFO (Last-In-First-Out) caching system.
- **`3-lru_cache.py`**: Implements an LRU (Least Recently Used) caching system.
- **`4-mru_cache.py`**: Implements an MRU (Most Recently Used) caching system.

## Usage

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```

3. Run the test files to see the caching systems in action:
   ```bash
   ./0-main.py
   ./1-main.py
   ./2-main.py
   ./3-main.py
   ./4-main.py
   ```

## Author and Contributors
   Abdelhafid Mahmoudi: [GitHub](https://github.com/abdelhafid-mahmoudi-env)

## License
   This project is licensed under the MIT License.
