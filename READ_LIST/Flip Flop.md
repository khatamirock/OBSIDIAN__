A **flip-flop** is a fundamental building block in digital electronics, used to store a single bit of binary data.It has two stable states, representing a '0' or a '1', and can maintain its state indefinitely until an input signal prompts it to switch states. 

**Key Points:**

- **Storage Element: Flip-flops serve as ==basic memory units== in digital systems, capable of storing one bit of information.
    
- **Types of Flip-Flops:**
    
    - **SR (Set-Reset) Flip-Flop:** Has two inputs, Set (S) and Reset (R). Setting S to '1' stores a '1'; setting R to '1' stores a '0'.

|       |       |       |        |
| ----- | ----- | ----- | ------ |
| **S** | **R** | **Q** | **Q’** |
| 0     | 0     | 0     | 1      |
| 0     | 1     | 0     | 1      |
| 1     | 0     | 1     | 0      |
| 1     | 1     | ∞     | ∞      |

**D (Data or Delay) Flip-Flop:** Captures the value of the D-input at a specific portion of the clock cycle (rising or falling edge) and stores it until the next clock event.

|           |       |       |        |
| --------- | ----- | ----- | ------ |
| **Clock** | **D** | **Q** | **Q’** |
| ↓ » 0     | 0     | 0     | 1      |
| ↑ » 1     | 0     | 0     | 1      |
| ↓ » 0     | 1     | 0     | 1      |
| ↑ » 1     | 1     | 1     | 0      |

    
 **JK Flip-Flop:** An **enhancement** of the SR flip-flop that eliminates invalid states. With i==nputs J and K, it can toggle its state when both inputs are high.==

- **Inputs:** J (Set), K (Reset)
- **Operation:**
    - Similar to SR but eliminates the invalid state.
    - When J=1,K=1 the flip-flop toggles its state.

#### Truth Table:

| **J** (set) | **K** (reset) | Q(t) (Previous State) | Q(t+1) (Next State) |
| ----------- | ------------- | --------------------- | ------------------- |
| 0           | 0             | 0                     | No Change           |
| 0           | 0             | 1                     | No Change           |
| 0           | 1             | X                     | 0 (Reset)           |
| 1           | 0             | X                     | 1 (Set)             |
| 1           | 1             | 0                     | 1 (Toggle)          |
| 1           | 1             | 1                     | 0 (Toggle)          |


	
**T (Toggle) Flip-Flop:** Toggles its state with each clock pulse when its single input T is high. It=='s useful in counters and toggle== operations.

|       |       |             |
| ----- | ----- | ----------- |
| **T** | **Q** | **Q (t+1)** |
| 0     | 0     | 0           |
| 1     | 0     | 1           |
| 0     | 1     | 1           |
| 1     | 1     | 0           |

- **Clock Dependency:** Flip-flops are edge-triggered devices, meaning they change states on specific transitions of the clock signal (rising or falling edge). This makes them suitable for synchronous circuits where operations are coordinated by clock pulses.
    
- **Applications:** Flip-flops are integral in constructing memory elements, registers, counters, and shift registers, forming the backbone of sequential logic circuits.



