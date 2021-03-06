## Machine Learning
This repository focuses on the implementation and analysis of various Machine Learning Algorithms along with some hand-written notes for the same. 


### Linear Regression and Optimization Functions
I have implemented Linear Regression (Both Uninvariate and Multivariate) from scratch using NumPy along with Batch and Mini-Batch Gradient Descent (I don't find any special reason to implement Stochastic GD because it is basically Mini-batch Gradient Descent with batch-size = 1 and Mini-Batch GD serves the best of both the worlds).

### Polynomial Regression
I have implemented Polynomial Regression from scratch using NumPy and then shown how it helps tackle the problem of high bias caused by the less complex linear model on the given data. For this, I have implemented learning curves for both the algorithms and shown how the High Bias of Linear Regression is solved by the more complex Polynomial Regression.

### Ridge and Lasso Regression
I have implemented Ridge Regression from scratch and have demonstrated the difference between Linear Regression and Ridge Regression by showing the decline in the weights as the cost function gets optimized by Gradient Descent. I have also used Closed Solution (Normal Equation) for Ridge Regression for directly obtaining the optimal value of theta for the Ridge Cost Function.

### Classification Models
I have implemented Classification models like Logistic Regression and K Nearest Neighbors (KNN) from scratch on dummy data as well some 'real' data. In some cases this is accompanied by some Exploratory Data Analysis (EDA) of the data. I have also added notes for some of the models which as per me, are sufficient to get a good understanding of the algorithm. 

### Support Vector Machines and Kernels
I have added detailed hand-written notes on Support Vector Machines and Kernel Functions including the math as well as intuition behind them. The notes provide a good insight about the working and logic begind the algorithm. I have covered the primal as well as the dual problem solution for the quadratic optimization problem using Lagrange Multiplier Method and the necessity of Kernels for non-linearly separable data. I was having problem in understanding the derivation of w and b after one solves for alphas in the Dual Lagrangian problem. In the case of Kernels, we don't have our 'higher' Xi's with us so we cannot derive w and b back from alphas. This has been solved in one of the commits.

### Neural Networks
I have implemented a 3 Layer Neural Network (2 hidden layers and 1 output layer) from scratch using Python's built-in libraries on the MNIST dataset. I will also try to attach the related maths and intuition behind Neural Networks and some fundamental concepts of Deep Learning in general.

### K Means Clustering
I have implemented K Means Clustering from scratch using NumPy, matplotlib and some other built-in libraries demostrating the cluster assignment and centroid shifting step of K Means. I have also covered the process of finding the best K for a given dataset and how one should choose the optimum value of K. K Means is a self-explanatory algorithm as it is very easy to represent graphically.

### Generative Adversarial Networks (GANs)
I have covered the intuition and working process behind GANs and have tried explaining the meaning and derivation of its min-max Loss Function, which is the same as in [Ian Goodfellow's original paper](https://arxiv.org/pdf/1406.2661.pdf). I am still having some difficulty in understanding how to get to the probabilistic loss function from the BCE-type min-max loss function.
I might also try to understand the optimization process but might as well skip it for now as it is quite Math heavy.

#### I have implemented a vanilla GAN from scratch to [Generate Hand-Written Digits](https://github.com/Kartikeya2710/Hand-Written-Digit-Generator) (trained on the MNIST dataset for about 25,000 epochs with a batch size of 64) and deployed the same with the help of Heroku and Streamlit.
