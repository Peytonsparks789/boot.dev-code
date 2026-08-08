from src.markdown_processor.splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_links
from src.nodes.textnode import TextType, TextNode, DELIMITERS


def text_to_text_nodes(nodes):
    new_nodes = []

    for node in nodes:
        parsed_nodes = [node]
        for text_type, delimiter in DELIMITERS.items():
            parsed_nodes = split_nodes_delimiter(parsed_nodes, delimiter, text_type)

        parsed_nodes = split_nodes_image(parsed_nodes)
        parsed_nodes = split_nodes_links(parsed_nodes)

        new_nodes.extend(parsed_nodes)

    return new_nodes