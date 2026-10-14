
"""
NSU Python — Lab 12
Additional Examples: NumPy and Pandas

Topics:
- NumPy arrays and data types
- Indexing, slicing, and filtering
- Vectorized operations
- Array shapes and matrices
- Mathematical and statistical functions
- Pandas Series and DataFrames
- Selecting and filtering data
- Adding and modifying columns
- Missing values
- Sorting and grouping
- Combining NumPy and Pandas

Requirements:
    pip install numpy pandas

Run:
    python examples.py
"""

import numpy as np
import pandas as pd


# ============================================================
# Example 1 — Creating NumPy arrays
# ============================================================

def example_01():
    numbers = np.array([10, 20, 30, 40, 50])

    print("Array:", numbers)
    print("Type:", type(numbers))
    print("Data type:", numbers.dtype)
    print("Shape:", numbers.shape)
    print("Dimensions:", numbers.ndim)
    print("Size:", numbers.size)

    zeros = np.zeros(5)
    ones = np.ones(4)
    sequence = np.arange(0, 10, 2)
    values = np.linspace(0, 1, 5)

    print("Zeros:", zeros)
    print("Ones:", ones)
    print("Sequence:", sequence)
    print("Linspace:", values)


# ============================================================
# Example 2 — Indexing and slicing
# ============================================================

def example_02():
    numbers = np.array([10, 20, 30, 40, 50, 60])

    print("First:", numbers[0])
    print("Last:", numbers[-1])
    print("First three:", numbers[:3])
    print("Middle:", numbers[2:5])
    print("Every second:", numbers[::2])
    print("Reversed:", numbers[::-1])

    numbers[0] = 100
    print("Modified:", numbers)


# ============================================================
# Example 3 — Vectorized arithmetic
# ============================================================

def example_03():
    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])

    print("Addition:", a + b)
    print("Subtraction:", b - a)
    print("Multiplication:", a * b)
    print("Division:", b / a)
    print("Squares:", a ** 2)
    print("Add 5:", a + 5)

    # NumPy performs element-wise operations.
    # No explicit for loop is required.


# ============================================================
# Example 4 — Boolean indexing and filtering
# ============================================================

def example_04():
    scores = np.array([45, 80, 67, 92, 30, 75])

    mask = scores >= 60

    print("Scores:", scores)
    print("Mask:", mask)
    print("Passed:", scores[mask])
    print("Failed:", scores[scores < 60])

    print("Number passed:", np.sum(mask))
    print("Any above 90:", np.any(scores > 90))
    print("All passed:", np.all(scores >= 60))


# ============================================================
# Example 5 — Statistical operations
# ============================================================

def example_05():
    data = np.array([12, 15, 18, 20, 25, 30])

    print("Sum:", np.sum(data))
    print("Mean:", np.mean(data))
    print("Median:", np.median(data))
    print("Minimum:", np.min(data))
    print("Maximum:", np.max(data))
    print("Standard deviation:", np.std(data))
    print("Variance:", np.var(data))

    # Default std() and var() use population formulas.


# ============================================================
# Example 6 — Two-dimensional arrays
# ============================================================

def example_06():
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    print("Matrix:")
    print(matrix)

    print("Shape:", matrix.shape)
    print("First row:", matrix[0])
    print("Second column:", matrix[:, 1])
    print("Element [1, 2]:", matrix[1, 2])

    print("Row sums:", matrix.sum(axis=1))
    print("Column sums:", matrix.sum(axis=0))
    print("Transpose:")
    print(matrix.T)


# ============================================================
# Example 7 — Reshaping arrays
# ============================================================

def example_07():
    numbers = np.arange(1, 13)

    print("Original:", numbers)

    matrix = numbers.reshape(3, 4)

    print("Reshaped (3 x 4):")
    print(matrix)

    print("Flattened:", matrix.flatten())
    print("Shape:", matrix.shape)

    # reshape() requires the same number of elements.


# ============================================================
# Example 8 — Matrix operations
# ============================================================

def example_08():
    a = np.array([
        [1, 2],
        [3, 4]
    ])

    b = np.array([
        [5, 6],
        [7, 8]
    ])

    print("Element-wise multiplication:")
    print(a * b)

    print("Matrix multiplication:")
    print(a @ b)

    print("Transpose:")
    print(a.T)

    print("Determinant:", np.linalg.det(a))


# ============================================================
# Example 9 — Creating Pandas Series
# ============================================================

def example_09():
    scores = pd.Series(
        [85, 92, 76, 88],
        index=["Anna", "John", "Maria", "Alex"]
    )

    print(scores)

    print("Anna's score:", scores["Anna"])
    print("Mean score:", scores.mean())
    print("Highest score:", scores.max())
    print("Students above 80:")
    print(scores[scores > 80])


# ============================================================
# Example 10 — Creating a DataFrame
# ============================================================

def example_10():
    students = pd.DataFrame({
        "name": ["Anna", "John", "Maria", "Alex"],
        "age": [22, 24, 23, 21],
        "score": [85, 92, 76, 88]
    })

    print(students)

    print("Shape:", students.shape)
    print("Columns:", students.columns.tolist())
    print("Data types:")
    print(students.dtypes)

    print("First two rows:")
    print(students.head(2))

    print("Summary:")
    print(students.describe())


# ============================================================
# Example 11 — Selecting rows and columns
# ============================================================

def example_11():
    df = pd.DataFrame({
        "name": ["Anna", "John", "Maria", "Alex"],
        "age": [22, 24, 23, 21],
        "score": [85, 92, 76, 88]
    })

    print("Names:")
    print(df["name"])

    print("Multiple columns:")
    print(df[["name", "score"]])

    print("First row with iloc:")
    print(df.iloc[0])

    print("First two rows:")
    print(df.iloc[:2])

    print("Specific value with loc:")
    print(df.loc[1, "score"])


# ============================================================
# Example 12 — Filtering DataFrames
# ============================================================

def example_12():
    df = pd.DataFrame({
        "name": ["Anna", "John", "Maria", "Alex", "Sara"],
        "age": [22, 24, 23, 21, 25],
        "score": [85, 92, 76, 88, 55]
    })

    print("Students with scores >= 80:")
    print(df[df["score"] >= 80])

    print("Students older than 22:")
    print(df[df["age"] > 22])

    print("Older than 22 AND score >= 80:")
    print(
        df[
            (df["age"] > 22) &
            (df["score"] >= 80)
        ]
    )

    print("Selected names:")
    print(df.loc[df["score"] >= 80, "name"])


# ============================================================
# Example 13 — Adding and modifying columns
# ============================================================

def example_13():
    df = pd.DataFrame({
        "name": ["Anna", "John", "Maria", "Alex"],
        "math": [80, 90, 70, 85],
        "python": [90, 95, 85, 80]
    })

    df["average"] = (df["math"] + df["python"]) / 2

    df["passed"] = df["average"] >= 80

    print("With calculated columns:")
    print(df)

    df.loc[df["name"] == "Maria", "python"] = 95

    df["average"] = (df["math"] + df["python"]) / 2
    df["passed"] = df["average"] >= 80

    print("After updating Maria's score:")
    print(df)


# ============================================================
# Example 14 — Missing values
# ============================================================

def example_14():
    df = pd.DataFrame({
        "name": ["Anna", "John", "Maria", "Alex"],
        "score": [85, np.nan, 76, np.nan]
    })

    print("Original DataFrame:")
    print(df)

    print("Missing values:")
    print(df.isna())

    print("Missing count:")
    print(df.isna().sum())

    mean_score = df["score"].mean()

    filled = df.fillna({"score": mean_score})

    print("Missing scores replaced with mean:")
    print(filled)

    print("Rows without missing values:")
    print(df.dropna())


# ============================================================
# Example 15 — Sorting and grouping data
# ============================================================

def example_15():
    df = pd.DataFrame({
        "name": ["Anna", "John", "Maria", "Alex", "Sara"],
        "group": ["A", "B", "A", "B", "A"],
        "score": [85, 92, 76, 88, 95]
    })

    print("Sorted by score:")
    print(df.sort_values("score", ascending=False))

    print("Mean score by group:")
    print(df.groupby("group")["score"].mean())

    print("Count by group:")
    print(df.groupby("group")["name"].count())

    print("Maximum score by group:")
    print(df.groupby("group")["score"].max())


# ============================================================
# Run all examples
# ============================================================

if __name__ == "__main__":
    examples = [
        example_01,
        example_02,
        example_03,
        example_04,
        example_05,
        example_06,
        example_07,
        example_08,
        example_09,
        example_10,
        example_11,
        example_12,
        example_13,
        example_14,
        example_15,
    ]

    for index, example in enumerate(examples, start=1):
        print(f"\n{'=' * 55}")
        print(f"EXAMPLE {index:02d}")
        print(f"{'=' * 55}")
        example()

    print("\nNumPy version:", np.__version__)
    print("Pandas version:", pd.__version__)
