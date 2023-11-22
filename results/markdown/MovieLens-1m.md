The results are obtained on the dataset of <b>MovieLens-1m</b>.<br>

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| BUIR                     | 298        | NULL             | 0.14680      | 0.19115    | 0.22593  | 0.15305       |
| BUIR_Egress              | 299        | NULL             | 0.15292      | 0.20169    | 0.23589  | 0.15943       |
| BUIR_Weight              | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_Weight_Egress       | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_NonConcat           | 245        | [4,4,4]          | 0.14639      | 0.18995    | 0.21990  | 0.15262       |
| BUIR_NonConcat_Egress    | 000        | [2,2,2]          | 0.00000      | 0.04371    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| LightGCN                 | 261        | NULL             | 0.1999       | 0.272      | 0.3027   | 0.2084        |
| LightGCN_Egress          | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_Weight          | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_Weight_Egress   | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_NonConcat       | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_NonConcat_Egress| 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| SGL                      | 42         | NULL             | 0.2002       | 0.2737     | 0.3096   | 0.2087        |
| SGL_Egress               | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_Weight               | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_Weight_Egress        | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_NonConcat            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_NonConcat_Egress     | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| SimGCL                   | 217        | NULL             | 0.1784       | 0.2555     | 0.2819   | 0.186         |
| SimGCL_Egress            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SimGCL_Weight            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SimGCL_Weight_Egress     | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SimGCL_NonConcat         | 000        | NULL             | 0.00000      | 0.07248    | 0.00000  | 0.00000       |
| SimGCL_NonConcat_Egress  | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| XSimGCL                  | 61         | NULL             | 0.2051       | 0.2852     | 0.3201   | 0.2138        |
| XSimGCL_Egress           | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| XSimGCL_Weight           | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| XSimGCL_Weight_Egress    | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| XSimGCL_NonConcat        | 000        | NULL             | 0.00000      | 0.07277    | 0.00000  | 0.00000       |
| XSimGCL_NonConcat_Egress | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| MixGCF                   | 2          | NULL             | 0.1174       | 0.1491     | 0.1754   | 0.1225        |
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
