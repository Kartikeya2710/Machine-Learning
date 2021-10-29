## Support Vector Machines Use-cases

### Should you use the primal or the dual form of the SVM problem to train a model on a training set with millions of instances and hundreds of features?

**Ans.** This question applies only to linear SVMs since kernelized can only use the dual form. The computational complexity of the primal form of the SVM problem is proportional to the number of training instances m, while the computational complexity of the dual form is proportional to a number between m² and m³. So, if there are millions of instances, you should use the primal form, because the dual form will be much too slow.
The LinearSVC class is based on liblinear which implements an optimized algorithm for linear SVMs using the primal problem or the dual problem, it does not use the Kernel Trick and thus the worst case time complexity is roughly O (m x n).
(where m and n are the number of support vectors and features respectively)
The SVC class can make use of Kernel functions and thus the computation of the solution of the Dual Problem is generally between O (m2 x n) and O (m3 x n).
This also means that for a huge dataset containing millions of training examples, the Kernelized SVM (SVC with Kernel) will become dreadfully slow. So, SVMs are generally perfect for complex small and medium sized datasets, where there are a lot of features (maybe even more than the number of training samples) but not so many training samples (say within a few hundred thousand).

Thus, SVMs are widely used in Natural Language Processing, Image Classification, etc. In fact, Vladimir Vapnik had proved that SVMs were better than some state-of-the-art algorithms like Neural Networks for hand-writing recognition back in the day.
In fact, a polynomial kernel of degree 2 is used in Natural Language Processing since larger degrees tend to overfit on NLP problems as per Wikipedia.

### What do you mean by Hinge loss?

**Ans.** Hinge Loss is a concept that is used to approach the problem of Linear SVMs from a different ‘angle’ (pun not intended). It is a more intuitive concept which aims at penalizing the algorithm for a sample X(i), having label y(i) according to the following condition:


Loss = 0 				        if  y(i)(X(i). w + b) >= 1
Loss = 1 - y(i)(X(i). w + b)	otherwise


![Image of Yaktocat](https://www.bing.com/images/search?view=detailV2&ccid=PGqpYm7o&id=2AB48070DBC5BD7CCAD0902861B8D4AB0C185150&thid=OIP.PGqpYm7o5GCbDXxXErr2JAHaFZ&mediaurl=https%3a%2f%2fi.stack.imgur.com%2fIfeze.png&exph=419&expw=575&q=hinge+loss&simid=607993861184124981&FORM=IRPRST&ck=2A73C097F2A0D8FCD851CF6DCE516939&selectedIndex=7)

Thus, the slope is 0 if the data sample satisfies the inequality constraint and is -1 otherwise making the loss function linear in nature for the latter part.
This helps in formulating a loss function for Linear SVM that can be optimized using Gradient Descent. Sir Andrew Ng has done a very clever transition from Logistic Regression to SVMs converting the loss function smoothly for an excellent understanding. You can check out my hand written notes. [3]

### Give some situations where you will use an SVM over a Random Forest Machine Learning algorithm.

**Ans.**
1.	SVMs are particularly useful for very high dimensional spaces. If your feature space is very high dimensional, you might be better off using an SVM with a polynomial kernel.
2.	SVMs can often outperform some Neural Network implementations and thus, the amount of effort in training a Neural Network might not be worth it for some cases. Eg. Simpler Image Recognition tasks.


### Point(s) worth noting:
1.	if you set probability=True when building a model of SVM in Scikit-Learn, then after training it will calibrate the probabilities using Logistic Regression on the SVM’s scores. This is computationally expensive if you have a lot of training instances but can be used for smaller datasets if needed.
2.	One cannot use any function as a Kernel function, a function must satisfy Mercer’s Theorem to become a Kernel function.


