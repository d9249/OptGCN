The results are obtained on the dataset of <b>Amazon-Book</b>.<br>

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| BUIR                     | 135        | NULL             | 0.01014      | 0.02272    | 0.01782  | 0.01769       |
| BUIR_Egress              | 000        | [0000,0000,0000] | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_Weight              | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_Weight_Egress       | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_NonConcat           | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_NonConcat_Egress    | 000        | NULL             | 0.00000      | 0.04371    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| LightGCN                 | 261        | NULL             | 0.01641      | 0.03933    | 0.03063  | 0.02863       |
| LightGCN_Egress          | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_Weight          | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_Weight_Egress   | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_NonConcat       | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_NonConcat_Egress| 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| SGL                      | 29         | NULL             | 0.01867      | 0.04486    | 0.03497  | 0.03258       |
| SGL_Egress               | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_Weight               | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_Weight_Egress        | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_NonConcat            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_NonConcat_Egress     | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| SimGCL                   | 17         | NULL             | 0.02008      | 0.04819    | 0.03777  | 0.03504       |
| SimGCL_Egress            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SimGCL_Weight            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SimGCL_Weight_Egress     | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SimGCL_NonConcat         | 000        | NULL             | 0.00000      | 0.07248    | 0.00000  | 0.00000       |
| SimGCL_NonConcat_Egress  | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| XSimGCL                  | 16         | NULL             | 0.02008      | 0.04805    | 0.03774  | 0.03503       |
| XSimGCL_Egress           | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| XSimGCL_Weight           | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| XSimGCL_Weight_Egress    | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| XSimGCL_NonConcat        | 000        | NULL             | 0.00000      | 0.07277    | 0.00000  | 0.00000       |
| XSimGCL_NonConcat_Egress | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| MixGCF                   | 71         | NULL             | 0.01901      | 0.04579    | 0.03561  | 0.03318       |
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
