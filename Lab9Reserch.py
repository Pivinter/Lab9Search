class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert_node(root.left, value)
        else:
            root.right = insert_node(root.right, value)
    return root

def print_tree(root, prefix=""):
    if root is None:
        return
    print_tree(root.left, prefix + "--")
    print(prefix + str(root.value))
    print_tree(root.right, prefix + "--")

def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

def remove_node_with_no_children(root, value):
    if root is None:
        return root
    
    if value < root.value:
        root.left = remove_node_with_no_children(root.left, value)
    elif value > root.value:
        root.right = remove_node_with_no_children(root.right, value)
    else:
        if root.left is None and root.right is None:
            root = None
    return root

def find_nodes_without_children(root, nodes=None):
    if nodes is None:
        nodes = []

    if root is None:
        return nodes

    if root.left is None and root.right is None:
        nodes.append(root.value)

    find_nodes_without_children(root.left, nodes)
    find_nodes_without_children(root.right, nodes)

    return nodes

def remove_node_with_one_child(root, value):
    if root is None:
        return root

    if value < root.value:
        root.left = remove_node_with_one_child(root.left, value)
    elif value > root.value:
        root.right = remove_node_with_one_child(root.right, value)
    else:
        if root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
    return root

def find_nodes_with_one_child(root, nodes=None):
    if nodes is None:
        nodes = []

    if root is None:
        return nodes

    if (root.left is not None and root.right is None) or (root.left is None and root.right is not None):
        nodes.append(root.value)

    find_nodes_with_one_child(root.left, nodes)
    find_nodes_with_one_child(root.right, nodes)

    return nodes

def find_min_value_node(node):
    while node.left is not None:
        node = node.left
    return node

def remove_node_with_two_children(root, value):
    if root is None:
        return root

    if value < root.value:
        root.left = remove_node_with_two_children(root.left, value)
    elif value > root.value:
        root.right = remove_node_with_two_children(root.right, value)
    else:
        if root.left and root.right:
            temp = find_min_value_node(root.right)
            root.value = temp.value
            root.right = remove_node_with_no_children(root.right, temp.value)
    return root

def find_nodes_with_two_children(root, nodes=None):
    if nodes is None:
        nodes = []

    if root is None:
        return nodes

    if root.left is not None and root.right is not None:
        nodes.append(root.value)

    find_nodes_with_two_children(root.left, nodes)
    find_nodes_with_two_children(root.right, nodes)

    return nodes

def remove_branch(root, value):
    if root is None:
        return root

    if value < root.value:
        root.left = remove_branch(root.left, value)
    elif value > root.value:
        root.right = remove_branch(root.right, value)
    else:
        root = None
    return root

def find_all_nodes(root, nodes=None):
    if nodes is None:
        nodes = []

    if root is None:
        return nodes

    nodes.append(root.value)

    find_all_nodes(root.left, nodes)
    find_all_nodes(root.right, nodes)

    return nodes

def tree_to_dict(root):
    if root is None:
        return None
    return {
        'value': root.value,
        'left': tree_to_dict(root.left),
        'right': tree_to_dict(root.right)
    }

def dict_to_tree(tree_dict):
    if tree_dict is None:
        return None
    root = TreeNode(tree_dict['value'])
    root.left = dict_to_tree(tree_dict['left'])
    root.right = dict_to_tree(tree_dict['right'])
    return root

def save_tree_to_file_preorder(root, file):
    if root is None:
        file.write("-1 ")
        return
    file.write(str(root.value) + " ")
    save_tree_to_file_preorder(root.left, file)
    save_tree_to_file_preorder(root.right, file)

def save_tree_to_file(root, filename):
    with open(filename, 'w') as file:
        save_tree_to_file_preorder(root, file)

def load_tree_from_file_preorder(file):
    value = int(next(file))
    if value == -1:
        return None

    root = TreeNode(value)
    root.left = load_tree_from_file_preorder(file)
    root.right = load_tree_from_file_preorder(file)
    return root

def load_tree_from_file(filename):
    with open(filename, 'r') as file:
        return load_tree_from_file_preorder((val for val in file.read().split()),)

def build_tree_predefined(num_nodes):
    import random
    root = None
    elements = [random.randint(1, 100) for _ in range(num_nodes)]
    for value in elements:
        root = insert_node(root, value)
    return root, elements

def add_element(root, value):
    return insert_node(root, value)

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def is_balanced(node):
    if node is None:
        return True
    return abs(height(node.left) - height(node.right)) <= 1 and is_balanced(node.left) and is_balanced(node.right)

def sorted_array_to_bst(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])
    return root

def balance_tree(root):
    nodes = find_all_nodes(root)
    nodes.sort()
    return sorted_array_to_bst(nodes)

print("1. Створити бінарне дерево пошуку")
print("2. Показати бінарне дерево пошуку")
print("3. Показати Кількість елементів без дочірніх вузлів")
print("4. Видалити вузол без дочірніх вузлів")
print("5. Видалити вузол з одним дочірнім вузлом")
print("6. Видалити вузол з двома дочірніми вузлами")
print("7. Видалити гілку дерева")
print("8. Зберегти дерево у файл")
print("9. Завантажити дерево з файлу")
print("10. Добавити новий елемент у бінарне дерево пошуку")
print("11. Збалансувати бінарне дерево пошуку")
print("0. Вихід")
root = None
while True:
            choice = int(input("Введіть номер опції: "))
            if choice == 1:
                num_nodes = int(input("Введіть кількість елементів: "))
                root, elements = build_tree_predefined(num_nodes)
                print(f"Бінарне дерево пошуку створено з наступними елементами: {elements}")
            elif choice == 2:
                print("Бінарне дерево:")
                print_tree(root)
            elif choice == 3:
                count = count_leaf_nodes(root)
                print(f"Кількість елементів без дочірніх вузлів: {count}")
            elif choice == 4:
                nodes_without_children = find_nodes_without_children(root)
                if nodes_without_children:
                    print("Вузли без дочірніх вузлів: ", ", ".join(map(str, nodes_without_children)))
                    value = int(input("Введіть значення вузла, який хочете видалити: "))
                    root = remove_node_with_no_children(root, value)
                    print("Вузол без дочірніх вузлів видалено, якщо він існував.")
                else:
                    print("Немає вузлів без дочірніх елементів для видалення.")
            elif choice == 5:
                nodes_with_one_child = find_nodes_with_one_child(root)
                if nodes_with_one_child:
                    print("Вузли з одним дочірнім вузлом: ", ", ".join(map(str, nodes_with_one_child)))
                    value = int(input("Введіть значення вузла, який хочете видалити: "))
                    root = remove_node_with_one_child(root, value)
                    print("Вузол з одним дочірнім вузлом видалено, якщо він існував.")
                else:
                    print("Немає вузлів з одним дочірнім елементом для видалення.")
            elif choice == 6:
                nodes_with_two_children = find_nodes_with_two_children(root)
                if nodes_with_two_children:
                    print("Вузли з двома дочірніми вузлами: ", ", ".join(map(str, nodes_with_two_children)))
                    value = int(input("Введіть значення вузла, який хочете видалити: "))
                    root = remove_node_with_two_children(root, value)
                    print("Вузол з двома дочірніми вузлами видалено, якщо він існував.")
                else:
                    print("Немає вузлів з двома дочірніми елементами для видалення.")
            elif choice == 7:
                all_nodes = find_all_nodes(root)
                if all_nodes:
                    print("Всі вузли дерева: ", ", ".join(map(str, all_nodes)))
                    value = int(input("Введіть значення вузла, який хочете видалити: "))
                    root = remove_branch(root, value)
                    print("Гілка дерева видалена, якщо вона існувала.")
                else:
                    print("Немає гілок для видалення.")
            elif choice == 8:
                filename = input("Введіть назву файлу: ")
                save_tree_to_file(root, filename)
                print("Дерево збережено у файл.")
            elif choice == 9:
                filename = input("Введіть назву файлу: ")
                root = load_tree_from_file(filename)
                print("Дерево завантажено з файлу.")
            elif choice == 10:
                value = int(input("Введіть значення нового елемента: "))
                root = add_element(root, value)
                print(f"Елемент {value} додано до бінарного дерева пошуку.")
            elif choice == 11:
                root = balance_tree(root)
                print("Бінарне дерево пошуку збалансовано.")
            elif choice == 0:
                break
            else:
                print("Неправильний вибір, спробуйте ще раз.")