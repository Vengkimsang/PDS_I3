# ---------------------------------------------------------------------------
# Problem 8 (Medium) · *args, **kwargs and lambda
# ---------------------------------------------------------------------------
def describe(*numbers, decimals=2, label="Data"):
    """Return (count, min, max, mean) of any number of values and print them."""
    if len(numbers) == 0:
        print(f"{label}: no values")
        return None
    mean = round(sum(numbers) / len(numbers), decimals)
    print(f"{label}: n={len(numbers)} min={min(numbers)} max={max(numbers)} mean={mean}")
    return len(numbers), min(numbers), max(numbers), mean

def make_tag(text, **style):
    """Wrap text in an HTML-like tag built from keyword arguments."""
    attrs = ""
    for key, value in style.items():
        attrs += f' {key}="{value}"'
    return f"<span{attrs}>{text}</span>"

print()
describe(12, 7, 30, 4)
describe(3.14159, 2.71828, decimals=3, label="Constants")
describe()
print(make_tag("Hello", color="red", size=14))

square = lambda x: x ** 2
is_adult = lambda age: age >= 18
print(square(9), is_adult(17), is_adult(21))

