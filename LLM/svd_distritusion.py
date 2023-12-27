from myplotstyle import AcademicPlot
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
    if "wte" in key or model[key].dim() != 2:
        continue
    layer_weights = model[key].detach().numpy()  # 转换为numpy数组，并与原始Tensor断开连接
    layer_number = int(key.split('.')[2])
    if "attn" in key:
        if "q_proj" in key:
            data_arrays["atten_q"].append(layer_weights)
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

    # 可选：释放TensorFlow的内部缓存
    gc.collect()

plt = AcademicPlot(figsize=(24, 18), nrows=2, ncols=4)

def plot_heatmap(data, ax, title):
    sns.heatmap(np.vstack(data), ax=ax, cmap="viridis", cbar=False)
    plt.set_title(title, ax)

# 绘制每种权重类型的热力图，并清除数据
for key, array in data_arrays.items():
    row, col = (0, ["atten_q", "atten_k", "atten_v", "o_proj"].index(key)) if key in ["atten_q", "atten_k", "atten_v", "o_proj"] else (1, ["mlp_gate_proj", "mlp_up_proj", "mlp_down_proj"].index(key))
    plot_heatmap(array, plt.axs[row, col], key)
    array.clear()  # 清除数据

# 设置坐标轴标签
for ax in plt.axs.flat:
    ax.set_xlabel("Depth")
    ax.set_ylabel("Width")

# 保存并显示图像
plt.savefig("./assets/svd_distribution.png")
plt.show()

gc.collect()  # 再次进行垃圾收集
