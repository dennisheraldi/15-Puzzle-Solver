# 15-Puzzle Solver

## Table of Contents

- [Program Description](#program-description)
- [Program Demo](#program-demo)
- [Program Requirements](#program-requirements)
- [How to Run the Program](#how-to-run-the-program)
- [Author](#author)

## Program Description

This Python-based program solves the classic 15-Puzzle problem using the **Branch and Bound** algorithm. The algorithm evaluates nodes based on a "bound" that combines the cost to reach a given state from the root and an estimated cost to reach the goal state. The estimation is based on the number of tiles that are not in their correct positions (misplaced tiles).

The program's graphical user interface (GUI) is built using **Tkinter**, allowing for an interactive experience during puzzle-solving.

### Folder and File Structure

- **`src/`**: Contains the source code of the Python program.
- **`test/`**: Stores test data files for different puzzle configurations.
- **`doc/`**: Includes reports and specifications related to the task.
- **`run.bat`**: A batch file for compiling and running the program.
- **`README.md`**: This README file, which provides an overview of the project.

## Program Demo

Here’s a quick preview of the program in action:

![Demo](https://user-images.githubusercontent.com/71638224/161409246-b03d4764-192f-4bde-899b-065d9d575be5.gif)

## Program Requirements

- Python 3.9 or higher

## How to Run the Program

1. **Install Python**: Make sure that Python 3.9 (or a newer version) is installed on your system.
2. **Extract the Project Files**: Download and extract the `Tucil3_13520139.zip` file into a directory of your choice.
3. **Run the Program**:
   - For **CLI** (Command Line Interface) usage, run `run_cli.bat`.
   - For **GUI** usage, run `run_gui.bat`.
4. After launching the program, you’ll be prompted to input a file containing the initial puzzle matrix.
5. Ensure the file you wish to use is located in the `test/` folder.
6. Once the puzzle is loaded, the program will display the following:
   - The **Kurang(i)** function value.
   - The **X** value.
   - Step-by-step solution for the puzzle.
   - Puzzle-solving animation (available in the GUI version).

## Author

**Fachry Dennis Heraldi** (13520139)  
For the completion of the IF2211 *Strategi Algoritma* assignment
