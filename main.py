import argparse
from SELFRec import SELFRec
from util.conf import ModelConf

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', '-m', type=str, default='BPR', help='name of models')
    args, _ = parser.parse_known_args()
    
    graph_baselines =  [
        'LightGCN',
        'LightGCN_Weight',
        'LightGCN_Egress',
        'LightGCN_Weight_Egress',
        'DirectAU',
        'MF'
    ]
    
    ssl_graph_models = [
        'SGL',
        'SGL_Egress',
        'SGL_Weight',
        'SGL_Weight_Egress',
        'SimGCL',
        'SimGCL_Egress',
        'SimGCL_Weight',
        'SimGCL_Weight_Egress',
        'BUIR',
        'BUIR_Egress',
        'BUIR_Weight',
        'BUIR_Weight_Egress',
        'SelfCF',
        'XSimGCL',
        'MixXSimGCL',
        'XSimGCL_Egress',
        'XSimGCL_Weight',
        'XSimGCL_Weight_Egress',
        'NCL',
        'NCL_Egress',
        'NCL_Weight',
        'NCL_Weight_Egress',
        'MixGCF',
        'MixGCF_Egress',
        'MixGCF_Weight',
        'MixGCF_Weight_Egress'
    ]

    print('=' * 80)
    print('Graph-Based Baseline Models:')
    print('   '.join(graph_baselines))
    print('-' * 100)
    print('Self-Supervised  Graph-Based Models:')
    print('   '.join(ssl_graph_models))
    print('=' * 80)
    
    model = args.model
    
    import numpy as np
    import os, random, torch
    import time
    
    def seed_everything(seed):
        random.seed(seed)
        os.environ["PYTHONHASHSEED"] = str(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False

    seed_everything(54)
    s = time.time()
    if model in graph_baselines or model in ssl_graph_models:
        conf = ModelConf('./conf/' + model + '.conf')
    else:
        print('Wrong model name!')
        exit(-1)
    rec = SELFRec(conf)
    rec.execute()
    e = time.time()
    print("Running time: %f s" % (e - s))