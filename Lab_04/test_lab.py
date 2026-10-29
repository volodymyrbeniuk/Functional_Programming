import pytest

from lab import (
    BinaryTreeNode,
    fibonacci,
    fibonacci_naive,
    inorder,
    inorder_gen,
    postorder,
    preorder,
    quicksort,
    randomized_select,
    recursive_factorial,
    recursive_filter,
    recursive_map,
    recursive_sum,
    tree_height,
    tree_size,
)


def test_recursive_list_functions_cover_empty_and_nonempty_inputs() -> None:
    assert recursive_sum([]) == 0
    assert recursive_sum([1, 2, 3, 4]) == 10
    assert recursive_map([], lambda value: value * 2) == []
    assert recursive_map([1, 2, 3], lambda value: value * 2) == [2, 4, 6]
    assert recursive_filter([1, 2, 3, 4], lambda value: value % 2 == 0) == [2, 4]
    assert recursive_filter([], lambda value: value > 0) == []


def test_recursive_factorial_and_invalid_input() -> None:
    assert recursive_factorial(0) == 1
    assert recursive_factorial(5) == 120
    with pytest.raises(ValueError, match="non-negative"):
        recursive_factorial(-1)


def test_quicksort_sorts_without_mutating_and_handles_duplicates() -> None:
    values = [4, 2, 4, 1, 0, 2]
    original = values.copy()
    assert quicksort(values) == [0, 1, 2, 2, 4, 4]
    assert values == original
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    assert quicksort([3, 3, 3]) == [3, 3, 3]


def test_randomized_select_is_one_based_and_does_not_mutate_input() -> None:
    values = [4, 2, 4, 1]
    original = values.copy()
    assert randomized_select(values, 1) == 1
    assert randomized_select(values, 3) == 4
    assert randomized_select(values, 4) == 4
    assert values == original
    with pytest.raises(ValueError):
        randomized_select(values, 0)
    with pytest.raises(ValueError):
        randomized_select(values, 5)


def test_tree_traversals_and_metrics() -> None:
    tree = BinaryTreeNode(
        4,
        BinaryTreeNode(2, BinaryTreeNode(1), BinaryTreeNode(3)),
        BinaryTreeNode(6, BinaryTreeNode(5), BinaryTreeNode(7)),
    )
    assert inorder(tree) == [1, 2, 3, 4, 5, 6, 7]
    assert preorder(tree) == [4, 2, 1, 3, 6, 5, 7]
    assert postorder(tree) == [1, 3, 2, 5, 7, 6, 4]
    assert list(inorder_gen(tree)) == inorder(tree)
    assert tree_size(tree) == 7
    assert tree_height(tree) == 3
    assert inorder(None) == []
    assert tree_size(None) == 0
    assert tree_height(None) == 0


def test_memoized_fibonacci_matches_recursive_reference_and_uses_cache() -> None:
    fibonacci.cache_clear()
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55
    assert fibonacci(30) == fibonacci_naive(30) == 832040
    before = fibonacci.cache_info().hits
    assert fibonacci(30) == 832040
    assert fibonacci.cache_info().hits > before
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci(-1)


def test_naive_fibonacci_rejects_negative_input() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        fibonacci_naive(-1)
