

# Graph Algorithms

1.  **Is a graph with all vertices of even degree always connected? (T/F)**
    *   **F** - A graph can consist of two disconnected components, each with all even-degree vertices.
2.  **Eulerian trail vs Eulerian circuit — list necessary condition(s).**
    *   **Trail:** exactly ==0 or 2 odd-degree vertice==s; **Circuit:** exactly 0 odd-degree vertices (all even).
3.  **Does every DAG-(Directed Acyclic Graph) have a unique topological order? (T/F) **
    *   **F** - If a DAG has multiple source nodes (in-degree 0), the order they appear in can vary.
4.  **If DFS finds a back edge, must the graph be cyclic? (Y/N)**
    *   **Y** - A back edge connects a node to its ancestor in the DFS tree, which by definition forms a cycle.
5.  **For adjacency list vs adjacency matrix: which is better for sparse graphs? (pick)**
    *   **Adjacency list** - Its space complexity is O(V+E), which is far better than the matrix's O(V^2) for sparse graphs.
6.  **Given directed edges, is indegree(outdegree) sum = number of edges? (T/F)**
    *   **T** - Each directed edge contributes exactly one to the total out-degree sum and one to the total in-degree sum.
		- **Sum of indegrees = E.**
		- **Sum of outdegrees = E.**
		- **Sum of both = 2E.**

**Example (topo / Euler / Hamiltonian traps):**

*   **Graph A:** `V={1,2,3,4}`, `E={(1,2),(2,3),(3,1),(3,4)}` — which of: Eulerian trail, Eulerian circuit, Hamiltonian path, topological order exist?
    *   **Eulerian trail** (odd degrees at 3,4), **Hamiltonian path** (e.g., 4-3-1-2); NO circuit or topological order (due to 1-2-3 cycle).
*   **Graph B (DAG with two sources):** `V={a,b,c}`, `E={(a,c),(b,c)}` — how many valid topological orders?
    *   **2** - The two source nodes, 'a' and 'b', can be ordered in any way (`a,b,c` or `b,a,c`).

# Spanning Trees (MST)

1.  **If all edge weights are distinct, is MST unique? (T/F)**
    *   **T** - With distinct weights, the greedy choice made by algorithms like Kruskal's is always unique at every step.
2.  **Kruskal chooses edges in increasing order — can it ever form a cycle? (Y/N)**
    *   **N** - Kruskal's algorithm explicitly checks if adding an edge forms a cycle and ==discards it if it does.==
3.  **Does Prim and Kruskal always produce same total weight? (T/F)**
    *   **T** - All MSTs of a graph have the same minimum total weight, even if the edge sets differ due to ties.
4.  **If an edge is the heaviest on *every* cycle it belongs to, can it be in an MST? (Y/N)**
    *   **N** - The Cycle Property states that the heaviest edge on any cycle cannot be part of any MST.
5.  **Is maximum spanning tree the MST of negated weights? (T/F)**
    *   **T** - Maximizing Σwᵢ is equivalent to minimizing Σ(-wᵢ), and MST algorithms work correctly with negative weights.

**Example (tie / cut traps):**

*   **Graph:** `V={1,2,3,4}`, `E={(1,2,1),(2,3,1),(3,4,2),(4,1,2),(1,3,2)}` — find edges that can differ between MSTs.
    *   Edges **(1,4)** and **(3,4)** - After picking the two weight-1 edges, you must pick one weight-2 edge, creating a tie between these two.

# Shortest Paths

1.  **Can Dijkstra handle negative-weight edges? (Y/N)**
    *   **N** - Its greedy approach can fail because a later path through a negative edge can create a shorter path to an already "finalized" node.
2.  **Does Bellman–Ford always return shortest paths if there is a negative cycle reachable from source? (Y/N)**
    *   **N** - It can detect the cycle and report its existence, but cannot return a finite "shortest path" as it is infinitely small.
3.  **In D==AG shortest-path, is topological order required? (T/F)**==
    *   **T** - Processing vertices in topological order ensures that when we compute dist(v), we have already found the shortest paths to all its predecessors.
4.  **If two shortest paths exist with same length, does predecessor array uniquely identify one? (Y/N)**
    *   **N** - The final predecessor stored depends on which path's final edge was processed last during relaxation.
5.  **Is single-source shortest path on unweighted graph same as BFS? (T/F)**
    *   **T** - BFS explores layer by layer, which is equivalent to finding shortest paths in a graph where every edge has weight 1.

**Example (Dijkstra trap):**

*   `V={s,a,b}`, `E={(s,a,2),(s,b,5),(a,b,-4)}` — run Dijkstra from s — what happens?
    *   **It fails.** It finalizes `a` at dist 2, then incorrectly relaxes `b` to dist -2, missing the correct `s->b` path of 5.

# Max-Flow / Min-Cut

1.  **Is max-flow value = capacity of some s–t cut? (T/F)**
    *   **T** - This is the Max-Flow Min-Cut Theorem, a fundamental result in the field.
2.  **Residual graph: does an augmenting path always increase flow by 1 unit? (Y/N)**
    *   **N** - It increases flow by the path's bottleneck capacity, which can be greater than 1.
3.  **Does reversing augmenting path directions in residual graph reintroduce capacity? (Y/N)**
    *   **Y** - A reverse edge represents the ability to "push back" flow, effectively freeing up capacity on the forward edge.
4.  **Is augmenting along arbitrarily chosen paths guaranteed polynomial time? (Y/N)**
    *   **N** - A poor choice of augmenting paths can lead to exponential time complexity; Edmonds-Karp (using BFS) makes it polynomial.


# Searching Algorithms

1.  **Binary search precondition: array must be sorted. (T/F)**
    *   **T** - The algorithm relies entirely on the sorted property to discard half the search space.
2.  **Off-b==y-one: with `while (low <= high)` mid = `(low+high)/2` — can overflow? (Y/N)**==
    *   ==**Y** - If `low` and `high` are large positive integers, their sum can exceed the maximum== integer value. Use `low + (high-low)/2`.
3.  **Is binary search valid on ==rotated sorted array without modification==? (Y/N)**
    *   **N** - The standard logic fails because the sorted property is broken across the pivot point.
4.  **Linear search complexity best-case = O(1) and worst-case = O(n). (T/F)**
    *   **T** - Best case is finding the element at the first position; worst case is finding it at the last (or not at all).
5.  **In balanced BST search, worst-case height = Θ(log n). (T/F)**
    *   **T** - By definition, a balanced BST maintains a logarithmic height to guarantee efficient operations.

**Example (rotated array trap):**

*   **Array:** `[13,15,17,2,5,9]` — search for 5 using standard binary search — will it find correctly?
    *   **No** - It would check mid `17`, see `5 < 17`, and incorrectly search the left half `[13,15,17]`, missing the target.

# Techniques for Analysis of Algorithms

1.  **Master Theorem: identify which case for `T(n)=aT(n/b)+f(n)`. (Given recurrences)**
    *   Case 1: `f(n)` is polynomially smaller than $n^(log_b a)$
    *   Case 2: `f(n)` is asymptotically equal to $n^(log_b a)$
    *   Case 3: `f(n)` is polynomially larger than $n^(log_b a)$ (and satisfies regularity condition).
2.  **Is amortized cost of incrementing binary counter over n increments = O(1) per increment? (T/F)**
    *   **T** - While a single increment can be O(log n), the total bit flips over n increments average out to O(1) per operation.
3.  **Worst-case ≠ average-case (True trap). (T/F)**
    *   **T** - Quicksort is a classic example where worst-case is O(n²) but average-case is O(n log n).
4.  **Is Big-O tight? (T/F) — distinguish O, Θ, Ω.**
    *   **F** - Big-O is an upper bound, not necessarily tight. `Θ` (Theta) is the tight bound. `Ω` (Omega) is a lower bound.
5.  **Can recursion tree always be used instead of Master theorem? (Y/N)**
    *   **Y** - The Master theorem is just a shortcut for analyzing common recurrence patterns that can be solved with a recursion tree.

**Example (recurrence traps):**

*   `T(n)=2T(n/2)+n log n` — which Master case applies?
    *   **None.** `f(n)=n log n` is asymptotically larger than `n^(log_2 2) = n`, but not polynomially larger, so Case 3 doesn't apply.
*   `T(n)=T(n-1)+O(1)` — solution?
    *   **O(n)** - This recurrence represents a simple loop that decrements `n` by 1 and does constant work each time.

# Approximation Algorithms

1.  **Greedy for 0/1 knapsack is optimal? (Y/N)**
    *   **N** - Greedy choice (e.g., by value/weight ratio) can fail; 0/1 Knapsack is NP-hard and requires dynamic programming for an optimal solution.
2.  **Does PTAS exist for NP-hard problems generally? (Y/N)**
    *   **N** - Only a subset of NP-hard problems (like Knapsack) have a PTAS; many (like TSP) do not, unless P=NP.
3.  **Approx ratio: smaller is always better? (T/F)**
    *   **T** - For minimization problems, a ratio `c >= 1` is sought, where `c=1` is optimal. For maximization, a ratio `c <= 1` is sought. In both cases, closer to 1 is better.

**Example (knapsack trap):**

*   **Items:** `[(v=60,w=10),(v=100,w=20),(v=120,w=30)]`, capacity=50 — greedy by value/weight picks what? Is it optimal?
    *   **Greedy picks (60,10) and (100,20) for value 160.** It's **not optimal**; the optimal solution is (100,20) and (120,30) for value 220.

# Parallel Algorithms

1.  **Amdahl’s Law: given serial fraction s, is speedup ≤ 1/(s + (1-s)/p)? (T/F)**
    *   **T** - This is the direct formula for Amdahl's Law.
2.  **Can infinite processors give infinite speedup if s>0? (Y/N)**
    *   **N** - As `p -> ∞`, the speedup is limited by `1/s`. The serial portion is the ultimate bottleneck.
3.  **PRAM models: is CRCW stronger than EREW? (T/F)**
    *   **T** - Concurrent Read, Concurrent Write (CRCW) is less restrictive (and thus more powerful/harder to build) than Exclusive Read, Exclusive Write (EREW).
4.  **Does parallel prefix sum need synchronization? (Y/N)**
    *   **Y** - It requires synchronization barriers between steps to ensure partial sums are correctly computed before being used in the next step.
5.  **Are race conditions detectable by checking pairwise locking only? (Y/N)**
    *   **N** - More complex race conditions like deadlocks can involve cycles of more than two threads/locks.

**Example (Amdahl trap):**

*   **Serial fraction `s=0.1`, `p=8`** — compute max speedup (use formula).
    *   `1 / (0.1 + (1-0.1)/8) = 1 / (0.1 + 0.9/8) = 1 / 0.2125 ≈ 4.7x` speedup.

# Quick True/False trap list (mixed)

1.  ==**Every tree is bipartite.**==
    *   **T** - A graph is bipartite iff it has no odd-length cycles. A tree has no cycles at all.
2.  **==Every DAG has a topological ordering that is unique.**==
    *   **F** - If there are multiple source nodes at any stage, their relative order can be swapped.
3.  **MST edges are a subset of shortest-path tree edges.**
    *   **F** - An MST connects all nodes with minimum weight; a shortest-path tree connects one source to all nodes with minimum path length. These are different objectives.
4.  **Max-flow algorithms always require integer capacities.**
    *   **F** - Algorithms like Edmonds-Karp work for rational capacities, but the Ford-Fulkerson method is not guaranteed to terminate for irrationals.
5.  **If `f(n)=n^c` and `g(n)=n^{c} log n`, then `g(n)` is Θ(`f(n)`)?**
    *   **F** - `g(n)` grows strictly faster than `f(n)`. `g(n)` is O(`f(n)`) is false, but `f(n)` is O(`g(n)`) is true. They are not `Θ` of each other.

# Bonus: Common Exam Traps (one-liners)

*   **“Dijkstra works with negative edges” (mark as trap).**
    *   Trap: Fails because its greedy choice assumes finalized paths can't be improved.
*   **“Choose middle as `(low+high)/2` — ignore overflow” (trap).**
    *   Trap: `low+high` can overflow; use `low+(high-low)/2` instead.
*   **“If two nodes have same distance, predecessor array is deterministic” (trap).**
    *   Trap: The final predecessor depends on the order of edge relaxation.
*   **“Greedy always optimal for 0/1 knapsack” (trap).**
    *   Trap: Optimal for Fractional Knapsack, but fails for 0/1, which is NP-hard.
*   **“Parallel speedup = p × serial speed” (trap).**
    *   Trap: This is ideal linear speedup, but Amdahl's Law shows the serial portion is a bottleneck.