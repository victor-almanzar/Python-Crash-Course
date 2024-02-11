# Truth Tables

Below are truth tables for the comparison operator ==, and each of the logic operators and, or, and not.

## `==` Truth Table

```markdown
| x     | ==  | y     | Returns |
|-------|-----|-------|---------|
| True  | ==  | True  | True    |
| True  | ==  | False | False   |
| False | ==  | True  | False   |
| False | ==  | False | True    |
```

## AND Truth Table

```markdown
| x     | and | y     | Returns |
|-------|-----|-------|---------|
| True  | and | True  | True    |
| True  | and | False | False   |
| False | and | True  | False   |
| False | and | False | False   |
```

## OR Truth Table

```markdown
| x    | or  | y     | Returns |
|------|-----|-------|---------|
| True | or  | True  | True    |
| True | or  | False | True    |
| False| or  | True  | True    |
| False| or  | False | False   |
```

## NOT Truth Table

```markdown
| not   | x     | Returns |
|-------|-------|---------|
| not   | True  | False   |
| not   | False | True    |
```

These tables are helpful for understanding how logical operators work in Python and are fundamental in constructing conditions and algorithms.
