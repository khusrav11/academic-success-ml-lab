# T0 vs T1 comparison

I found that T1 performs better than T0 on every metric: accuracy improved from 0.654 to 0.679, macro F1 from 0.653 to 0.679 and ROC-AUC from 0.673 to 0.734 (+0.06).

18 of T0's errors were fixed by adding week-4 signals. However 52 errors remained mostly false negatives with assignment scores between 50–70.

Conclusion: I found that early-checkpoint data predicts academic success better than enrollment data alone but about ~32% of the test set is still misclassified.