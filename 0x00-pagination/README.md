# Pagination Project

This project involves implementing pagination for a dataset of popular baby names using Python. The project is divided into several tasks that build upon each other to achieve different aspects of pagination, including simple pagination, hypermedia pagination, and deletion-resilient pagination.

## Project Structure

- `0-simple_helper_function.py`: Contains the `index_range` function to calculate the start and end index for a given page and page size.
- `1-simple_pagination.py`: Implements the `Server` class with methods to load the dataset and return a paginated page of the dataset.
- `2-hypermedia_pagination.py`: Extends the `Server` class to include a method that returns pagination metadata along with the paginated data.
- `3-hypermedia_del_pagination.py`: Further extends the `Server` class to ensure pagination is resilient to deletions in the dataset.

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the `pycodestyle` style (version 2.5.*).
- The length of your files will be tested using `wc`.
- All your modules should have documentation.
- All your functions should have documentation.
- All your functions and coroutines must be type-annotated.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/alx-backend.git
    cd alx-backend/0x00-pagination
    ```

2. Ensure you have the `Popular_Baby_Names.csv` file in the directory:
    ```bash
    wget http://path_to_your_csv_file/Popular_Baby_Names.csv
    ```

3. Run the main files to test each task:
    ```bash
    ./0-main.py
    ./1-main.py
    ./2-main.py
    ./3-main.py
    ```

## Tasks

### Task 0: Simple Helper Function

Implement a function `index_range` that takes two integer arguments `page` and `page_size`. The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

### Task 1: Simple Pagination

Implement a `Server` class to paginate a database of popular baby names. The class should include a method `get_page` that takes two integer arguments `page` and `page_size` and returns the appropriate page of the dataset.

### Task 2: Hypermedia Pagination

Extend the `Server` class to include a method `get_hyper` that takes the same arguments as `get_page` and returns a dictionary containing pagination metadata along with the paginated data.

### Task 3: Deletion-Resilient Hypermedia Pagination

Further extend the `Server` class to ensure pagination is resilient to deletions in the dataset. Implement a method `get_hyper_index` that returns pagination metadata that accounts for deletions in the dataset.

## License

This project is licensed under the MIT License.

## Author
[Abdelhafid Mahmoudi](https://github.com/abdelhafid-mahmoudi-env/alx-backend.git)
