# Alphabetic

A Python script that generates regular expressions from deterministic finite automata.

## How to Run

### Requirements

- Python 3.x (no additional packages needed)

### Run the script directly:
   ```bash
   git clone https://github.com/hevertonn/alphabetic.git

   cd alphabetic/

   python src/main.py
   ```

The program will ask you to provide the number of automaton states, alphabet and transitions, and then display the generated regular expression.

## What It Does

When you run the script, it:
- Processes the provided automaton to generate an equivalent regular expression
- Prints the resulting regular expression to the console

## Example Output

```
Generated regular expression: (a+b)*abb
```
