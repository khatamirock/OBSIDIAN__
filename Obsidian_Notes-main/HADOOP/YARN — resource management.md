**Solves**
- Separates resource management from processing; allows ==multiple processing frameworks== (MapReduce, Spark etc.) to run on the same cluster.

How it works (high level)

- **ResourceManager (global)** manages cluster resources; 
- **NodeManagers** run containers on worker nodes; 
- **ApplicationMaster** manages each application’s lifecycle & negotiates containers from RM

**Modern alternatives / evolution**
- ==Kubernetes== or cloud-native scheduler