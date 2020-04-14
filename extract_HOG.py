import lib.collecting_img as ci

pos_path = 'pd'
neg_path = 'nd'

ex_flag = input("1:positive 0:negitive \n")

if(ex_flag == '1'):
    ci.collecting_hog(pos_path,'HOG_data/PHOG.txt')
elif(ex_flag == '0'):
    ci.collecting_hog(neg_path,'HOG_data/NHOG.txt')

