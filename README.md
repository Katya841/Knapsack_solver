


- **tests/**:  Folder with test input data
- **output/**: Output folder
- **answers/**:  Answers folder 
- **knapsack_cylp.py**: Source code interaction files with the chosen MIP library
- **cut_generator.py**: Redefined separation procedure source code
- **gen_test.py**: Test generation
- **test_solver.py**: Testing script

## Installation
1. **Clone the repository**

   ```bash
   $ git clone https://github.com/Katya841/Knapsack_solver
   $ cd Knapsack_solver
   ```
2. **Create and Activate a Virtual Environment, installing libraries**
   ```bash
   $ <python_path> -m venv <venv_name>
   $ source <venv_name>/bin/activate
   (<venv_name>)$ pip install mip pytest
   ```

## Running the programm

1. **Test execution**
   ```bash
   $ pytest
   ```
    This command runs the solver on all tests provided in the tests folder and compares the results with the answers from the answers folder

2. **Test execution**
  ![alt text](<Screenshot from 2024-10-11 22-59-44.png>)
3. **Running your own test(run.py)**

    1. File structure filename_in and filename_out

       filename_in
       ```bash
        N b
        a[i] c[i]
        ```
       filename_out
       ```bash
        best_cost cnt total_cost total_weight
        x[i]
       ```
    Execute run.py and enter the file name of your input data and the file name for saving the result:
    ![alt text](<Screenshot from 2024-10-11 23-56-51.png>)
    
