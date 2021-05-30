from django.db import models
import numpy as np
from typing import List
import random

class TDMNode:
    def __init__(self, id, depth = 1, parent = None, children = None, embedding = None) -> None:
        self.id: int = id
        self.parent: TDMNode = parent or None
        self.children: List[TDMNode] = children or []
        self.embedding: np.array = embedding if embedding is not None else np.random.randn(32)
        self._depth: int = depth
        self._temp_children_id = None
        self._temp_parent_id = None

    def __str__(self) -> str:
        return f"{self.id}\t{self.parse_parent()}\t{self.parse_children()}\t{self.parse_embedding()}"

    @property
    def depth(self):
        return self._depth

    def parse_parent(self) -> int:
        if self.parent is None:
            return 0
        return self.parent.id

    def parse_children(self) -> str:
        return ','.join([str(x.id) for x in self.children])

    def parse_embedding(self) -> str:
        return ','.join(['%.5f'%x for x in self.embedding])

    @classmethod
    def load(cls, line: str):
        [id, parent_id, children_id, embedding] = line.split('\t')
        id = int(id)
        parent_id = int(parent_id)
        children_id = [int(x) for x in children_id.split(',')] if children_id else []
        embedding = np.array([float(x) for x in embedding.split(',')])
        ret = TDMNode(id, 0, None, None, embedding)
        ret._temp_children_id = children_id
        ret._temp_parent_id = parent_id
        return ret

    def clear(self):
        del self._temp_children_id
        del self._temp_parent_id

class TDMTree:
    _root: TDMNode = None
    _node_num: int = 0

    @property
    def node_num(self):
        return self._node_num

    def dump(self, path) -> None:
        with open(path, 'w') as file:
            queue = []
            if self._root:
                queue.append(self._root)
            while len(queue):
                node = queue.pop(0)
                print(str(node), file=file)
                queue.extend(node.children)

        print('* Dump tree to', path)

    def refresh_depth(self):
        if not self._root:
            return

        self._root._depth = 1
        st = [self._root]
        while len(st):
            node = st.pop()
            for child in node.children:
                child._depth = node._depth + 1
                st.append(child)

    def get_limited_nodes(self, max_n_children, max_depth):
        if not self._root or max_depth <= 0:
            return []

        ret = [self._root]
        st = [self._root]

        while len(st):
            node = st.pop()
            if node.depth >= max_depth:
                continue

            sampled_children = random.sample(node.children, min(len(node.children), max_n_children))
            ret.extend(sampled_children)
            st.extend(sampled_children)

        return ret

    @classmethod
    def generateRandom(cls, depth = 5, n_children = (2, 2, 3, 3, 0)):
        assert depth == len(n_children) and n_children[-1] == 0, str(n_children)

        cur_id = 1
        queue: List[TDMNode] = []
        tree = TDMTree()
        tree._root = TDMNode(cur_id, 1)

        cur_id += 1
        queue.append(tree._root)

        while len(queue):
            node = queue.pop(0)
            dep = node._depth
            for _ in range(n_children[dep - 1]):
                child = TDMNode(cur_id, dep + 1, node)
                node.children.append(child)
                queue.append(child)
                cur_id += 1

        tree._node_num = cur_id
        return tree

    @classmethod
    def load(cls, path):
        tree = TDMTree()
        node_map = {}

        with open(path, 'r') as file:
            for line in file:
                line = line.strip()
                node = TDMNode.load(line)
                if node.id == 1:
                    tree._root = node
                if node.id in node_map:
                    raise Exception('Duplicate node %d'%node.id)
                node_map[node.id] = node
                tree._node_num += 1

        for nid in node_map.keys():
            node = node_map[nid]
            if node._temp_parent_id:
                node.parent = node_map[node._temp_parent_id]
            for child_id in node._temp_children_id:
                node.children.append(node_map[child_id])

            node.clear()

        del node_map
        tree.refresh_depth()

        return tree
