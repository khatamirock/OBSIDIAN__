Pattern: one node (Master/Leader) coordinates work; others (Slaves/Followers/Workers) perform tasks or hold replicated data.

What master does
- Assigns work, manages metadata, coordinates state (e.g., NameNode in classic HDFS, Leader in many consensus protocols)

What slaves do
- Execute tasks or serve read requests; typically follow master instructions    

Drawbacks / risks
- Single master can be a ==single point of failure (SPOF==) unless you add HA (active/passive leader election)
- Complexity in leader election and split-brain handling

Modern naming: use **Leader–Follower** or **Primary–Replica** instead of master–slave.