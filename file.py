import os

def print_file_tree(root_dir, indent=""):
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isdir(item_path):
            print(f"{indent}📁 {item}")
            print_file_tree(item_path, indent + "  ")
        else:
            print(f"{indent}📄 {item}")

if __name__ == "__main__":
    print_file_tree(".", indent="----")
