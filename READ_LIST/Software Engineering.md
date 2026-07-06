
# Software Testing Types

## 1. **Manual vs. Automated Testing**

- **Manual Testing**: Performed by humans without automation tools.
- **Automated Testing**: Uses scripts and tools to perform tests automatically.

## 2. **Levels of Testing**

### 2.1 Unit Testing

- Tests individual components (functions, classes, modules).
- Typically automated.
- Example: Testing a function that calculates tax.

### 2.2 Integration Testing

- Tests ==interactions between integrated components== or modules.
- Ensures data flows correctly between them.
- Example: Checking if a login system correctly interacts with a database.

### 2.3 System Testing

- Tests the complete, integrated system to validate requirements.
- Example: Running the full application to check overall behavior.

### 2.4 Acceptance Testing

- Verifies if the system meets business requirements.
- **Types:**
    - **User Acceptance Testing (UAT)**: Performed by end-users.
    - **Alpha Testing**: Done in a controlled environment ==before public release.==
    - **Beta Testing**: Done by real users in a live environment ==before final release.==

## 3. **Types of Testing by Purpose**

### 3.1 Functional Testing

- Ensures the software functions as expected.
- Example: Verifying that a signup form works correctly.

### 3.2 Non-Functional Testing

- Tests aspects like performance, usability, security.
- Example: Checking how fast a webpage loads.

### 3.3 Regression Testing

- Ensures new changes don’t break existing functionality.
- Example: After updating a login feature, checking if previous functions still work.

### 3.4 Performance Testing

- Measures system speed, responsiveness, stability.
- **Types:**
    - **Load Testing**: Tests under expected load.
    - **Stress Testing**: Tests under extreme load.
    - **Scalability Testing**: Tests ability to handle increasing loads.

### 3.5 Security Testing

- Identifies vulnerabilities and weaknesses.
- Example: Testing against SQL injection attacks.

### 3.6 Usability Testing

- Checks ease of use and user experience.
- Example: Evaluating if users find an e-commerce site easy to navigate.

### 3.7 Compatibility Testing

- Ensures software works on different devices, OS, and browsers.
- Example: Checking if a website runs correctly on Chrome, Firefox, and Safari.

### 3.8 Smoke Testing

- ==Quick, basic test to check== if the software is stable for further testing.
- Example: Running key functionalities before deeper testing.

### 3.9 Sanity Testing

- Focuses on specific new features or bug fixes.
- Example: If a login bug was fixed, only testing the login system.

## 4. **Specialized Testing**

### 4.1 A/B Testing

- ==Compares two versions of a feature to determine better performance.==

### 4.2 Exploratory Testing

- Tester explores software without predefined test cases.

### 4.3 Ad-hoc Testing

- ==Informal, unstructured testing without documentation.==

### 4.4 Monkey Testing

- Random inputs are given to test system robustness.

---

This structured note helps in organizing different testing types in a clear way for Obsidian study purposes.



---
# ✍️ **Testing in ==Implementation== Stage**

👉  
During the implementation stage, testing ensures that the developed program works correctly, meets requirements, and is free from errors. The following types of testing are commonly performed:

---

## 🧪 **1. Unit Testing**

**Definition:**  
Testing individual modules or components of a program separately.

**Purpose:**

- Verify each function works correctly
    

**Example:**  
Testing a single function like `calculateTotal()`

---

## 🔗 **2. Integration Testing**

**Definition:**  
Testing combined modules to check interaction between them.

**Purpose:**

- Detect interface errors between modules
    

**Example:**  
Checking if login module correctly connects with database

---

## 🖥️ **3. System Testing**

**Definition:**  
Testing the complete integrated system as a whole.

**Purpose:**

- Ensure the entire system meets requirements
    

**Example:**  
Testing full software (login → process → output)

---

## ✅ **4. Acceptance Testing**

**Definition:**  
Testing done to verify the system meets user requirements.

**Types:**
- Alpha Testing (developer site)
- Beta Testing (real users)

---

## 🔍 **5. White Box Testing**

**Definition:**  
Testing internal logic and code structure.

**Focus:**

- Code paths, loops, conditions
    

---

## 🔒 **6. Black Box Testing**

**Definition:**  
Testing functionality without knowing internal code.

**Focus:**

- Inputs and outputs
    

---

## ⚡ **7. Regression Testing**

**Definition:**  
Re-testing after changes to ensure old features still work.

---

# 🧠 Quick Revision

- Unit → single module
    
- Integration → module interaction
    
- System → full system
    
- Acceptance → user validation
    
- White → inside code
    
- Black → outside view
    
- Regression → after changes
    

---

If you want, I can convert this into:  
✔ 5-mark / 10-mark formatted answer  
✔ bullet vs paragraph style (depending on exam pattern)  
✔ or past question variations 👍
