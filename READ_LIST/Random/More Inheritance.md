# 🧬 **1. Single Inheritance**

👉 **One child inherits from one parent**

```cpp
#include <iostream>
using namespace std;

class A {
public:
    void show() { cout << "Class A\n"; }
};

class B : public A {
};

int main() {
    B obj;
    obj.show();  // inherited
}
```

---

# 🧬 **2. Multiple Inheritance**

👉 **One child inherits from multiple parents**

```cpp
#include <iostream>
using namespace std;

class A {
public:
    void showA() { cout << "Class A\n"; }
};

class B {
public:
    void showB() { cout << "Class B\n"; }
};

class C : public A, public B {
};

int main() {
    C obj;
    obj.showA();
    obj.showB();
}
```

---

# 🧬 **3. Multilevel Inheritance**

👉 **Chain inheritance (A → B → C)**

```cpp
#include <iostream>
using namespace std;

class A {
public:
    void showA() { cout << "Class A\n"; }
};

class B : public A {
};

class C : public B {
};

int main() {
    C obj;
    obj.showA();  // from A
}
```

---

# 🧬 **4. Hierarchical Inheritance**

👉 **Multiple children from one parent**

```cpp
#include <iostream>
using namespace std;

class A {
public:
    void show() { cout << "Class A\n"; }
};

class B : public A {};
class C : public A {};

int main() {
    B obj1;
    C obj2;

    obj1.show();
    obj2.show();
}
```

---

# 🧬 **5. Hybrid Inheritance**

👉 **Combination (often causes diamond problem)**

```cpp
#include <iostream>
using namespace std;

class A {
public:
    void show() { cout << "Class A\n"; }
};

class B : public A {};
class C : public A {};

class D : public B, public C {
};

int main() {
    D obj;
    // obj.show(); ❌ ambiguous (diamond problem)
}
```

👉 Fix using **virtual inheritance**:

```cpp
class B : virtual public A {};
class C : virtual public A {};
```

---

# ⚡ Final Exam Tip

👉 Write:

- Definition (1 line)
    
- Small diagram (A → B etc.)
    
- Tiny code (even partial is fine)
    

---

# 🧠 Ultra Quick Memory

- Single → 1 parent
    
- Multiple → many parents
    
- Multilevel → chain
    
- Hierarchical → 1 → many
    
- Hybrid → mix
    

---

If you want, I can:  
✔ give **very short 2-mark code versions**  
✔ or explain **diamond problem in one diagram** (VERY common exam trap)