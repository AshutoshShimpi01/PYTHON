

Q. No.,Input String,Desired Output,Basic Python Method/Function
1,data science,DATA SCIENCE,.upper()
2,PYTHON,python,.lower()
3,hello world,hello world,.strip()
4,"apple,banana,cherry","['apple', 'banana', 'cherry']",".split(',')"
5,learning python,learning,str[:index] (Slicing)
6,coding,g,str[-1] (Negative Indexing)
7,programming,m,str[index] (Positive Indexing)
8,ashutosh,Ashutosh,.capitalize()
9,a b c (list of strings),a-b-c,'-'.join(list)
10,hello,5,len()



Certainly\! Here are 10 basic questions on Python strings, designed to be similar to your previous request, along with the expected output and the function/method to use.

## Basic Python String Questions

| Q. No. | Input String | Desired Output | Basic Python Method/Function |
| :----: | :---------------------------------- | :----------------------------- | :----------------------------- |
| 1 | `data science` | `DATA SCIENCE` | `.upper()` |
| 2 | `PYTHON` | `python` | `.lower()` |
| 3 | `hello world` | `hello world` | `.strip()` |
| 4 | `apple,banana,cherry` | `['apple', 'banana', 'cherry']` | `.split(',')` |
| 5 | `learning python` | `learning` | `str[:index]` (Slicing) |
| 6 | `coding` | `g` | `str[-1]` (Negative Indexing) |
| 7 | `programming` | `m` | `str[index]` (Positive Indexing) |
| 8 | `ashutosh` | `Ashutosh` | `.capitalize()` |
| 9 | `a b c` (list of strings) | `a-b-c` | `'-'.join(list)` |
| 10 | `hello` | `5` | `len()` |

-----

## Example Solutions

Here's how you would write the Python code for a few of these questions:

### Q. 1: Uppercasing

```python
input_string = "data science"
output = input_string.upper()
print(output)
# Output: DATA SCIENCE
```

### Q. 4: Splitting

```python
input_string = "apple,banana,cherry"
output = input_string.split(',')
print(output)
# Output: ['apple', 'banana', 'cherry']
```

### Q. 9: Joining

```python
input_list = ['a', 'b', 'c']
output = '-'.join(input_list)
print(output)
# Output: a-b-c
```
