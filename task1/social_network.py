from user import User
from graph import Graph

class SocialNetwork:
    """Integrates User and Graph to manage the social network."""

    def __init__(self):
        self._users = {}      # name -> User object
        self._graph = Graph()

    def register_user(self, name):
        if name in self._users:
            print(f"User {name} already exists.")
            return False
        user = User(name)
        self._users[name] = user
        self._graph.add_vertex(name)
        print(f"User {name} registered.")
        return True

    def add_friendship(self, name1, name2):
        if name1 not in self._users or name2 not in self._users:
            print("User does not exist.")
            return False
        self._graph.add_edge(name1, name2)
        # Also update the User objects (optional redundancy)
        self._users[name1].add_friend(name2)
        self._users[name2].add_friend(name1)
        print(f"{name1} and {name2} are now friends.")
        return True

    def shortest_path(self, name1, name2):
        # To be implemented later
        pass

    def recommend_friends(self, name):
        # To be implemented later
        pass
