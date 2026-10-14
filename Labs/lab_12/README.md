# NSU Python — Lab 12
## NumPy and Pandas

Complete at least **10 core tasks**, including **Tasks 10–14** and at least five tasks from Tasks 1–9. All 14 are recommended. Tasks 15–16 are optional bonuses and do not replace core tasks.

### Setup
Activate your course virtual environment, select it in VS Code, then run:

```bash
python -m pip install numpy pandas
python examples.py
python tasks.py
```

Use `python3` instead if that is your system's Python command. Python 3.10+ is required. Record the versions that work in your environment. No plotting or machine-learning packages are needed.

### Files
- `tasks.py`: student assignment.
- `examples.py`: introductory demonstrations.
- `students.csv`: fictional student records, including missing, non-numeric, and out-of-range scores.
- `assignments.csv`: fictional two-assignment scores for the weighted-score bonus.
- `tasks_solution.py`: instructor reference. **Remove before distributing to students.**

Run from this directory so relative CSV paths resolve. Tasks 13 and 14 depend on Task 12. Keep the supplied files unchanged. Export results to new filenames.

### Data rules
Scores must be numeric and between 0 and 100, inclusive. A blank or non-numeric score is missing after conversion. Missing scores do not automatically represent zero. Exclude invalid scores from the report and disclose the number excluded. The pass threshold is 60. Calculate the pass percentage over valid scores only.

### Submission
Submit `tasks.py`, the supplied CSV files, exported reports, and a short README under `lab_12/` in your course GitHub repository. Identify completed tasks, describe the data-cleaning rule, and record NumPy/Pandas versions. Do not submit instructor solutions.

### Review criteria
Correct shapes and axis use, vectorized calculations, correct filtering, explicit treatment of invalid data, reproducible exports, and readable code. Compare floating-point results with a tolerance rather than relying on exact display formatting. Table spacing and dtype labels can differ between versions.
