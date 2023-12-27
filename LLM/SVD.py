import torch

from myplotstyle import AcademicPlot
from transformers import AutoModelForCausalLM, AutoTokenizer
# torch.linalg.matrix_rank(t)

ck_path = "/data/Data/LeonRho/model/Llama-2-7b-hf"
model = AutoModelForCausalLM.from_pretrained(ck_path).state_dict()

print(model.keys())

layer_numbers = []
attn_q_list_sum = []
attn_k_list_sum = []
attn_v_list_sum = []
o_proj_list_sum = []    
mlp_gate_proj_list_sum = []
mlp_up_proj_list_sum = []
mlp_down_proj_list_sum = []



attn_q_list_g5 = []
attn_k_list_g5 = []
attn_v_list_g5 = []
o_proj_list_g5 = []    
mlp_gate_proj_list_g5 = []
mlp_up_proj_list_g5 = []
mlp_down_proj_list_g5 = []


threshold = 4
for key in model.keys():

    print("processing: ", key)

    if "wte" in key or model[key].dim() != 2:
        continue
    if key.startswith("model.layers"):
        if key.endswith("weight"):
            
            rank = torch.linalg.matrix_rank(model[key])
            _, S, _ = torch.linalg.svd(model[key])
            layer_number = int(key.split('.')[2])
            if layer_number not in layer_numbers: 
                layer_numbers.append(layer_number)
            if "attn" in key:
                if "q_proj" in key:
                    attn_q_list_sum.append(torch.sum(S).item())
                    attn_q_list_g5.append((S > threshold).sum().item())
                elif "k_proj" in key:
                    attn_k_list_sum.append(torch.sum(S).item())
                    attn_k_list_g5.append((S > threshold).sum().item())
                elif "v_proj" in key:
                    attn_v_list_sum.append(torch.sum(S).item())
                    attn_v_list_g5.append((S > threshold).sum().item())
                else:
                    o_proj_list_sum.append(torch.sum(S).item())
                    o_proj_list_g5.append((S > threshold).sum().item())
            elif "mlp" in key:
                if "gate_proj" in key:
                    mlp_gate_proj_list_sum.append(torch.sum(S).item())
                    mlp_gate_proj_list_g5.append((S > threshold).sum().item())
                elif "up_proj" in key:
                    mlp_up_proj_list_sum.append(torch.sum(S).item())
                    mlp_up_proj_list_g5.append((S > threshold).sum().item())
                else:
                    mlp_down_proj_list_sum.append(torch.sum(S).item())
                    mlp_down_proj_list_g5.append((S > threshold).sum().item())
                
# Create a figure with subplots
plt = AcademicPlot(nrows=4,ncols=4, figsize=(24, 18),fontsize=20)

# Plotting the sum of singular values for each component
plt.plot(layer_numbers, attn_q_list_sum, marker='o',ax=plt.axs[0, 0])
plt.set_title("Sum of Singular Values (attn_q)",ax=plt.axs[0, 0])
plt.plot(layer_numbers, attn_k_list_sum, marker='o',ax=plt.axs[0, 1])
plt.set_title("Sum of Singular Values (attn_k)",ax=plt.axs[0, 1])
plt.plot(layer_numbers, attn_v_list_sum, marker='o',ax=plt.axs[0, 2])
plt.set_title("Sum of Singular Values (attn_v)",ax=plt.axs[0, 2])
plt.plot(layer_numbers, o_proj_list_sum, marker='o',ax=plt.axs[0, 3])
plt.set_title("Sum of Singular Values (o_proj)",ax=plt.axs[0, 3])
plt.plot(layer_numbers, mlp_gate_proj_list_sum, marker='o',ax=plt.axs[1, 0])
plt.set_title("Sum of Singular Values (mlp_gate_proj)",ax=plt.axs[1, 0])
plt.plot(layer_numbers, mlp_up_proj_list_sum, marker='o',ax=plt.axs[1, 1])
plt.set_title("Sum of Singular Values (mlp_up_proj)",ax=plt.axs[1, 1])
plt.plot(layer_numbers, mlp_down_proj_list_sum, marker='o',ax=plt.axs[1, 2])
plt.set_title("Sum of Singular Values (mlp_down_proj)",ax=plt.axs[1, 2])

# Plotting the number of singular values greater than 5 for each component
plt.plot(layer_numbers, attn_q_list_g5, marker='o',ax=plt.axs[2, 0])
plt.set_title("Number of Singular Values $\geq$ 5 (attn_q)",ax=plt.axs[2, 0])
plt.plot(layer_numbers, attn_k_list_g5, marker='o',ax=plt.axs[2, 1])
plt.set_title("Number of Singular Values $\geq$ 5 (attn_k)",ax=plt.axs[2, 1])
plt.plot(layer_numbers, attn_v_list_g5, marker='o',ax=plt.axs[2, 2])
plt.set_title("Number of Singular Values $\geq$ 5 (attn_v)",ax=plt.axs[2, 2])
plt.plot(layer_numbers, o_proj_list_g5, marker='o',ax=plt.axs[2, 3])
plt.set_title("Number of Singular Values $\geq$ 5 (o_proj)",ax=plt.axs[2, 3])
plt.plot(layer_numbers, mlp_gate_proj_list_g5, marker='o',ax=plt.axs[3, 0])
plt.set_title("Number of Singular Values $\geq$ 5 (mlp_gate_proj)",ax=plt.axs[3, 0])
plt.plot(layer_numbers, mlp_up_proj_list_g5, marker='o',ax=plt.axs[3, 1])
plt.set_title("Number of Singular Values $\geq$ 5 (mlp_up_proj)",ax=plt.axs[3, 1])
plt.plot(layer_numbers, mlp_down_proj_list_g5, marker='o',ax=plt.axs[3, 2])
plt.set_title("Number of Singular Values $\geq$ 5 (mlp_down_proj)",ax=plt.axs[3, 2])

for ax in plt.axs.flat:
    plt.set_xlabel("Layer Number",ax=ax)
    plt.set_ylabel("Value",ax=ax)


# Adjust layout
plt.savefig('SVD_analysis.png')
plt.show()
