"""Recursive algorithms, immutable binary trees, and memoization."""

from __future__ import annotations

from collections.abc import Callable, Iterator, Sequence
from dataclasses import dataclass
from functools import lru_cache
from random import Random
from typing import Any, Protocol, TypeVar


class SupportsOrdering(Protocol):
    """A value that supports the ordering operations used by quicksort."""

    def __lt__(self, other: Any, /) -> bool: ...

    def __eq__(self, other: object, /) -> bool: ...

    def __gt__(self, other: Any, /) -> bool: ...


T = TypeVar("T", bound=SupportsOrdering)
U = TypeVar("U")


@dataclass(frozen=True)
class BinaryTreeNode:
    """An immutable integer-valued binary tree node."""

    value: int
    left: BinaryTreeNode | None = None
    right: BinaryTreeNode | None = None


def recursive_sum(values: Sequence[int]) -> int:
    """Sum a sequence by structural recursion without changing it."""
    return 0 if not values else values[0] + recursive_sum(values[1:])


def recursive_map(values: Sequence[T], function: Callable[[T], U]) -> list[U]:
    """Apply a function to every item using recursive list structure."""
    if not values:
        return []
    return [function(values[0]), *recursive_map(values[1:], function)]


def recursive_filter(values: Sequence[T], predicate: Callable[[T], bool]) -> list[T]:
    """Keep matching items using recursive list structure."""
    if not values:
        return []
    head, *tail = values
    filtered_tail = recursive_filter(tail, predicate)
    return [head, *filtered_tail] if predicate(head) else filtered_tail


def recursive_factorial(n: int) -> int:
    """Return n! recursively; reject negative integers."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return 1 if n < 2 else n * recursive_factorial(n - 1)


def quicksort(values: Sequence[T]) -> list[T]:
    """Return a sorted copy using recursive three-way quicksort."""
    if len(values) < 2:
        return list(values)

    pivot = values[len(values) // 2]
    lower = [value for value in values if value < pivot]
    equal = [value for value in values if value == pivot]
    upper = [value for value in values if value > pivot]
    return [*quicksort(lower), *equal, *quicksort(upper)]


def randomized_select(values: Sequence[T], rank: int, seed: int = 0) -> T:
    """Return the 1-based rank statistic without modifying the input."""
    if not 1 <= rank <= len(values):
        raise ValueError("rank is outside the sequence")

    rng = Random(seed)
    work = list(values)
    target = rank - 1
    low, high = 0, len(work) - 1

    while low <= high:
        pivot = work[rng.randint(low, high)]
        left, right, index = low, high, low
        while index <= right:
            if work[index] < pivot:
                work[left], work[index] = work[index], work[left]
                left += 1
                index += 1
            elif work[index] > pivot:
                work[index], work[right] = work[right], work[index]
                right -= 1
            else:
                index += 1

        if target < left:
            high = left - 1
        elif target > right:
            low = right + 1
        else:
            return pivot

    raise RuntimeError("unreachable")


def inorder_gen(tree: BinaryTreeNode | None) -> Iterator[int]:
    """Yield a tree's values in left-root-right order."""
    if tree is not None:
        yield from inorder_gen(tree.left)
        yield tree.value
        yield from inorder_gen(tree.right)


def preorder_gen(tree: BinaryTreeNode | None) -> Iterator[int]:
    """Yield a tree's values in root-left-right order."""
    if tree is not None:
        yield tree.value
        yield from preorder_gen(tree.left)
        yield from preorder_gen(tree.right)


def postorder_gen(tree: BinaryTreeNode | None) -> Iterator[int]:
    """Yield a tree's values in left-right-root order."""
    if tree is not None:
        yield from postorder_gen(tree.left)
        yield from postorder_gen(tree.right)
        yield tree.value


def inorder(tree: BinaryTreeNode | None) -> list[int]:
    """Return the in-order traversal as a list."""
    return list(inorder_gen(tree))


def preorder(tree: BinaryTreeNode | None) -> list[int]:
    """Return the pre-order traversal as a list."""
    return list(preorder_gen(tree))


def postorder(tree: BinaryTreeNode | None) -> list[int]:
    """Return the post-order traversal as a list."""
    return list(postorder_gen(tree))


def tree_size(tree: BinaryTreeNode | None) -> int:
    """Count the nodes recursively."""
    if tree is None:
        return 0
    return 1 + tree_size(tree.left) + tree_size(tree.right)


def tree_height(tree: BinaryTreeNode | None) -> int:
    """Return the number of nodes on the longest root-to-leaf path."""
    if tree is None:
        return 0
    return 1 + max(tree_height(tree.left), tree_height(tree.right))


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """Return Fibonacci(n) with recursive memoization; reject negative n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_naive(n: int) -> int:
    """Uncached Fibonacci for small-input comparison in the demonstration."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return n if n < 2 else fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def main() -> None:
    values = [7, 2, 9, 2, 1]
    tree = BinaryTreeNode(
        4,
        BinaryTreeNode(2, BinaryTreeNode(1), BinaryTreeNode(3)),
        BinaryTreeNode(6, BinaryTreeNode(5), BinaryTreeNode(7)),
    )
    print("Quicksort:", quicksort(values))
    print("Input unchanged:", values)
    print("In-order:", inorder(tree))
    print("Pre-order:", preorder(tree))
    print("Post-order:", postorder(tree))
    print("Tree size and height:", tree_size(tree), tree_height(tree))
    print("Fibonacci(30):", fibonacci(30))
    print("Memoization cache:", fibonacci.cache_info())


if __name__ == "__main__":
    main()
