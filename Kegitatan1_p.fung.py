# Fungsi untuk penjumlahan
def addition(a, b):
    return a + b


# Fungsi untuk pengurangan
def subtraction(a, b):
    return a - b


# Fungsi untuk perkalian
def multiplication(a, b):
    return a * b


# Fungsi untuk pembagian
def division(a, b):
    if b == 0:
        return "Pembagian oleh nol tidak diperbolehkan"
    return a / b


# Fungsi untuk mengevaluasi pohon ekspresi
def tree(expression):
    if isinstance(expression, tuple):
        left = expression[0]
        operator = expression[1]
        right = expression[2]

        if operator == '+':
            return addition(tree(left), tree(right))
        elif operator == '-':
            return subtraction(tree(left), tree(right))
        elif operator == '*':
            return multiplication(tree(left), tree(right))
        elif operator == '/':
            if tree(right) == 0:
                return "Pembagian oleh nol tidak diperbolehkan"
            return division(tree(left), tree(right))
    else:
        return expression


# Pohon ekspresi
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi
result = tree(expression_tree)

# Tampilkan hasil evaluasi
print("Hasil evaluasi pohon ekspresi:", result)
