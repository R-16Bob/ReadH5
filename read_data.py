import h5py
def read_data(file_path):
    '''
    :param file_path:
    :return: loss_list,acc_list
    '''
    with h5py.File(file_path, 'r') as f:
        keys=list(f.keys())
        print(keys)
        acc_data=f[keys[0]]
        loss_data=f[keys[2]]
        # print(loss_data,acc_data)
        acc_list = acc_data[()]
        loss_list = loss_data[()]
        return loss_list,acc_list

if __name__ == '__main__':
    file_dir = '24-5-31/'
    file_name = 'cifar10_FedAvg_cl100_dir.h5'
    loss_list,acc_list=read_data('data/' + file_dir + file_name)
    print(loss_list)
    print(acc_list)