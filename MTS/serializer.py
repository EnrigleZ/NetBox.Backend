from .models import TDMNode, TDMTree

def parse_embedding(embedding_str):
    return [float(x) for x in embedding_str.split(',')]

def serialize_TDMNode(node: TDMNode):
    return {
        'id': node.id,
        'name': str(node.id),
        'parent': node.parse_parent(),
        'depth': node.depth,
        'num_children': len(node.children),
        'embedding': parse_embedding(node.parse_embedding()),
    }

def serialize_TDMTree_index(tree: TDMTree, max_n_children = 5, max_depth = 3):
    nodes = tree.get_limited_nodes(max_n_children, max_depth)
    return [serialize_TDMNode(node) for node in nodes]
