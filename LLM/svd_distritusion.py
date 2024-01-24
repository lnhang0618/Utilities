from sciplotlib import AcademicPlot
from transformers import AutoModelForCausalLM
import torch
import numpy as np
import seaborn as sns
import gc  # 导入垃圾收集模块

ck_path = "/data/Data/LeonRho/model/Llama-2-7b-hf"
model = AutoModelForCausalLM.from_pretrained(ck_path).state_dict()

# 初始化数组
data_arrays = { 
    "atten_q": [], "atten_k": [], "atten_v": [], "o_proj": [],
    "mlp_gate_proj": [], "mlp_up_proj": [], "mlp_down_proj": []
}

# 提取权重数据
for key in model.keys():
    print("processing: ", key)
    if "wte" in key or model[key].dim() != 2:
        continue
    if key.startswith("model.layers"):
        if key.endswith("weight"):
            # rank = torch.linalg.matrix_rank(model[key])
            # _, S, _ = torch.linalg.svd(model[key])

            layer_weights = model[key].cpu().numpy()
            layer_number = int(key.split('.')[2])
            if "attn" in key :
                if "q_proj" in key:
                    rank = torch.linalg.matrix_rank(model[key])
                    _, S, _ = torch.linalg.svd(model[key])
                    data_arrays["atten_q"].append(S)
            '''   
                elif "k_proj" in key:
                    data_arrays["atten_k"].append(layer_weights)
                elif "v_proj" in key:
                    data_arrays["atten_v"].append(layer_weights)
                else:
                    data_arrays["o_proj"].append(layer_weights)
            elif "mlp" in key:
                if "gate" in key:
                    data_arrays["mlp_gate_proj"].append(layer_weights)
                elif "up" in key:
                    data_arrays["mlp_up_proj"].append(layer_weights)
                elif "down" in key:
                    data_arrays["mlp_down_proj"].append(layer_weights)
            '''
            
    # 可选：释放TensorFlow的内部缓存
    gc.collect()

combined_data = np.column_stack((tensor.numpy() for tensor in data_arrays["atten_q"]))

atten_q = combined_data

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt

# 绘制
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x=np.linspace(1,atten_q.shape[1],atten_q.shape[1])
y=np.linspace(1,atten_q.shape[0],atten_q.shape[0])

X, Y = np.meshgrid(x, y)

Z = atten_q

ax.plot_surface(X, Y, Z, color='r')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.savefig("./assets/atten_q.png")