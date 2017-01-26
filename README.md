# 7pred
*Prediction of subcellular localization of human proteins using Meka [1,2] libraries*

The **7pred** is a set of seven **GO-based predictors** able to predict the subcellular localization of human proteins.

A recent human benchmark dataset [3] and two methods of problem transformation, **Classifer Chain (CC)** and **Label Cardinality (LC)**, along with two single-label classifiers, **SMO** and **J48**, were used to create the predictive models.

**Leave-one-out cross-validation** was used to evaluate the performance of the predictors.

Proteins are represented by vectors with 429 (T-B2) and 87 (T-C2) elements (essencial GO terms selected by mEN and mLASSO classifiers [4]).

The predictive models created achieved an overall success rate between 69.2 and 72.3% (overall actual accuracy or exact match) and between 76.1 and 80.3% (overall locative accuracy).

## Predictors:
1 - Predictor T-B2/CC-J48
2 - Predictor T-B2/CC-SMO
3 - Predictor T-B2/LC-SMO
4 - Predictor T-C2/CC-J48
5 - Predictor T-C2/CC-SMO
6 - Predictor T-C2/LC-J48
7 - Predictor T-C2/LC-SMO

## Input:
1 - UniProtKB Accession Number(s) (multiple accession numbers should be separated with commas): Enter 1"
1.1 - Enter UniProtKB Accession Number(s) (e.g., P20618,P15531,P07384)
or
2 - File (one UniProtKB Accession Number per line): Enter 2"
2.1 - Enter file name (e.g., ProteinsIDs.txt)

## Output:
Seven .txt files, each one representing a predictive model, with the prediction's results.

## References:
[1] Eibe Frank, Mark A. Hall, and Ian H. Witten. The WEKA Workbench. Online Appendix for "Data Mining: Practical Machine Learning Tools and Techniques", Morgan Kaufmann, Fourth Edition, 2016.
[2] Jesse Read, Peter Reutemann, Bernhard Pfahringer, and Geoff Holmes. MEKA: A multilabel/ multi-target extension to Weka. Journal of Machine Learning Research, 17(21):1-5, 2016. URL http://jmlr.org/papers/v17/12-164.html
[3] Hong-Bin Shen and Kuo-Chen Chou. A top-down approach to enhance the power of predicting human protein subcellular localization: Hum-mPLoc 2.0. Analytical biochemistry, 394(2):269-274, 2009.
[4] Shibiao Wan, Man-Wai Mak, and Sun-Yuan Kung. Sparse regressions for predicting and interpreting subcellular localization of multi-label proteins. BMC bioinformatics, 17(1):1, 2016.
