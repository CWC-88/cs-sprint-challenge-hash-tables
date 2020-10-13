# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    table = {}

    for path in files:
        parts = path.split("/")

        if table.get(parts[-1]):
            table[parts[-1]].append(path)
        else:
            table[parts[-1]] = [path]

            result = []

    for value in queries:
        if table.get(value):
            result.extend(table.get(value))

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
