# Big picture — what an “interrupt” is

An **interrupt** is a signal that makes the CPU stop what it’s doing and run a special routine (an Interrupt Service Routine, ISR). Interrupts let hardware or software ask the CPU for immediate attention (like pausing a movie to pick up a ringing phone).

Two important axes to classify interrupts:

1. **Who triggers it** — software vs hardware (or the CPU itself).
    
2. **Maskable or not** — can the CPU temporarily ignore it (maskable) or not (non-maskable)?
    

---

# 1) Software interrupt (`INT n`)

- **Who triggers:** a program running on the CPU (instruction `INT n`, opcode `CDh` + type byte).
    
- **When:** synchronous — the interrupt happens exactly at that instruction.
    
- **Vector:** the `n × 4` IVT entry (first 1KB of memory).
    
- **Typical uses:** system calls, explicit breakpoints, debug traps.
    
- **What CPU does (step-by-step):**
    
    1. Finish current instruction (that executed `INT`).
        
    2. **Push FLAGS** on stack.
        
    3. **Push CS**, then **push IP** (return address).
        
    4. Load new IP from memory at `n × 4`; load new CS from `n × 4 + 2`.
        
    5. Clear IF and TF (so maskable interrupts/traps won’t disturb ISR).
        
- **Analogy:** You (program) press a “call assistance” button to page the manager — you asked for help purposely.
    

---

# 2) Hardware maskable interrupt (`INTR`)

- **Who triggers:** an external device (keyboard, timer, network card) raises the `INTR` pin.
    
- **Maskable:** yes — CPU only responds if the **Interrupt Flag (IF)** is set (enabled). `CLI` disables, `STI` enables.
    
- **Vector:** the device (or PIC like 8259) supplies an interrupt **type number**; the CPU looks up `type × 4` in the IVT.
    
- **Handshake detail (important):**
    
    - CPU finishes its current instruction.
        
    - CPU issues **two INTA (Interrupt Acknowledge) pulses**:
        
        - 1st INTA = “device, get ready.”
            
        - 2nd INTA = CPU reads the **8-bit type number X** from the device/PIC.
            
- **What CPU does after receiving X:**
    
    1. Push FLAGS.
        
    2. Push CS, push IP.
        
    3. Load IP from `X × 4`; load CS from `X × 4 + 2`.
        
    4. Clear IF and TF.
        
- **Analogy:** A fire alarm (device) rings. If building security (IF) is on, control room (CPU) acknowledges twice, asks “which floor?” (gets vector), then dispatches team to that floor.
    

---

# 3) Non-Maskable Interrupt (NMI)

- **Who triggers:** a special external pin (NMI) — usually for serious events (power failure, hardware error).
    
- **Maskable?:** **No** — cannot be turned off by IF/CLI. Always has higher priority than INTR.
    
- **Vector:** fixed **type 2** (so CPU loads vector from `00008h` and `0000Ah`).
    
- **What CPU does:**
    
    1. Finish current instruction.
        
    2. Push FLAGS.
        
    3. Push CS, push IP.
        
    4. Load IP from `00008h`; CS from `0000Ah`.
        
    5. Clear IF and TF (so other maskable interrupts/traps are disabled while servicing).
        
- **Analogy:** A building’s emergency stop (big red button) — it forces immediate response no matter what overrides are in place.
    

---

# 4) CPU-generated exceptions (synchronous hardware interrupts)

- **Examples:** divide-by-zero (type 0), overflow (type 4), single-step (type 1).
    
- **Trigger:** the CPU detects a condition while executing an instruction (e.g., DIV by zero).
    
- **Behavior:** handled like an interrupt — vector is fixed (type number), same push/load steps.
    
- **Note:** these are synchronous (occur exactly where the problem happens), not asynchronous like INTR.
    

---

# Common, shared mechanics (what’s the same for all)

- CPU _finishes current instruction_ first (no half-done instructions).
    
- CPU _pushes FLAGS_, then _CS_, then _IP_ onto the stack.
    
- CPU _loads CS:IP_ from the IVT entry (which depends on type).
    
- CPU _clears IF and TF_ while ISR runs (so the CPU won’t be interrupted by maskable interrupts or single-step traps during the ISR).
    
- The ISR must end with `IRET` which _pops IP, CS, FLAGS_ (restores state).
    

**Stack push order reminder:**  
Push order = FLAGS, CS, IP. Because stack grows downward, the top of stack after the pushes contains IP (the last pushed).

---

# Quick comparison table

|Feature|Software `INT n`|Hardware `INTR` (maskable)|`NMI` (non-maskable)|CPU exceptions|
|---|--:|--:|--:|--:|
|Triggered by|Program (`INT`)|External device|Special external pin|CPU (error/condition)|
|Maskable?|—|Yes (IF controls)|No|—|
|Vector source|Operand `n` in instruction → `n×4`|Device/PIC supplies type X via INTA → `X×4`|Fixed type 2 → `00008h/0000Ah`|Fixed type (e.g., 0 → div0)|
|INTA handshake|No|**Yes — two INTA pulses**|No|No|
|Synchronous?|Yes|No (asynchronous)|No (asynchronous)|Yes (synchronous)|
|Push order & IF behavior|Push FLAGS, CS, IP; clear IF/TF|Same|Same|Same|

---

# Small, exam-sharp trap points

- **Who provides the vector?** INTR → device/PIC (via INTA). NMI → fixed (type 2). INT n → immediate in software. Exceptions → CPU.
    
- **Two INTA pulses** for maskable interrupts — first = “ready”, second = “give me vector”. Don’t forget that.
    
- **IF & TF** are cleared by the CPU when entering ISR — so maskable interrupts won’t nest unexpectedly.
    
- **Push order**: FLAGS pushed **first**, then CS, then IP. (Some students reverse this.)
    
- **Synchronous vs asynchronous**: divide-by-zero is synchronous (happens at instruction), INTR/NMI are asynchronous (can happen any time).
    

---

# Final analogy — the “Office” version (one-line each)

- **Software INT:** Employee pushes a “help” button (intentional call) → manager gets the call and acts.
    
- **INTR (maskable):** External vendor rings office phone; receptionist (IF) decides whether to forward the call; if forwarded, receptionist asks vendor which department (INTA handshake).
    
- **NMI:** Fire alarm — cannot be ignored; immediate, top-priority response.
    
- **CPU exception:** Employee trips over something while working — automatic internal alert routed immediately to safety officer.
    

---

If you want, I can now:

- Draw a tiny ASCII flow diagram for each case, **or**
    
- Give 6 one-line example questions teachers ask (with short answers) to solidify these traps.
    

Which one next?