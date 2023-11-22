The results are obtained on the dataset of <b>Amazon-kindle</b>.<br>

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| BUIR                     | 296        | NULL             | 0.00949      | 0.07104    | 0.03876  | 0.05365       |
| BUIR_Egress              | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_Weight              | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_Weight_Egress       | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_NonConcat           | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_NonConcat_Egress    | 000        | NULL             | 0.00000      | 0.04371    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| LightGCN                 | 296        | NULL             | 0.02662      | 0.1887     | 0.119    | 0.1505        |
| LightGCN_Egress          | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_Weight          | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_Weight_Egress   | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_NonConcat       | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_NonConcat_Egress| 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| SGL                      | 45         | NULL             | 0.02946      | 0.2055     | 0.1296   | 0.1688        |
| SGL_Egress               | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_Weight               | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_Weight_Egress        | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_NonConcat            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_NonConcat_Egress     | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| SimGCL                   | 18         | NULL             | 0.02791      | 0.1932     | 0.1202   | 0.1578        |
| SimGCL_Egress            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SimGCL_Weight            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SimGCL_Weight_Egress     | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SimGCL_NonConcat         | 000        | NULL             | 0.00000      | 0.07248    | 0.00000  | 0.00000       |
| SimGCL_NonConcat_Egress  | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| XSimGCL                  | 24         | NULL             | 0.02924      | 0.2017     | 0.1283   | 0.1653        |
| XSimGCL_Egress           | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| XSimGCL_Weight           | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| XSimGCL_Weight_Egress    | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| XSimGCL_NonConcat        | 000        | NULL             | 0.00000      | 0.07277    | 0.00000  | 0.00000       |
| XSimGCL_NonConcat_Egress | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| MixGCF                   | 69         | NULL             | 0.02986      | 0.2049     | 0.1248   | 0.1688        |
| MixGCF_Egress            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| MixGCF_Weight            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| MixGCF_Weight_Egress     | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| MixGCF_NonConcat         | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| MixGCF_NonConcat_Egress  | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| NCL                      | -          | NULL             | -            | -          | -        | -             |
| NCL_Egress               | -          | NULL             | -            | -          | -        | -             |
| NCL_Weight               | -          | NULL             | -            | -          | -        | -             |
| NCL_Weight_Egress        | -          | NULL             | -            | -          | -        | -             |
| NCL_NonConcat            | -          | NULL             | -            | -          | -        | -             |
| NCL_NonConcat_Egress     | -          | NULL             | -            | -          | -        | -             |
