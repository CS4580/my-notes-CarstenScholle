"""  Iterator protocols
"""

def main():
    """Driven Function
    """
    iterable = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    # Create an iterator
    iterator = iter(iterable)
    # Get first element
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    # print(next(iterator)) This will throw an error

    # TODO: Add a function with try: catch: to test the iterator

    # TODO: Then, use a Generator

    # Vorteil: Es wird nicht die gesamte data in den mainmemory geladen, sondern immer nur ein teil der daten


if __name__ == '__main__':
    main()