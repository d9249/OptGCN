The results are obtained on the dataset of <b>FilmTrust</b>.<br>

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| BUIR                     | 291        | NULL             | 0.08579      | 0.8377     | 0.6072   | 0.8084        |
| BUIR_Egress              | 000        | [0000,0000,0000] | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_Weight              | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_Weight_Egress       | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_NonConcat           | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| BUIR_NonConcat_Egress    | 000        | NULL             | 0.00000      | 0.04371    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| LightGCN                 | 276        | NULL             | 0.08761      | 0.8538     | 0.6157   | 0.8255        |
| LightGCN_Egress          | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_Weight          | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_Weight_Egress   | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_NonConcat       | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| LightGCN_NonConcat_Egress| 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| SGL                      | 121        | NULL             | 0.08849      | 0.8576     | 0.629    | 0.8337        |
| SGL_Egress               | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_Weight               | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_Weight_Egress        | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_NonConcat            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SGL_NonConcat_Egress     | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| SimGCL                   | 1          | NULL             | 0.02685      | 0.3136     | 0.1668   | 0.253         |
| SimGCL_Egress            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SimGCL_Weight            | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SimGCL_Weight_Egress     | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| SimGCL_NonConcat         | 000        | NULL             | 0.00000      | 0.07248    | 0.00000  | 0.00000       |
| SimGCL_NonConcat_Egress  | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| XSimGCL                  | 1          | NULL             | 0.06827      | 0.6585     | 0.4854   | 0.6433        |
| XSimGCL_Egress           | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| XSimGCL_Weight           | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| XSimGCL_Weight_Egress    | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |
| XSimGCL_NonConcat        | 000        | NULL             | 0.00000      | 0.07277    | 0.00000  | 0.00000       |
| XSimGCL_NonConcat_Egress | 000        | NULL             | 0.00000      | 0.00000    | 0.00000  | 0.00000       |

| Model                    | Best Epoch | Best Weight      | Precision@20 | Recall@20  | NDCG@20  | Hit Ratio@20  |
|:-------------------------|:----------:|:----------------:|:------------:|:----------:|:--------:|:-------------:|
| MixGCF                   | 173        | NULL             | 0.08454      | 0.832      | 0.6115   | 0.7966        |
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
