from src.nodes.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.PLAINTEXT:
            nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Delimiter {delimiter} not closed properly")
        new_nodes = node.text.split(delimiter)

        for idx, new_node in enumerate(new_nodes):
            if idx % 2 != 0:
                nodes.append(TextNode(text=new_node, text_type=text_type))
            else:
                nodes.append(TextNode(text=new_node, text_type=TextType.PLAINTEXT))

    return nodes