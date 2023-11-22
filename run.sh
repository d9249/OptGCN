# nohup ./run.sh &

# ==========================================
python main.py -m=LightGCN
python main.py -m=SimGCL
python main.py -m=XSimGCL
python main.py -m=SGL
python main.py -m=BUIR
python main.py -m=MixGCF
python main.py -m=NCL
# ==========================================
python main.py -m=LightGCN_Weight
python main.py -m=SimGCL_Weight
python main.py -m=XSimGCL_Weight
python main.py -m=SGL_Weight
python main.py -m=BUIR_Weight
python main.py -m=MixGCF_Weight
python main.py -m=NCL_Weight
# ==========================================
python main.py -m=LightGCN_Egress
python main.py -m=SimGCL_Egress
python main.py -m=XSimGCL_Egress
python main.py -m=SGL_Egress
python main.py -m=BUIR_Egress
python main.py -m=MixGCF_Egress
python main.py -m=NCL_Egress
# ==========================================
python main.py -m=LightGCN_Weight_Egress
python main.py -m=SimGCL_Weight_Egress
python main.py -m=XSimGCL_Weight_Egress
python main.py -m=SGL_Weight_Egress
python main.py -m=BUIR_Weight_Egress
python main.py -m=MixGCF_Weight_Egress
python main.py -m=NCL_Weight_Egress
# ==========================================