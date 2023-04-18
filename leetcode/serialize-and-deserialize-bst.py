#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.serialize-and-deserialize-bst
# Date: 2023/04/18
# Filename: serialize-and-deserialize-bst

__author__ = "Yoshi Truong"
__date__ = "2023/04/18"

from leetcode.datastructure import TreeNode


# https://leetcode.com/problems/serialize-and-deserialize-bst/
class Codec:
    """https://leetcode.com/problems/serialize-and-deserialize-binary-tree/"""

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        arr = [str(root.val)]
        nodes = [root]
        idx = 0
        while idx < len(nodes):
            if nodes[idx].left:
                nodes.append(nodes[idx].left)
                arr.append(str(nodes[idx].left.val))
            else:
                arr.append('null')
            if nodes[idx].right:
                nodes.append(nodes[idx].right)
                arr.append(str(nodes[idx].right.val))
            else:
                arr.append('null')
            idx += 1
        return ','.join(arr)

    def deserialize(self, s):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not s:
            return None
        elements = [int(x) if x != 'null' else None for x in s.split(',')]
        root = TreeNode(elements[0])
        nodes = [root]
        idx = 0
        for i in range(1, len(elements), 2):
            lval = elements[i]
            rval = elements[i + 1] if i + 1 < len(elements) else None
            if lval is not None:
                nodes[idx].left = TreeNode(lval)
                nodes.append(nodes[idx].left)
            if rval is not None:
                nodes[idx].right = TreeNode(rval)
                nodes.append(nodes[idx].right)
            idx += 1
        return root