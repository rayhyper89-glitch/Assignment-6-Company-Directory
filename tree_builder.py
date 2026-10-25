class EmployeeNode:
    """Represents one employee in the company directory."""

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    """Manages the company's employee reporting structure."""

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # Start searching from the root when no node is provided.
        if current_node is None:
            current_node = self.root

        if current_node is None:
            print("Error: The team tree is empty. Add a team lead first.")
            return False

        side = side.lower().strip()

        if side not in ("left", "right"):
            print("Error: Side must be 'left' or 'right'.")
            return False

        # Check whether the current node is the requested manager.
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is not None:
                    print(f"Error: The LEFT side of {manager_name} is occupied.")
                    return False

                current_node.left = EmployeeNode(employee_name)

            else:
                if current_node.right is not None:
                    print(f"Error: The RIGHT side of {manager_name} is occupied.")
                    return False

                current_node.right = EmployeeNode(employee_name)

            return True

        # Search the left subtree recursively.
        if current_node.left is not None:
            if self.insert(
                manager_name, employee_name, side, current_node.left
            ):
                return True

        # Search the right subtree recursively.
        if current_node.right is not None:
            if self.insert(
                manager_name, employee_name, side, current_node.right
            ):
                return True

        # Report a missing manager after searching the tree.
        if current_node == self.root:
            print(f"Error: Manager '{manager_name}' was not found.")

        return False

    def print_tree(self, node=None, level=0):
        # Use the root for the initial call.
        if node is None and level == 0:
            node = self.root

        # Stop when a leaf's child is reached.
        if node is None:
            return

        # Print the employee and show the reporting hierarchy.
        print("    " * level + "- " + node.name)

        # Recursively print the left and right subtrees.
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


def company_directory():
    company = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")

        choice = input("Choose an option (1–4): ").strip()

        if choice == "1":
            if company.root is not None:
                print("Error: A team lead already exists.")
                continue

            name = input("Enter team lead's name: ").strip()

            if name:
                company.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")
            else:
                print("Error: Name cannot be empty.")

        elif choice == "2":
            if company.root is None:
                print("Error: Add a team lead first.")
                continue

            manager = input("Enter the manager's name: ").strip()
            employee = input("Enter the new employee's name: ").strip()
            side = input(
                "Should this employee be on the LEFT or RIGHT of the manager? "
            ).strip().lower()

            if not manager or not employee:
                print("Error: Manager and employee names cannot be empty.")
                continue

            success = company.insert(manager, employee, side)

            if success:
                print(
                    f"✅ {employee} added to the "
                    f"{side.upper()} of {manager}."
                )

        elif choice == "3":
            if company.root is None:
                print("The company directory is empty.")
            else:
                print("\n🌳 Current Team Structure:")
                company.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("Invalid choice. Please select an option from 1 to 4.")


# Run the program.
if __name__ == "__main__":
    company_directory()
