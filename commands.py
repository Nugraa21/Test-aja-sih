def tree(d, pad=""):
    for k, v in d.items():
        print(pad + "├──", k)
        if isinstance(v, dict):
            tree(v, pad + "│   ")
