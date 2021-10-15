## Machine Learning
This repository focuses on the implementation and analysis of various Machine Learning Algorithms along with some hand-written notes for the same. 


### Linear Regression and Optimization Functions
I have implemented Linear Regression (Both Uninvariate and Multivariate) from scratch using NumPy along with Batch and Mini-Batch Gradient Descent (I don't find any special reason to implement Stochastic GD because it is basically Mini-batch Gradient Descent with batch-size = 1 and Mini-Batch GD serves the best of both the worlds).

### Polynomial Regression
I have implemented Polynomial Regression from scratch using NumPy and then shown how it helps tackle the problem of high bias caused by the less complex linear model on the given data. For this, I have implemented learning curves for both the algorithms and shown how the High Bias of Linear Regression is solved by the more complex Polynomial Regression.

### Ridge and Lasso Regression
I have implemented Ridge Regression from scratch and have demonstrated the difference between Linear Regression and Ridge Regression by showing the decline in the weights as the cost function gets optimized by Gradient Descent. I have also used Closed Solution (Normal Equation) for Ridge Regression for directly obtaining the optimal value of theta for the Ridge Cost Function.

### Classification Models
I have implemented Classification models like Logistic Regression and K Nearest Neighbors (KNN) from scratch on dummy data as well some real world data. In some cases this is accompanied by some Exploratory Data Analysis (EDA) of the data. I have also added notes for some of the models which as per me, are sufficient to get a good understanding of the in's and out's of the algorithm. I am having problem in understanding the derivation of w and b after one solves for alphas in the Dual Lagrangian problem. In the case of Kernels, we don't have our 'higher' Xi's with us so we cannot derive w and b back from alphas.

### Support Vector Machines and Kernels
I have added detailed hand-written notes on Support Vector Machines and Kernel Functions including the math as well as intuition behind them. The notes provide a good insight about the working and logic begind the algorithm. I have covered the primal as well as the dual problem solution for the quadratic optimization problem using Lagrange Multiplier Method and the necessity of Kernels for non-linearly separable data.

### Neural Networks
I have implemented a 3 Layer Neural Network (2 hidden layers and 1 output layer) from scratch using Python's built-in libraries on the MNIST dataset. I will also try to attach the related maths and intuition behind Neural Networks and some fundamental concepts of Deep Learning in general.
