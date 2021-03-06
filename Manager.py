import Project.Tree
import Project.Node


def main2():
    try:
        nfile = input("Please enter a file name: ")
        tree = Project.Tree.Tree()
        tree.read_tree(tree, nfile)
        pointer = tree.root.children[0]
    except FileNotFoundError:
        print("File not found.")
        main2()
    print(pointer.option + "\n")
    message_option(pointer)
    stop = input("Do you want to input a new file? (yes or no) \n")
    if stop == "yes" or stop == "Yes":
        main2()
    elif stop == "no" or stop == "No":
        exit()
    else:
        print("\n" + "Unclear answer, program terminating.")
        exit()


def message_option(pointer):
    while pointer is not None:
        if pointer.print_child_options() > 0:
            print(pointer.message)
            option = input("1) " + pointer.children[0].option + " 2) " + pointer.children[1].option + "\n")
            try:
                pointer = pointer.child(option)
            except ValueError:
                print("\n That is not a valid option")

        else:
            print(pointer.message)
            pointer = None


main2()