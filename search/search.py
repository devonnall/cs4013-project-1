# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# Depth-First Search (DFS) implementation
def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first using a stack."""
    # Create a stack to store nodes that need to be explored
    stack = util.Stack()
    # Set to keep track of visited nodes to avoid cycles
    visited = set()
    # Push the start state with an empty path into the stack
    stack.push((problem.getStartState(), []))  # (state, path)
    
    # Continue searching until there are no nodes left in the stack
    while not stack.isEmpty():
        # Pop the most recently added node from the stack
        state, path = stack.pop()
        
        # Check if the current state is the goal state
        if problem.isGoalState(state):
            return path  # Return the sequence of actions to reach the goal
        
        # If the state has not been visited yet, process it
        if state not in visited:
            visited.add(state)  # Mark the state as visited
            # Retrieve successors of the current state
            for successor, action, _ in problem.getSuccessors(state):
                # Push each successor to the stack with the updated path
                stack.push((successor, path + [action]))
    
    return []

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()  # Create a queue for storing nodes
    visited = set()  # Set to track visited nodes
    queue.push((problem.getStartState(), []))  # Push the start state with an empty path
    
    while not queue.isEmpty():
        state, path = queue.pop()  # Dequeue the oldest node
        
        if problem.isGoalState(state):
            return path  # Return the sequence of actions to reach the goal
        
        if state not in visited:
            visited.add(state)
            for successor, action, _ in problem.getSuccessors(state):
                queue.push((successor, path + [action]))
    
    return []

# def breadthFirstSearch(problem: SearchProblem):
#     """Search the shallowest nodes in the search tree first."""
#     # Initialize the queue with the starting state and an empty action list
#     startState = problem.getStartState()
#     frontier = util.Queue()
#     frontier.push((startState, []))  # (state, actions)

#     # Track visited states to avoid revisiting them
#     visited = set()
#     visited.add(startState)

#     while not frontier.isEmpty():
#         # Get the next node from the queue
#         currentState, actions = frontier.pop()

#         # Check if the current state is the goal
#         if problem.isGoalState(currentState):
#             return actions

#         # Generate successors
#         for successor, action, _ in problem.getSuccessors(currentState):
#             if successor not in visited:
#                 # Mark the successor as visited
#                 visited.add(successor)
#                 # Add the successor to the queue with the updated action list
#                 frontier.push((successor, actions + [action]))

#     # If no solution is found, return an empty list
#     return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()  # Create a priority queue for storing nodes
    visited = set()  # Set to track visited nodes
    pq.push((problem.getStartState(), [], 0), 0)  # Push the start state with cost 0
    
    while not pq.isEmpty():
        state, path, cost = pq.pop()  # Pop the node with the lowest cost
        
        if problem.isGoalState(state):
            return path  # Return the sequence of actions to reach the goal
        
        if state not in visited:
            visited.add(state)
            for successor, action, step_cost in problem.getSuccessors(state):
                new_cost = cost + step_cost  # Compute total cost
                pq.push((successor, path + [action], new_cost), new_cost)
    
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()  # Create a priority queue for storing nodes
    visited = set()  # Set to track visited nodes
    pq.push((problem.getStartState(), [], 0), 0)  # Push the start state with cost 0
    
    while not pq.isEmpty():
        state, path, cost = pq.pop()  # Pop the node with the lowest combined cost and heuristic
        
        if problem.isGoalState(state):
            return path  # Return the sequence of actions to reach the goal
        
        if state not in visited:
            visited.add(state)
            for successor, action, step_cost in problem.getSuccessors(state):
                new_cost = cost + step_cost  # Compute total cost
                priority = new_cost + heuristic(successor, problem)  # Compute A* priority
                pq.push((successor, path + [action], new_cost), priority)
    
    return []

# def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
#     """Search the node that has the lowest combined cost and heuristic first."""
#     # Initialize the priority queue with the starting state
#     startState = problem.getStartState()
#     frontier = util.PriorityQueue()
#     frontier.push((startState, [], 0), 0)  # (state, actions, cost), priority

#     # Track visited states and their costs
#     visited = {}
#     visited[startState] = 0

#     while not frontier.isEmpty():
#         # Get the node with the lowest priority (cost + heuristic)
#         currentState, actions, currentCost = frontier.pop()

#         # Check if the current state is the goal
#         if problem.isGoalState(currentState):
#             return actions

#         # Generate successors
#         for successor, action, stepCost in problem.getSuccessors(currentState):
#             newCost = currentCost + stepCost
#             heuristicCost = heuristic(successor, problem)
#             totalCost = newCost + heuristicCost

#             # If the successor hasn't been visited or a better path is found
#             if successor not in visited or newCost < visited[successor]:
#                 visited[successor] = newCost
#                 frontier.push((successor, actions + [action], newCost), totalCost)

#     # If no solution is found
#     return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
