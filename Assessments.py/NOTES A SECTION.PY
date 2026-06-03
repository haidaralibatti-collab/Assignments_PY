Section A: Concept Application – Answers

1. What is the difference between a .py file and a .ipynb file?

.py file: A standard Python script containing only Python code. It is executed from a terminal, command prompt, or IDE.
.ipynb file: A Jupyter Notebook file that contains code, output, text explanations, images, and visualizations in separate cells.

Example:

analysis.py → Only Python code.
analysis.ipynb → Code + charts + notes + outputs.

2. What is the difference between a numerical feature and a categorical feature?

Numerical Feature	Categorical Feature
Represents quantities or measurements	Represents groups or categories
Can be used for mathematical calculations	Usually represented as labels
Examples: Age, Cholesterol, Blood Pressure	Examples: Sex, Chest Pain Type, Thalassemia

In the Heart Disease dataset:

Age = Numerical feature
Cholesterol = Numerical feature
Sex = Categorical feature

3. Why does the data type of your target variable matter before framing a prediction problem?

The target variable's data type helps determine the type of machine learning problem.

If the target contains categories/classes (e.g., 0 = No Disease, 1 = Disease), it is a classification problem.
If the target contains continuous numeric values (e.g., predicting cholesterol level), it is a regression problem.

In the Heart Disease dataset, the target is an integer representing disease presence, so the problem is typically classification.

4. What does a correlation value of 0.23 tell you about two variables?

Correlation measures the strength and direction of a relationship between two variables.

A correlation of 0.23 means:

The relationship is positive.
The relationship is weak.
As age increases, the likelihood of heart disease tends to increase slightly, but age alone is not a strong predictor.

Correlation Scale:

+1 → Perfect positive relationship
0 → No relationship
-1 → Perfect negative relationship

Since 0.23 is close to 0, the relationship is weak.

5. What is the fundamental difference between a rule-based system and a data-driven approach?

Rule-Based System	Data-Driven Approach
Uses predefined rules created by experts	Learns patterns from data
Example: If cholesterol > 240, mark as high risk	Model learns risk factors automatically
Easy to understand	Can discover hidden patterns
Less flexible	More adaptable to new data

Example:

Rule-Based: If cholesterol > 240 → High Risk
Data-Driven: A machine learning model analyzes age, cholesterol, blood pressure, and other factors to predict heart disease risk.