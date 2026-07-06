### ✅ **What is Overfitting?**

Overfitting happens when a model learns the training data _too well_ — including noise and random patterns — instead of generalizing to new, unseen data.
#### 🔧 **How to Prevent Overfitting**
1. IIncreasing training data
2. Make the model more effective and complex
3. Regularization (L1, and L2)
4. prunning
5. Dropout *(During training, you randomly "turn off" a percentage of neurons in each layer)*
6. cross-validation and early stopping

"StandardScaler is a preprocessing technique used to transform features so they have a ==**mean of 0** and a **standard deviation of 1**.== 
This process is called **Standardization** (or Z-score normalization). 
*It ensures that features with different scales—like 'Age' (0–100) and 'Annual Income' ($20,000–$200,000)—are treated equally by the model."*


### 2. Why do we actually need it? (The "Pro" Insight)
This is where you show deep knowledge. Mention these three categories of algorithms:

- ==**Distance-==based models:** Algorithms like **KNN, K-Means, and SVM** calculate the distance between points. If one feature has a much larger rang==e, it will dominate the distance== calculation, making the other features "invisible."
    
- ==**Gradien==t Descent-based models:** For **Logistic Regression, Linear Regression, and Neural Networks**, ==scaling helps== the gradient descent optimizer converge to the global minimum ==much faster==. Without it, the loss function looks like a long, skinny valley, making the optimization "zig-zag" inefficiently.
    
- **Tree-based models (The Exception):** It's worth mentioning that **Random Forests and XGBoost** are generally scale-==invariant==. They split based on rank, so scaling usually won't change their performance.

 


### L1 & L2 Reguralization
Reguralization is used for penalty added to the loss function. Instead of minimizing the loss funciton alone model try to minimize the penalty parameter  
- L1 (Lasso): L1 used for ==feature selection==. Like if we got ==100 features== we can use l1 lasso to get the most relevant features and zero out the rest...
- L2 (Ridge): L2 adds penalty of square of the magnitudes of coefficients. L2 is best for ==multi-colinearity== (when features are highly correlated)
- **L1 → feature selection**
- **L2 → shrink weights**
#### Sparse and Dense Matrix...
#### **L1 (Lasso) and L2 (Ridge) regularization** 
are techniques used to ==prevent overfitting== by adding ==a _penalty_== to the ==model’s loss function==. This discourages the model from assigning overly large weights to features.

---

### 🎯 **Bias–Variance Tradeoff (Simple but Deep)**

Every model makes errors from two sources:

- **Bias** → error from _wrong assumptions_ (model too simple)
- **Variance** → error from _too much sensitivity to data_ (model too complex)


👉 If your model has **high variance**:
- Training error = **very low**
- Test/validation error = **high**

If you detect **high variance**:
- Add **regularization (L1/L2)**
- Use **Dropout (Neural Nets)**

---
### THE PRECISION RECALL MATTERS.........
Suppose we have 150 people and we are testing whether they are sick.

Reality:

- 30 people are ==actually sick==
- 120 people are not sick


Now suppose the model ==predicts==:

- 40 people as “sick”
- Among those 40, only 25 are actually sick
- The remaining 15 are healthy but predicted sick

Also:

- Since 30 people were actually sick and only 25 were found,
- 5 sick people were missed


So we get:

|Actual / Predicted|Sick|Not Sick|
|---|--:|--:|
|Sick|25|5|
|Not Sick|15|105|

Meaning:

- TP (True Positive) = 25 → sick people correctly found
    
- FP (False Positive) = 15 → healthy people wrongly called sick
    
- FN (False Negative) = 5 → sick people missed
    
- TN (True Negative) = 105 → healthy people correctly identified
    

---

# Precision

> Out of everyone the model said was sick, how many were actually sick?

$\text{Precision} = \frac{TP}{TP+FP}$

Here:


$\text{Precision} = \frac{25}{25+15} = \frac{25}{40} = 0.625$

So precision = 62.5%

Meaning:

> When the model says someone is sick, it is correct 62.5% of the time.

---

# Recall

> Out of all the actually sick people, how many did the model successfully find?

$\text{Recall} = \frac{TP}{TP+FN}$

Here:
$\text{Recall} = \frac{25}{25+5} = \frac{25}{30} = 0.833$


So recall = 83.3%

Meaning:

> The model found 83.3% of the sick people.

---

# Easy Way to Remember

- Precision = "When I predict YES, how often am I right?"
- Recall = "Out of all the real YES cases, how many did I catch?"

---

# Real-Life Difference

Imagine hospital screening:

- High Recall is important because we do not want to miss sick people
- Even if some healthy people are incorrectly flagged


Example:  
If a model predicts everyone is sick:

- Recall = 100% (nobody sick is missed)
- Precision becomes low because many healthy people are falsely called sick


If a model predicts only 5 people are sick, and all 5 really are:

- Precision = 100%
- But recall may be low because many sick people were missed

---


Using the same 150 people:
### Case 1: Very High Precision

Model predicts only 10 people as sick, and all 10 are actually sick.

- Precision = 100%
- But there were really 30 sick people
- Recall = 10/30 = 33%

So it is very careful, but misses many sick people.

### Case 2: Very High Recall
Model predicts 60 people as sick.

- It catches all 30 sick people
- But 30 healthy people are wrongly predicted sick

Then:

- Recall = 100%
- Precision = 30/60 = 50%

So it catches everyone sick, but creates many false alarms.

The tradeoff:

- More aggressive prediction → higher recall, lower precision
- More careful prediction → higher precision, lower recall


For interviews, one strong sentence is:

> Precision matters when false alarms are costly, while recall matters when missing a true case is dangerous.



- Dense: A typical matrix where almost all the elements are non zero...
- Sparse: a matrix in which vast majority of the elements are zero...

### TF-IDF:
- TF: Term frequency: Its used to measure a word in a sentence is how much meaningful in this sentence, its used for local measuring, like ==how often== a ==word appears== in a line ??
- IDF: measures ==how rare== the words across all 20 documents  ??
	- Here is the secret: **==IDF isn’t about "meaning," it’s about "discrimination.=="**
  
  
  
### Evaluation Matrix:
##### **Golden Rule (MEMORIZE THIS)**
**“The ==choice of metric== depends on the ==business problem== and error cost.”**



### ## What are Residuals?
[Residuals](https://www.geeksforgeeks.org/machine-learning/how-to-calculate-studentized-residuals-in-python/) are the differences between ==observed and predicted== values of the dependent variable. Mathematically, the residual for the i-th observation is given by:
$Residual_i​=y_i​−cap(y)_i​$


## What is the purpose of residual plots?

Residual plots are graphical representations that plot residuals on the y-axis and the fitted values (or another variable) on the x-axis. These plots are essential for the following reasons:

1. ****Checking for ==Nonlinearity==****: In a well-fitted nonlinear model, the residuals ==should not display any systematic pattern== when plotted against the fitted values. Any discernible pattern suggests that the model may not have captured all the nonlinear relationships in the data.
2. ****Detecting Heteroscedasticity****: Heteroscedasticity refers to non-constant variance of residuals. A residual plot that fans out or shows increasing spread with fitted values indicates heteroscedasticity. This violates the assumption of constant variance, which can impact the reliability of the regression estimates.
3. ****Identifying Outliers****: Outliers are data points that have large residuals compared to the majority of the data. These points can disproportionately influence the model and lead to biased estimates.
4. ****Assessing Independence****: Residual plots can help detect ==autocorrelation== in the residuals, particularly when the data is time series. Patterns such as consecutive positive and negative residuals indicate a lack of independence


### 🎯 **The Question** ⭐

**“What are the assumptions of Linear / Logistic Regression?**

1. Linearity
2. independence of errors
	   `Errors should NOT be correlated`
3. ==No Multicollinearity==
	1. Features should not be highly correlated
		1. When **two or more features are highly correlated**, meaning they carry the _same information_.
4. Normality of errors
	1. `Errors should be normally distributed`
5. Homoscedasticity
	1. ==Constant variance of errors==



### Z-Test & P value
- Z-Statistic (Signal vs Noise)

	- Coefficient = **10**
	- Error (uncertainty) = **1**
	→ z = 10 (very strong signal 😎)

- P-Value (Decision Maker)
	- Probability that this result happened by chance
	
“The z-statistic measures how strong a coefficient is relative to its uncertainty, 
and the p-value tells us ==the probability that this effect occurred by chance==. A low p-value indicates the feature is statistically significant.”


### Baggin V Boosting
#### 🌲 **Bagging (Random Forest)**
- 👉 **Reduce variance (overfitting)**
##### 🔧 How it works:
- Take ==random samples of data== (with replacement)
- Train multiple trees **independently**
- Final prediction = **average / voting**

#### 🚀 **Boosting (XGBoost)**:
- 👉 **Reduce bias (and also variance)**
##### 🔧 How it works:
- Train first tree
- Check errors
- Next tree focuses on **mistakes**
- Repeat sequentially


### Intuition for vanishing gradients
When training moves error backward through many steps, the learning signal gets weaker and weaker, like a message passed through many people until it becomes faint.


### RNN LSTM & OTHERS

#### 1. ) RNN: the basic memory machine 
An RNN processes a sequence **one step at a time** and keeps a **hidden state** as its memory
At each word:
- it reads the current word
- combines it with the previous memory
- updates the memory

RNNs struggle because of:
- **vanishing gradients**
- **exploding gradients**

#### 2. LSTM:
LSTM was built to fix the long-memory problem of RNNs.

An LSTM is like a smart notebook with:
- a **cell state** = long-term memory
- gates = control valves deciding what to remember, forget, and output
![[Pasted image 20260408152912.png]]

#### 3. GRU: the simpler LSTM:
It also helps with long-term memory, but with fewer gates and less complexity.

If LSTM is:
- detailed notebook with separate controls

GRU is:
- a simpler notebook with fewer knobs


#### 4) Transformers: no recurrence:

Instead of reading words one by one and <<storing  memory ... in a hidden state ||, 
Transformers let each word **look at all other words directly**.
==That is the key idea: **attention**.==
###### Self-Attention — If They Dig Deeper
> **"In self-attention, each word gets turned into three vectors — Query, Key and Value. The Query asks 'what am I looking for?', the Key says 'what do I contain?', and the Value is the actual information. We multiply Q and K to get attention scores, then use those scores to take a weighted sum of the Values. That gives each word a context-aware representation."**

#### Why Transformers beat RNNs in practice

###### 1. Parallelism
RNNs read one step at a time, so training is slower.
Transformers process many tokens at once during training, which is much faster on GPUs.

##### 2. Better long-range dependency handling
A word can directly attend to another word far away.

###### 3. Scales better
This is why modern NLP moved heavily toward Transformers.


| Model       | Main idea                            | Strength                    | Weakness                                   |
| ----------- | ------------------------------------ | --------------------------- | ------------------------------------------ |
| RNN         | hidden state carries memory          | simple                      | poor long-term memory                      |
| LSTM        | gated memory control                 | long dependencies           | more complex                               |
| GRU         | simpler gated memory (update, reset) | faster, fewer params        | slightly less expressive sometimes         |
| Transformer | attention over all tokens            | best for long-range context | more compute, especially on long sequences |



![[Pasted image 20260412225728.png]]

![[Pasted image 20260412225655.png]]


![[Pasted image 20260412225748.png]]


![[Pasted image 20260412225826.png]]