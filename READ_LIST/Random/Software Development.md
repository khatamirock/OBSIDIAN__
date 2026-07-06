 ### **1. Agile (Scrum & Kanban)** #star/5  

**Agile Manifesto**:  (*individual's working with customer response*)

| **Core Values**                  | over this ??                     |
| -------------------------------- | -------------------------------- |
| 1. Individuals and Inter.actions | Over processes and tools         |
| 2. Working Software              | Over comprehensive documentation |
| 3. Customer Collaboration        | Over contract negotiation        |
| 4. Responding to Change          | Over following a plan            |
#### **Definition**:
Agile is an ==iterative and incremental== software development method ology that focuses on flexibility, customer collaboration, and continuous improvement.
	
- **Scrum**: A structured framework that ==divides work into fixed-length iterations (sprints)== with roles like Scrum Master and Product Owner.
	- **Kanban**: A **visual workflow management** method that ==limits work in progress== (WIP) and ==focuses on continuous delivery.==
	
	#### **When to Use**:
	- When requirements are uncertain or frequently changing.
	- The technology or approach is new or risky
	- Projects needing fast and continuous delivery 
	- The project needs to be delivered quickly and in parts
	- Teams seeking close collaboration and iterative improvements.
	- The client wants to be involved ==regularly==
	
	#### **Advantages**:
	
	✅ Flexible and adaptive to changes.  
	✅ Continuous feedback improves quality.  
	✅ Increases team collaboration and customer satisfaction.
	
	#### **Disadvantages**:
	
	❌ Requires frequent customer involvement.  
	❌ Difficult to estimate time and cost accurately.  
	❌ Less suitable for highly regulated environments.

	### ✅**Agile Model – Key Points for Exam:**

	1. Agile is a **software development methodology** that promotes **iterative** and **incremental** development.
    
	2. Projects are broken into **small cycles** called **sprints** (usually 1–4 weeks).
    
	3. Focuses on:
	    - **Customer collaboration**
	    - **Flexible planning**
	    - **Continuous feedback**
	    - **Working software over documentation**
        
	4. Agile allows **changes at any stage** of development.
    
	5. Common Agile frameworks include **Scrum**, **Kanban**, and **Extreme Programming (XP)**.

	---
	
	### **2. Waterfall Model**
	
	#### **Definition**:
	
	A ==linear and sequential== software development model where each phase (Requirement → Design → Implementation → Testing → Deployment → Maintenance) must be completed before moving to the next.
	
	#### **When to Use**:
	
	- When requirements are ==well-defined== and unlikely to change.
	- For projects with ==strict regulatory compliance== (e.g., healthcare, aerospace).
	- ==Small projects== with a clear scope.
	
	#### **Advantages**:
	
	✅ Well-structured and easy to manage.  
	✅ Clear documentation at each phase.  
	✅ Suitable for projects with fixed requirements.
	
	#### **Disadvantages**:
	
	❌ Not flexible; difficult to accommodate changes.  
	❌ Late testing increases risks of defects.  
	❌ Slower delivery compared to Agile.
	

---

**2. COCOMO Model**  
**Definition:**  [[READ_LIST/CHEAT_SHEET/Software Engineering#**11. Software Cost Estimation**|more...]]
COCOMO (Constructive Cost Model) is a software cost estimation model developed by Barry Boehm. It estimates effort, time, and cost based on the size of the software (in KLOC – thousands of lines of code).

**When to Use:**

- During early planning and budgeting stages
- When project size (KLOC) can be reasonably estimated
- To compare alternative project plans or architectures

**Advantages:**  
✅ Structured and quantitative estimation  
✅ Useful for early project planning  
✅ Adaptable to different project types (Organic, Semi-Detached, Embedded)

**Disadvantages:**  
❌ Accuracy depends on precise KLOC estimation  
❌ Less suitable for Agile or modern iterative development  
❌ Assumes traditional (often waterfall) development flow

**Example:**  
Suppose you're developing a payroll system with ~32 KLOC (thousand lines of code).

Using Basic COCOMO for an **Organic** project:  
**Effort (in person-months)** = **2.4 × (32)^1.05 ≈ 91.2 PM** 

This means you'd need around 91 person-months to complete the project (e.g., 9 people working for 10 months).
[[COCOMO|See more..]]

---

### **4. Spiral Model**

![[SPIRAL_MODEL.png]]
	
#### **Definition**:
	
A ==risk-driven model== that combines iterative development,,,, with a focus on **risk assessment** and mitigation at each phase.

#### **When to Use**:

- For ==large-scale== and ==high-risk projects==.
- When customer feedback is crucial.
- When requirements are unclear at the beginning.

#### **Advantages**:

✅ Risk management is integrated into the process.  
✅ Allows iterative refinement based on feedback.  
✅ Suitable for large and complex projects.

#### **Disadvantages**:

❌ Expensive and time-consuming.  
❌ Requires expert risk management.  
❌ Not ideal for small projects.
	
	---
	
### **5. RAD (Rapid Application Development)**

#### **Definition**:

A model that emphasizes ==rapid prototyping== and quick feedback cycles rather than extensive planning.

#### **When to Use**:

- When **==rapid development==** and **==quick releases==** are required.
- For UI/UX-focused applications.
- When end-user involvement is high.

#### **Advantages**:

✅ Fast development and delivery.  
✅ Encourages customer feedback.  
✅ Reduces development cost.

#### **Disadvantages**:

❌ Requires active customer participation.  
❌ Not suitable for complex projects.  
❌ Risk of poor scalability due to quick iterations.

---

### **6. Prototyping Model**

#### **Definition**:

A development model where a prototype (mock-up) is built to understand user requirements better before full-scale development.

#### **When to Use**:

- When requirements are not well understood.
- For UI/UX-intensive applications.
- When user feedback is essential.

#### **Advantages**:

✅ Improves requirement understanding.  
✅ Reduces risk of system failure.  
✅ Increases user satisfaction.

#### **Disadvantages**:

❌ Can lead to scope creep if not managed well.  
❌ Time-consuming if multiple iterations are needed.  
❌ Higher development cost due to rework.
		### **Summary Table**
	
| Model                      | Best for                                   | Key Advantages                                     | Key Disadvantages                                   |
| -------------------------- | ------------------------------------------ | -------------------------------------------------- | --------------------------------------------------- |
| **Agile (Scrum & Kanban)** | Changing requirements, fast-paced projects | High flexibility, continuous improvement           | Needs customer involvement, unpredictable cost/time |
| **Waterfall**              | Fixed, well-defined projects               | Clear structure, easy documentation                | Rigid, late testing increases risk                  |
| **V-Model**                | Testing-focused, safety-critical systems   | Early defect detection, well-documented            | Inflexible, high initial testing cost               |
| **Spiral**                 | High-risk, large-scale projects            | Risk management, iterative approach                | Expensive, requires risk management expertise       |
| **RAD**                    | ==UI/UX-focused==, rapid development       | Fast delivery, cost-effective                      | Requires active user input, not scalable            |
| **Prototyping**            | Unclear requirements, user-driven projects | Improves understanding, enhances user satisfaction | Can lead to scope creep, costly                     |
|                            |                                            |                                                    |                                                     |
