import torch

from myplotstyle import AcademicPlot
# torch.linalg.matrix_rank(t)



ck_path = "/data/Data/LeonRho/model/Llama-1B/training/iter-011999-ckpt.pth"
model = torch.load(ck_path)

print(model.keys())

layer_numbers = []
attn_list_sum = []
c_proj_list_sum = []    
mlp_c_fc1_list_sum = []
mlp_c_fc2_list_sum = []
mlp_c_proj_list_sum = []



attn_list_g5 = []
c_proj_list_g5 = []    
mlp_c_fc1_list_g5 = []
mlp_c_fc2_list_g5 = []
mlp_c_proj_list_g5 = []


threshold = 4
for key in model.keys():

    print("processing: ", key)

    if "wte" in key:
        continue
    if key.startswith("transformer"): 
        if key.endswith("weight"):

            weight = model[key].float()
            
            rank = torch.linalg.matrix_rank(weight)
            _, S, _ = torch.linalg.svd(weight)
            layer_number = int(key.split('.')[2])
            if layer_number not in layer_numbers: 
                layer_numbers.append(layer_number)
            if "attn" in key:
                if "c_attn" in key:
                    attn_list_sum.append(torch.sum(S).item())
                    attn_list_g5.append((S > threshold).sum().item())
                else:
                    c_proj_list_sum.append(torch.sum(S).item())
                    c_proj_list_g5.append((S > threshold).sum().item())
            else:
                if "c_fc1" in key:
                    mlp_c_fc1_list_sum.append(torch.sum(S).item())
                    mlp_c_fc1_list_g5.append((S > threshold).sum().item())
                elif "c_fc2" in key:
                    mlp_c_fc2_list_sum.append(torch.sum(S).item())
                    mlp_c_fc2_list_g5.append((S > threshold).sum().item())
                else:
                    mlp_c_proj_list_sum.append(torch.sum(S).item())
                    mlp_c_proj_list_g5.append((S > threshold).sum().item())
                
# Create a figure with subplots
plt = AcademicPlot(nrows=2,ncols=5, figsize=(25, 10),fontsize=7)

# Plotting the sum of singular values for each component
plt.axs[0, 0].plot(layer_numbers, attn_list_sum, marker='o')
plt.axs[0, 0].set_title("Sum of Singular Values (attn)")
plt.axs[0, 1].plot(layer_numbers, c_proj_list_sum, marker='o')
plt.axs[0, 1].set_title("Sum of Singular Values (c_proj)")
plt.axs[0, 2].plot(layer_numbers, mlp_c_fc1_list_sum, marker='o')
plt.axs[0, 2].set_title("Sum of Singular Values (mlp_c_fc1)")
plt.axs[0, 3].plot(layer_numbers, mlp_c_fc2_list_sum, marker='o')
plt.axs[0, 3].set_title("Sum of Singular Values (mlp_c_fc2)")
plt.axs[0, 4].plot(layer_numbers, mlp_c_proj_list_sum, marker='o')
plt.axs[0, 4].set_title("Sum of Singular Values (mlp_c_proj)")

# Plotting the count of singular values > 5 for each component
plt.axs[1, 0].plot(layer_numbers, attn_list_g5, marker='o')
plt.axs[1, 0].set_title("Count of Singular Values > 5 (attn)")
plt.axs[1, 1].plot(layer_numbers, c_proj_list_g5, marker='o')
plt.axs[1, 1].set_title("Count of Singular Values > 5 (c_proj)")
plt.axs[1, 2].plot(layer_numbers, mlp_c_fc1_list_g5, marker='o')
plt.axs[1, 2].set_title("Count of Singular Values > 5 (mlp_c_fc1)")
plt.axs[1, 3].plot(layer_numbers, mlp_c_fc2_list_g5, marker='o')
plt.axs[1, 3].set_title("Count of Singular Values > 5 (mlp_c_fc2)")
plt.axs[1, 4].plot(layer_numbers, mlp_c_proj_list_g5, marker='o')
plt.axs[1, 4].set_title("Count of Singular Values > 5 (mlp_c_proj)")

# Setting labels for axes
for ax in plt.axs.flat:
    ax.set(xlabel='Layer Number', ylabel='Value')

# Adjust layout
plt.savefig('test.png')
plt.show()