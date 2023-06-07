import numpy as np
import os
import scipy.io as scio

raw_folder = './WiFi Human-to-Human Interactions Dataset'

filelist = []
for dirpath, dirnames, filenames in os.walk(raw_folder):
    for filename in filenames:
        filelist.append(os.path.join(dirpath, filename))


csi_dataset = []
csi_labels = []
is1 = 0
for file in filelist:
    print(file)
    is1 += 1
    csi = scio.loadmat(file)['Raw_Cell_Matrix']
    csi_data = []
    csi_label = []
    length = len(csi)
    num = np.linspace(0, length - 1, 1000).astype(int)
    for i in range(length):
        csi_data.append(abs(csi[i][0]['CSI'][0][0]).reshape(180,-1))
        csi_label.append(int(csi[i][0]['label'][0][0][-1][1:]))
    csi_dataset.append(np.squeeze(np.array(csi_data)[num]))
    csi_labels.append(min(csi_label))

    np.savez_compressed("csi_data_{}.npz".format(is1 / 600), csi_dataset)
    np.savez_compressed("csi_label_{}.npz".format(is1 / 600), csi_labels)






