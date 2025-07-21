from typing import List, Dict
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.name = ""
        self.deleted = False

def insert(root: TrieNode, path: List[str]):
    node = root
    for folder in path:
        if folder not in node.children:
            node.children[folder] = TrieNode()
            node.children[folder].name = folder
        node = node.children[folder]

def serialize(node: TrieNode, counter: Dict[str, int], lookup: Dict[str, List[TrieNode]]) -> str:
    if not node.children:
        return ""
    serials = []
    for child in sorted(node.children):
        serials.append(child + "(" + serialize(node.children[child], counter, lookup) + ")")
    serial = "".join(serials)
    counter[serial] += 1
    lookup[serial].append(node)
    return serial

def mark_deleted(counter: Dict[str, int], lookup: Dict[str, List[TrieNode]]):
    for serial, count in counter.items():
        if count > 1:
            for node in lookup[serial]:
                node.deleted = True

def collect(node: TrieNode, path: List[str], res: List[List[str]]):
    for child in node.children.values():
        if not child.deleted:
            res.append(path + [child.name])
            collect(child, path + [child.name], res)

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()
        for path in paths:
            insert(root, path)
        counter = defaultdict(int)
        lookup = defaultdict(list)
        serialize(root, counter, lookup)
        mark_deleted(counter, lookup)
        res = []
        collect(root, [], res)
        return res