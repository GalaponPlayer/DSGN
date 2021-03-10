import numpy as np
import matplotlib.pyplot as plt
import subprocess
import fire

def easy_AP(AP):
    return AP[1]

def moderate_AP(AP):
    return AP[2]

def hard_AP(AP):
    return AP[3]

def find_best_epoch(model_dir, start, end, step):
    APs = []
    for epoch in np.arange(start, end, step):
        with open(model_dir + "/" + "result_kitti_finetune_{}.txt".format(epoch)) as f:
            for line in f:
                slist = line.split(" ")
                if slist[0] == "3d":
                    easy = float(slist[3].replace("AP:", "").replace(",",""))
                    moderate = float(slist[4].replace(",", ""))
                    hard = float(slist[5].replace("\n", ""))
                    break
        APs.append((epoch, easy, moderate, hard))
    
    print('-----APs-----')
    for i in range(0, len(APs)):
        print(APs[i])
    
    max_AP_easy = max(APs, key=easy_AP)
    max_AP_moderate = max(APs, key=moderate_AP)
    max_AP_hard = max(APs, key=hard_AP)
    print('-----MAX EASY-----')
    print('EPOCH:{}  3DAP:{}'.format(max_AP_easy[0], max_AP_easy[1]))
    print('-----MAX MODERATE-----')
    print('EPOCH:{}  3DAP:{}'.format(max_AP_moderate[0], max_AP_moderate[2]))
    print('-----MAX HARD-----')
    print('EPOCH:{}  3DAP:{}'.format(max_AP_hard[0], max_AP_hard[3]))

    vis_APs(APs)

def vis_APs(APs):
    epochs = [ap[0] for ap in APs]
    AP_easy = [ap[1] for ap in APs]
    AP_moderate = [ap[2] for ap in APs]
    AP_hard = [ap[3] for ap in APs]

    plt.ylim(5, 30)
    plt.xlabel('EPOCHS')
    plt.ylabel('3D AP')

    plt.axhline(y=26.97, linestyle='dashed', color='green')
    plt.axhline(y=21.71, linestyle='dashed', color='blue')
    plt.axhline(y=18.22, linestyle='dashed', color='red')

    plt.plot(epochs, AP_easy, color='green')
    plt.plot(epochs, AP_moderate, color='blue')
    plt.plot(epochs, AP_hard, color='red')

    plt.savefig('./AP_visualization.png')
    arguments = ['display', './AP_visualization.png']
    subprocess.call(arguments)

if __name__=='__main__':
    fire.Fire(find_best_epoch)