# Fundamental Regression Pipeline

This is a **foundation project** to build procedural fluency in regression.

## Goal
Build one clean, correct regression pipeline that can be reused on any tabular dataset.

Focus is on **correct sequencing and decisions**.

This repo is about **muscle memory and building fluency**, not novelty.

## Checkpoint 1

### 1. Problem Setup
- Defined the prediction target (`MedHouseVal`) as `y`
- Defined all remaining columns as input features `X`
- Ensured strict separation between inputs and target to prevent leakage

### 2. Data Splitting
- Split the dataset into:
  - Training set (60%)
  - Validation set (20%)
  - Test set (20%)
- All splits were performed **before** any model training
- Shuffling was enabled to ensure representative distributions

### 3. Baseline Model
- Implemented a constant baseline predictor using the **mean of `y_train`**
- Evaluated baseline performance using Mean Squared Error (MSE):
  - Train MSE ≈ 1.33
  - Validation MSE ≈ 1.30
- This established the minimum performance bar for any learned model

### 4. Linear Regression Model
- Trained a plain `LinearRegression` model on the training data only
- Evaluated performance across all splits:
  - Train MSE ≈ 0.51
  - Validation MSE ≈ 0.53
  - Test MSE ≈ 0.55

### 5. Key Takeaways
- The linear model significantly outperformed the baseline
- Similar error across train, validation, and test sets indicates healthy generalization
- The pipeline shows no signs of data leakage or overfitting

This completes a clean, end-to-end regression workflow that can be reused and extended with more advanced models or feature transformations.

## Checkpoint 2

### 6. Feature Scaling Diagnostic
- Applied `StandardScaler` to input features
- Scaler was fit **only on the training set (`X_train`)**
- The same scaler was used to transform:
  - `X_train`
  - `X_val`
  - `X_test`
- Verified scaling correctness:
  - Training feature means ≈ 0
  - Training feature standard deviations ≈ 1
- Retrained `LinearRegression` on scaled features:
  - Train MSE ≈ 0.51
  - Validation MSE ≈ 0.53
  - Test MSE ≈ 0.55

### 7. Regularization Check (Ridge Regression)
- Trained `Ridge` regression on scaled features
- Evaluated the effect of increasing regularization strength (`alpha`)
- Observed behavior:
  - Small `alpha` values behaved similarly to Linear Regression
  - Larger `alpha` values increased both training and validation MSE

### 8. Key Takeaways
- Feature scaling was implemented correctly and caused no data leakage
- Scaling did not improve Linear Regression performance, as expected
- The linear model was not overfitting
- Regularization introduced unnecessary bias and degraded performance
- Further improvement required increasing model capacity

## Checkpoint 3

### 9. Model Complexity Upgrade (Decision Tree Regression)
- Introduced `DecisionTreeRegressor` to capture nonlinear relationships
- Trained an unconstrained decision tree:
  - Train MSE ≈ 0.00
  - Validation MSE ≈ 0.53

### 10. Complexity Control
- Reduced model capacity by limiting tree depth
- Observed bias–variance behavior:
  - Shallow trees underfit
  - Deep trees overfit
- Identified that controlled depth improved validation performance

### 11. Hyperparameter Selection (Cross-Validation)
- Used cross-validation on training data only to select `max_depth`
- Avoided repeated use of the validation set for decision-making
- Best cross-validated result:
  - `max_depth = 10`
  - CV MSE ≈ 0.44

### 12. Final Evaluation
- Refit `DecisionTreeRegressor(max_depth=10)` on full training data
- Evaluated final model performance:
  - Train MSE ≈ 0.21
  - Validation MSE ≈ 0.44
  - Test MSE ≈ 0.45

### 13. Key Takeaways
- Linear models underfit the dataset
- Regularization was unnecessary due to lack of overfitting
- Increasing model complexity was the correct intervention
- Complexity control was essential for generalization
- Cross-validation enabled principled hyperparameter selection
- Final test performance closely matched validation performance
