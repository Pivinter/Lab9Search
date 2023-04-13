import unittest
from Lab9Reserch import *



class TestTreeNode(unittest.TestCase):

    def setUp(self):
        self.tree = TreeNode(50)
        self.tree.left = TreeNode(30)
        self.tree.right = TreeNode(70)
        self.tree.left.left = TreeNode(20)
        self.tree.left.right = TreeNode(40)
        self.tree.right.left = TreeNode(60)
        self.tree.right.right = TreeNode(80)

    def test_insert_node(self):
        tree = None
        tree = insert_node(tree, 50)
        self.assertEqual(tree.value, 50)
        tree = insert_node(tree, 30)
        self.assertEqual(tree.left.value, 30)
        tree = insert_node(tree, 70)
        self.assertEqual(tree.right.value, 70)

    def test_count_leaf_nodes(self):
        self.assertEqual(count_leaf_nodes(self.tree), 4)

    def test_remove_node_with_no_children(self):
        tree = remove_node_with_no_children(self.tree, 20)
        self.assertIsNone(tree.left.left)

    def test_find_nodes_without_children(self):
        self.assertEqual(find_nodes_without_children(self.tree), [20, 40, 60, 80])


    def test_remove_node_with_two_children(self):
        tree = remove_node_with_two_children(self.tree, 50)
        self.assertEqual(tree.value, 60)


    def test_tree_to_dict_and_dict_to_tree(self):
        tree_dict = tree_to_dict(self.tree)
        new_tree = dict_to_tree(tree_dict)
        self.assertEqual(find_all_nodes(self.tree), find_all_nodes(new_tree))

    def test_height(self):
        self.assertEqual(height(self.tree), 3)


    def test_balance_tree(self):
        balanced_tree = balance_tree(self.tree)
        self.assertTrue(is_balanced(balanced_tree))

if __name__ == '__main__':
    unittest.main()
