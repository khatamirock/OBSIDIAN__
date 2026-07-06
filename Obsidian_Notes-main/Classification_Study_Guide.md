# Chapter 4: Classification - Comprehensive Study Guide

## Table of Contents
1. [Chapter Overview](#chapter-overview)
2. [Section 4.2: Why Not Linear Regression?](#section-42-why-not-linear-regression)
3. [Section 4.3: Logistic Regression](#section-43-logistic-regression)
4. [Section 4.4: Generative Models for Classification](#section-44-generative-models-for-classification)
5. [Key Concepts & Definitions](#key-concepts--definitions)
6. [Practical Applications](#practical-applications)

---

## Chapter Overview

### What You'll Learn
This chapter teaches you how to predict **categorical outcomes** (e.g., Yes/No, Disease A/B/C) rather than continuous values. The focus is on classification methods that predict which category an observation belongs to.

### Why This Matters
Classification problems are everywhere:
- **Medical diagnosis**: Which disease does a patient have?
- **Fraud detection**: Is this transaction fraudulent?
- **Credit risk**: Will this person default on their loan?

### Core Learning Objectives
1. Understand why linear regression fails for categorical responses
2. Master logistic regression for binary (2-class) problems
3. Learn Linear Discriminant Analysis (LDA) for multi-class problems
4. Evaluate classifier performance beyond simple accuracy

---

## Section 4.2: Why Not Linear Regression?

### What the Author is Teaching
Linear regression is **fundamentally unsuited** for classification tasks, despite seeming like a simple solution.

### Key Problem #1: Arbitrary Ordering with Multi-Class Response

**The Issue:**
When you have 3+ categories (e.g., stroke, drug overdose, epileptic seizure), encoding them as 1, 2, 3 imposes a meaningless order.

**Example:**
```
Encoding A: stroke=1, overdose=2, seizure=3
Encoding B: seizure=1, stroke=2, overdose=3
```

These produce **completely different models** and predictions, yet neither ordering makes clinical sense.

**Why We Care:**
The model treats the difference between stroke (1) and overdose (2) as the same mathematical distance as overdose (2) to seizure (3), which is medically meaningless.

### Key Problem #2: Probability Violations with Binary Response

**The Issue:**
Even with just 2 categories (Yes/No), linear regression can predict:
- Probabilities **< 0** (impossible!)
- Probabilities **> 1** (impossible!)

**When This Happens:**
- Low predictor values → negative probabilities
- High predictor values → probabilities exceeding 1

**Visual Evidence:**
See Figure 4.2 (left panel) - the linear fit crosses below 0 and could exceed 1 for extreme balances.

### What to Be Aware Of
- **Binary case exception**: Linear regression *sometimes* works for 2-class problems but is still suboptimal
- The predictions from linear regression on 0/1 coded binary responses **match LDA predictions** (interesting mathematical connection!)
- Never use linear regression when you have 3+ categories

### When to Apply This Knowledge
**Don't use linear regression when:**
- Response variable is categorical
- You need interpretable probabilities
- You have more than 2 classes

**Instead use:**
- Logistic regression (2 classes)
- Multinomial logistic regression (3+ classes)
- LDA/QDA (alternative approaches)

---

## Section 4.3: Logistic Regression

### What the Author is Teaching
Logistic regression models the **probability** of class membership using a function that always outputs values between 0 and 1.

### The Core Idea: The Logistic Function

**Mathematical Form:**

$p(X) = e^{(β₀ + β₁X)} / (1 + e^{(β₀ + β₁X)})$


**Why This Shape?**
- Always between 0 and 1 (valid probabilities!)
- Creates an **S-shaped curve** (sigmoid)
- Smooth transition from low to high probability

**Key Advantage:**
Unlike linear regression, you can never get impossible probabilities.

---

### Section 4.3.1: The Logistic Model

**What You're Learning:**
How to transform the logistic function into a linear model using the **logit transformation**.

**The Log-Odds (Logit) Transformation:**
```
log(p(X)/(1-p(X))) = β₀ + β₁X
```

**Why This Matters:**
- The left side (log-odds or logit) is linear in X
- This makes the model easier to estimate and interpret
- The coefficient β₁ represents the change in log-odds per unit change in X

**Understanding Odds:**
- Odds = p/(1-p)
- Probability of 0.2 → Odds of 1/4 (1 in 5 people)
- Probability of 0.9 → Odds of 9 (9 out of 10 people)
- Odds are common in gambling/betting contexts

**Coefficient Interpretation:**
- β₁ > 0: Increasing X increases p(X)
- β₁ < 0: Increasing X decreases p(X)
- One-unit increase in X multiplies odds by e^(β₁)

**Critical Awareness:**
The relationship between p(X) and X is **NOT linear** - the effect of changing X by 1 unit depends on the current value of X. This is different from linear regression!

---

### Section 4.3.2: Estimating the Regression Coefficients

**What You're Learning:**
How to find the "best" values for β₀ and β₁ using **maximum likelihood estimation (MLE)**.

**The Intuition:**
Find β₀ and β₁ that make the predicted probabilities:
- Close to 1 for observations that are class "Yes"
- Close to 0 for observations that are class "No"

**The Likelihood Function:**
```
L(β₀, β₁) = ∏(i: yᵢ=1) p(xᵢ) × ∏(i: yᵢ=0) (1 - p(xᵢ))
```

This multiplies all the predicted probabilities together - we want to maximize this!

**Important Notes:**
- You don't need to understand the calculus - statistical software handles this
- Maximum likelihood is more general than least squares
- For linear regression, least squares IS maximum likelihood (they're equivalent)

**Reading the Output (Table 4.1):**
- **Coefficient estimate**: β̂₁ = 0.0055 means higher balance → higher default probability
- **Standard error**: Measures uncertainty in the estimate
- **z-statistic**: Like t-statistic in linear regression
- **p-value**: Tests H₀: β₁ = 0 (no relationship)

**When to Apply:**
- Interpreting logistic regression software output
- Testing if a predictor is statistically significant
- Understanding uncertainty in your estimates

---

### Section 4.3.3: Making Predictions

**What You're Learning:**
How to use fitted coefficients to predict probabilities for new observations.

**The Prediction Formula:**
```
p̂(X) = e^(β̂₀ + β̂₁X) / (1 + e^(β̂₀ + β̂₁X))
```

**Example from Text:**
- Balance = $1,000 → p̂ = 0.00576 (0.576% chance of default)
- Balance = $2,000 → p̂ = 0.586 (58.6% chance of default)

**Key Insight:**
Small changes in balance can lead to large changes in probability when you're in the steep part of the S-curve!

**Qualitative Predictors (Dummy Variables):**
- Student status encoded as: Student=1, Non-student=0
- Positive coefficient (0.4049) means students have **higher** default probability
- This uses the same dummy variable approach from Chapter 3

**Critical Finding (Table 4.2):**
Students have higher default rates than non-students when considered alone - but this reverses when we control for balance! (See Section 4.3.4)

---

### Section 4.3.4: Multiple Logistic Regression

**What You're Learning:**
How to extend logistic regression to multiple predictors (balance, income, student status).

**The Multiple Logistic Model:**
```
log(p(X)/(1-p(X))) = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ
```

**The Confounding Paradox:**
This section reveals a **critical statistical phenomenon**:

**Single Variable (Table 4.2):**
- Student coefficient: +0.4049 (positive)
- Students have HIGHER default rates

**Multiple Variables (Table 4.3):**
- Student coefficient: -0.6468 (negative!)
- Students have LOWER default rates (controlling for balance)

**What's Happening? (Figure 4.3 explains this)**

**The Explanation:**
1. Students tend to carry higher credit card balances
2. Higher balances → higher default rates
3. So students default more overall (marginal effect)
4. BUT for the SAME balance, students default LESS (conditional effect)
5. The correlation between student status and balance creates confounding

**The Business Implication:**
- A student with unknown balance is **riskier** (higher average balance)
- A student with $1,500 balance is **less risky** than a non-student with the same balance

**Why This Matters:**
This illustrates why **multiple regression is crucial** - single-variable analyses can be misleading when predictors are correlated!

**Critical Awareness:**
- Always check for confounding when you have correlated predictors
- Results from single-predictor models can reverse in multiple-predictor models
- Context determines which relationship matters (marginal vs conditional)

**Example Prediction (Equations 4.8-4.9):**
Student with balance=$1,500, income=$40,000:
```
p̂ = 0.058 (5.8% default probability)
```

Non-student with same balance and income:
```
p̂ = 0.105 (10.5% default probability)
```

The student is less risky when balance is known!

---

### Section 4.3.5: Multinomial Logistic Regression

**What You're Learning:**
How to extend logistic regression beyond 2 classes (e.g., stroke, overdose, seizure).

**The Core Idea:**
Pick one class as the "baseline" (reference category), then model the log-odds of each other class versus this baseline.

**The Math (K classes, using class K as baseline):**
For classes k = 1, ..., K-1:
```
log(Pr(Y=k|X) / Pr(Y=K|X)) = β_{k0} + β_{k1}X₁ + ... + β_{kp}Xₚ
```

**Key Properties:**
- Choice of baseline doesn't affect predictions or log-odds between any pair of classes
- Only changes coefficient interpretation
- Need K-1 sets of coefficients

**Coefficient Interpretation (tricky!):**
With seizure as baseline:
- β_{stroke,j} = change in log-odds of stroke vs seizure for 1-unit increase in X_j
- Increasing X_j multiplies odds of stroke vs seizure by e^(β_{stroke,j})

**The Softmax Coding (Alternative):**
Instead of choosing baseline, estimate coefficients for ALL K classes:
```
Pr(Y=k|X) = e^(β_{k0} + ... + β_{kp}Xₚ) / Σₗ e^(β_{ℓ0} + ... + β_{ℓp}Xₚ)
```

**Why Learn Both?**
- Baseline coding: easier interpretation, standard in statistics
- Softmax coding: used in machine learning (especially neural networks - see Chapter 10)
- Both give identical predictions and log-odds ratios

**When to Apply:**
- Medical diagnosis with multiple diseases
- Product choice modeling (3+ options)
- Any classification with 3+ unordered categories

**Be Aware:**
- More classes require more data for reliable estimates
- Consider whether classes have a natural order (if yes, ordinal regression might be better)
- Interpretation requires care - always specify which baseline you're using

---

## Section 4.4: Generative Models for Classification

### What the Author is Teaching
An alternative approach: instead of modeling Pr(Y|X) directly, model the distribution of X within each class, then use **Bayes' theorem** to flip it around.

**The Key Philosophical Shift:**

**Discriminative (Logistic Regression):**
- Directly model Pr(Y=k|X=x) - "How do predictors discriminate between classes?"

**Generative (LDA/QDA/Naive Bayes):**
- Model Pr(X=x|Y=k) - "How is X distributed within each class?"
- Then use Bayes' theorem to get Pr(Y=k|X=x)

---

### Bayes' Theorem Foundation

**The Formula:**
```
Pr(Y=k|X=x) = [πₖ × fₖ(x)] / [Σₗ πₗ × fₗ(x)]
```

**Components:**
- **πₖ = prior probability**: Overall proportion of class k (before seeing X)
- **fₖ(x) = class-specific density**: Probability of X=x given class k
- **Posterior probability pₖ(x)**: Probability of class k given X=x (what we want!)

**Why This Approach?**

**Advantages:**
1. **Stability**: When classes are well-separated, logistic regression can be unstable
2. **Small samples**: Works better with limited data when normality assumption holds
3. **Natural extension**: Easily handles K > 2 classes
4. **Interpretability**: Can visualize class distributions

**The Challenge:**
Estimating fₖ(x) is hard! This is where different methods make different assumptions:
- LDA: Normal distribution, shared covariance
- QDA: Normal distribution, class-specific covariance
- Naive Bayes: Features are independent

---

### Section 4.4.1: Linear Discriminant Analysis (p=1)

**What You're Learning:**
LDA assumes each class follows a **normal (Gaussian) distribution** with **shared variance**.

**The Assumptions:**
```
fₖ(x) = (1/√(2πσₖ)) × exp(-(x-μₖ)²/(2σₖ²))
```

With constraint: σ₁² = σ₂² = ... = σₖ² = σ² (shared variance!)

**What This Means:**
- Each class has its own mean (μₖ) - centers can differ
- All classes have the same spread (σ²) - same variance
- Data in each class follows a bell curve

**The Discriminant Function:**
After plugging into Bayes' theorem and simplifying:
```
δₖ(x) = x × (μₖ/σ²) - (μₖ²/2σ²) + log(πₖ)
```

**Decision Rule:**
Assign observation to class with largest δₖ(x).

**Why "Linear"?**
The discriminant function δₖ(x) is a **linear function of x** - no x² or higher powers!

**The Decision Boundary (2 classes):**
The point where δ₁(x) = δ₂(x), which simplifies to:
```
x = (μ₁ + μ₂) / 2
```

The midpoint between class means! (When π₁ = π₂)

**Estimation in Practice:**
We don't know the true parameters, so we estimate:
```
μ̂ₖ = (1/nₖ) Σ xᵢ  [sample mean of class k]
σ̂² = (1/(n-K)) Σₖ Σᵢ (xᵢ - μ̂ₖ)²  [pooled variance]
π̂ₖ = nₖ/n  [sample proportion]
```

**Figure 4.4 Interpretation:**
- **Left panel**: True distributions (we know them because it's simulated)
- **Bayes decision boundary**: Optimal boundary (dashed line at x=0)
- **Right panel**: Estimated from 20+20 samples
- **LDA decision boundary**: Slightly off from optimal (solid line)
- **LDA error**: 11.1% vs Bayes error 10.6% - very close!

**What to Be Aware Of:**
- LDA performs well when normality assumption is reasonable
- Works best when variances are truly similar across classes
- Sample estimates can be off with small sample sizes
- Decision boundary is always linear (straight line in 1D, flat plane in 2D)

**When to Apply:**
- Binary classification with reasonably normal distributions
- When you believe variance is similar across classes
- Need interpretable linear decision boundaries
- Have sufficient data to estimate means and variance

---

### Section 4.4.2: Linear Discriminant Analysis (p>1)

**What You're Learning:**
Extending LDA to multiple predictors using the **multivariate Gaussian distribution**.

**The Multivariate Normal Distribution:**
```
X ~ N(μ, Σ)
```

Where:
- **μ** = mean vector (p components, one per predictor)
- **Σ** = covariance matrix (p×p, captures correlations between predictors)

**What Figure 4.5 Shows:**
- **Left**: Uncorrelated predictors (Cor(X₁,X₂)=0) → circular contours
- **Right**: Correlated predictors (Cor(X₁,X₂)=0.7) → elliptical contours
- Height of surface = probability density

**LDA Assumptions for Multiple Predictors:**
- Each class k has distribution N(μₖ, Σ)
- Class-specific mean vector μₖ (can differ)
- **Shared** covariance matrix Σ (same for all classes)

**The Multivariate Discriminant Function:**
```
δₖ(x) = x^T Σ⁻¹μₖ - (1/2)μₖ^T Σ⁻¹μₖ + log(πₖ)
```

**Why Still "Linear"?**
δₖ(x) is still linear in x (no squared terms) - the decision boundaries are **hyperplanes** in p-dimensional space.

**Figure 4.6 Analysis:**
- **Left panel**: Truth (3 classes, known parameters)
  - Ellipses = 95% probability regions for each class
  - Dashed lines = Bayes decision boundaries (optimal)
  - 3 boundaries (one for each pair of classes)

- **Right panel**: Estimated from data (20 per class)
  - Solid lines = LDA decision boundaries
  - Pretty close to Bayes boundaries!
  - Test errors: Bayes=7.46%, LDA=7.70%

**The Decision Boundary Between Classes k and ℓ:**
Set δₖ(x) = δₗ(x) and solve - this gives a linear equation (hyperplane).

**Default Data Example:**
Using balance and student status to predict default:
- Training error: 2.75%
- Seems good, but...

---

### Understanding Classifier Performance (The Nuance)

**What the Author is Teaching:**
Error rate alone is **misleading** - you must understand **types of errors** and **class imbalance**.

**The Null Classifier Problem:**
- Default rate in data: 3.33%
- A stupid classifier that always predicts "No default" has error = 3.33%!
- LDA's 2.75% is barely better than doing nothing!

**Why This Happens:**
Class imbalance - only 3.33% actually default. The model can get high accuracy by just predicting the majority class.

**The Confusion Matrix (Table 4.4):**
```
                    True Status
                 No Default  |  Default  | Total
Predicted No      9,644      |    252    | 9,896
Predicted Yes        23      |     81    |   104
Total             9,667      |    333    | 10,000
```

**Reading the Matrix:**
- **Diagonal**: Correct predictions (9,644 + 81 = 9,725)
- **Off-diagonal**: Errors
  - Type I error (False Positive): Predicted default, but didn't (23)
  - Type II error (False Negative): Predicted no default, but did (252)

**The Shocking Reality:**
- Only 23/9,667 = 0.24% error among non-defaulters (great!)
- But 252/333 = 75.7% error among defaulters (terrible!)
- **The model misses 3 out of 4 people who actually default!**

**Sensitivity and Specificity:**

**Sensitivity (True Positive Rate):**
- Percentage of defaulters correctly identified
- = 81/333 = 24.3%
- Measures: "Can we catch the positives?"

**Specificity (True Negative Rate):**
- Percentage of non-defaulters correctly identified
- = 9,644/9,667 = 99.8%
- Measures: "Can we correctly identify negatives?"

**Why Low Sensitivity?**
LDA minimizes **total** error rate (Bayes-optimal). But for imbalanced data:
- Predicting majority class is safest
- Minority class errors get "outvoted"

---

### Adjusting the Threshold (Critical Concept!)

**What You're Learning:**
You can trade off different types of errors by changing the **classification threshold**.

**The Default Threshold:**
```
Classify as "Default" if Pr(default=Yes|X) > 0.5
```

This minimizes total errors (Bayes optimal).

**Lowering the Threshold:**
```
Classify as "Default" if Pr(default=Yes|X) > 0.2
```

**Effect (Table 4.5):**
- Sensitivity improves: 75.7% → 58.6% (catches more defaulters!)
- Specificity drops: 99.8% → 97.6% (more false alarms)
- Overall error increases slightly: 2.75% → 3.73%

**The Trade-off (Figure 4.7):**
- **Low threshold**: Catch more positives, more false alarms
- **High threshold**: Miss more positives, fewer false alarms
- Threshold of 0.5 minimizes total error
- But total error may not be your goal!

**When to Lower Threshold:**
- Cost of missing a positive is high (cancer screening, fraud detection)
- Want high sensitivity even at cost of specificity

**When to Raise Threshold:**
- False alarms are costly (unnecessary medical procedures)
- Want high specificity even at cost of sensitivity

---

### The ROC Curve (Figure 4.8)

**What You're Learning:**
How to evaluate a classifier across **all possible thresholds** simultaneously.

**The ROC Curve Plots:**
- **X-axis**: False Positive Rate = 1 - Specificity
- **Y-axis**: True Positive Rate = Sensitivity

**How to Read It:**
- Each point = one threshold value
- Start (0,0): Threshold = 1 (predict no one defaults)
- End (1,1): Threshold = 0 (predict everyone defaults)
- Ideal curve: Hugs top-left corner (high TPR, low FPR)

**Area Under Curve (AUC):**
- Perfect classifier: AUC = 1.0
- Random guessing: AUC = 0.5 (the diagonal line)
- LDA on Default data: AUC = 0.95 (excellent!)

**Why ROC Curves Matter:**
- Compare classifiers without choosing a threshold
- Invariant to class imbalance
- Standard evaluation metric in medicine, ML competitions

**When to Use:**
- Comparing multiple models
- When you don't know the optimal threshold yet
- Communicating classifier performance to non-experts

**Critical Note:**
ROC curve for logistic regression on this data is virtually identical to LDA - both methods perform similarly here.

---

### Terminology Summary (Table 4.6 Concepts)

**The Author's Point:**
Classification evaluation uses **confusing overlapping terminology** from different fields. Here's the unified view:

**From a 2×2 Confusion Matrix:**
```
                  Truth: Positive  |  Truth: Negative
Predict Positive       TP          |       FP
Predict Negative       FN          |       TN
```

**Metrics (all measuring the same underlying ideas):**

**Sensitivity = Recall = True Positive Rate (TPR):**
- TP / (TP + FN)
- "Of actual positives, what fraction do we catch?"

**Specificity = True Negative Rate (TNR):**
- TN / (TN + FP)
- "Of actual negatives, what fraction do we correctly identify?"

**False Positive Rate (FPR):**
- FP / (TN + FP) = 1 - Specificity
- "Of actual negatives, what fraction do we incorrectly flag?"

**Precision = Positive Predictive Value (PPV):**
- TP / (TP + FP)
- "Of predicted positives, what fraction are actually positive?"

**Why So Many Terms?**
- Medicine uses sensitivity/specificity
- ML uses precision/recall
- Epidemiology uses predictive values
- They're all measuring error patterns!

**Be Aware:**
Always clarify which metric matters for your application:
- Cancer screening: Prioritize sensitivity (don't miss cases)
- Spam filter: Balance precision and recall
- Fraud detection: Often prioritize catching fraud (sensitivity) even with false alarms

---

## Key Concepts & Definitions

### Essential Vocabulary

**Classification:**
Predicting a categorical (qualitative) response variable.

**Binary Classification:**
Two-class problem (Yes/No, 0/1, Positive/Negative).

**Multiclass Classification:**
Three or more unordered classes.

**Logistic Function (Sigmoid):**
Function that maps real numbers to (0,1):
```
σ(z) = e^z / (1 + e^z)
```

**Logit (Log-Odds):**
```
logit(p) = log(p/(1-p))
```
The inverse of the logistic function.

**Odds:**
Ratio of probability to its complement: odds = p/(1-p)

**Maximum Likelihood Estimation (MLE):**
Method for estimating parameters by maximizing the likelihood function.

**Discriminant Function:**
Function δₖ(x) that scores how well x belongs to class k. Assign to class with highest score.

**Prior Probability (πₖ):**
Probability of class k before seeing the data (often estimated as class proportion).

**Posterior Probability (pₖ(x)):**
Probability of class k given observed data x (what we ultimately want).

**Decision Boundary:**
The boundary separating regions where different classes are predicted.

**Bayes Classifier:**
The optimal classifier that minimizes total error rate (if all model assumptions are correct).

**Confounding:**
When the relationship between X and Y changes depending on what other variables are controlled for.

**Multivariate Gaussian:**
Joint normal distribution for multiple variables, characterized by mean vector μ and covariance matrix Σ.

**Confusion Matrix:**
Table showing predicted vs actual class labels.

**Sensitivity:**
True positive rate (proportion of actual positives correctly identified).

**Specificity:**
True negative rate (proportion of actual negatives correctly identified).

**ROC Curve:**
Plot of sensitivity vs (1-specificity) across all thresholds.

**AUC (Area Under Curve):**
Summary metric for ROC curve; higher is better (max = 1.0).

---

## Practical Applications

### When to Use Each Method

**Logistic Regression:**
- **Best for:** Binary classification, need probability estimates, interpretable coefficients
- **Assumes:** Linear relationship between predictors and log-odds
- **Advantages:** Simple, interpretable, standard software, no distribution assumptions on X
- **Disadvantages:** Can be unstable with perfect separation, limited to linear boundaries

**Multinomial Logistic Regression:**
- **Best for:** 3+ unordered classes, need probability estimates
- **Assumes:** Log-odds between any pair of classes is linear in X
- **Advantages:** Natural extension of logistic regression
- **Disadvantages:** Many parameters with many classes, assumes no ordering

**Linear Discriminant Analysis (LDA):**
- **Best for:** Well-separated classes, multiple classes, normal-ish distributions
- **Assumes:** Normal distributions, **shared covariance** across classes
- **Advantages:** Stable with separation, good with small samples if assumptions hold, visualizable
- **Disadvantages:** Sensitive to normality assumption, linear boundaries only

### Real-World Decision Framework

**Step 1: Understand Your Problem**
- How many classes? (2 → logistic/LDA, 3+ → multinomial/LDA)
- What's the cost of errors? (Determines threshold, metrics)
- How much data? (Small → LDA if assumptions OK, Large → either)

**Step 2: Check Assumptions**
- Are classes roughly normal? (Yes → LDA might be better)
- Well-separated? (Yes → LDA more stable than logistic)
- Similar variances? (No → consider QDA instead of LDA)

**Step 3: Evaluate Properly**
- Class imbalanced? (Don't just use accuracy!)
- What metric matters? (Sensitivity? Specificity? F1-score?)
- Use ROC/AUC for threshold-independent comparison

**Step 4: Iterate**
- Try both logistic regression and LDA
- Compare using cross-validation on held-out data
- Adjust threshold based on business costs

### Common Pitfalls to Avoid

1. **Using linear regression for categorical outcomes**
   - Violates probability constraints
   - Meaningless with 3+ unordered classes

2. **Ignoring class imbalance**
   - High accuracy can be misleading
   - Always check sensitivity/specificity

3. **Wrong threshold**
   - Default 0.5 minimizes total error, not necessarily your loss function
   - Adjust based on relative costs of errors

4. **Confusing marginal and conditional effects**
   - Single-variable results can reverse in multiple regression
   - Always control for confounders

5. **Assuming normality without checking**
   - LDA can fail badly if distributions are very non-normal
   - Check with plots (histograms, Q-Q plots)

6. **Overfitting with too many predictors**
   - p large relative to n → unstable estimates
   - Use regularization or feature selection

7. **Reporting only training error**
   - Always evaluate on held-out test data
   - Training error underestimates true error

---

## Study Checklist

### Core Understanding
- [ ] Can explain why linear regression fails for classification
- [ ] Understand the logistic function and why it's used
- [ ] Can interpret logistic regression coefficients
- [ ] Know the difference between odds, log-odds, and probability
- [ ] Understand Bayes' theorem in the classification context
- [ ] Can explain the LDA assumptions
- [ ] Know when LDA vs logistic regression is preferred

### Technical Skills
- [ ] Can compute predicted probabilities from fitted model
- [ ] Can create and interpret a confusion matrix
- [ ] Can calculate sensitivity and specificity
- [ ] Understand how to adjust classification threshold
- [ ] Can interpret an ROC curve and AUC
- [ ] Know how to handle qualitative predictors (dummy variables)

### Conceptual Depth
- [ ] Understand confounding and why it matters
- [ ] Can explain the bias-variance trade-off in classification
- [ ] Know the difference between discriminative and generative models
- [ ] Understand why shared variance assumption matters in LDA
- [ ] Can articulate when to prioritize sensitivity vs specificity

### Application Readiness
- [ ] Can choose appropriate method for a new problem
- [ ] Know which evaluation metrics matter for different contexts
- [ ] Can communicate classifier performance to non-technical audience
- [ ] Understand business implications of false positives vs false negatives

---

## Summary: The Big Picture

**Chapter 4 Core Message:**
Classification requires specialized methods because categorical responses violate the assumptions of linear regression. The two main approaches are:

1. **Discriminative (Logistic Regression):** Directly model how predictors discriminate between classes
2. **Generative (LDA):** Model the distribution within each class, then use Bayes' theorem

**Key Insights:**
- Probability predictions must be between 0 and 1 (logistic function solves this)
- Coefficients have different interpretations than linear regression (log-odds scale)
- Accuracy alone is misleading with imbalanced classes
- Multiple predictors can reveal relationships hidden in single-variable analysis (confounding)
- Threshold choice depends on relative costs of different error types
- LDA assumes normality but can be more stable than logistic regression when classes are well-separated

**What's Next:**
Later chapters will introduce more flexible classification methods (trees, random forests, SVMs, neural networks) that can capture nonlinear decision boundaries. The principles learned here (evaluation metrics, threshold tuning, understanding trade-offs) will remain essential throughout.
