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
