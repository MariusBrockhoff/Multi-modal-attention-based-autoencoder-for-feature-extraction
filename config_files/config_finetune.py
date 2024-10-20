# TODO: split original DEC config file (and IDEC, etc accordingly) into pretrain/model config files and finetune config files

class Config_Finetuning(object):

    def __init__(self, data_path, model_type):
        super(Config_Finetuning, self).__init__()

        self.data_path = data_path
        self.MODEL_TYPE = model_type
        self.FILE_NAME = self.data_path.rpartition('/')[-1][:-4]

        # Load Pretrained Model

        self.PRETRAINED_SAVE_DIR = "C:/Users/marib/Documents/Github/ML_Spike_Sorting/trained_models/" + "Pretrain_NNCLR_" + self.MODEL_TYPE + "_" + self.FILE_NAME + ".h5"

        #"/rds/user/mb2315/hpc-work/Data/Saved_Models/" + "Pretrain_NNCLR_" + self.MODEL_TYPE + "_" + self.FILE_NAME + ".h5")
        
        #"/rds/user/mb2315/hpc-work/Data/Saved_Models/" + "DensityPseudoLabel_NNCLR_" + self.MODEL_TYPE + "_" + self.FILE_NAME + ".h5"

        #"/rds/user/mb2315/hpc-work/Data/Saved_Models/" + "Pretrain_" + self.MODEL_TYPE + "_" + self.FILE_NAME + ".h5"
        
        #"C:/Users/marib/Documents/Github/ML_Spike_Sorting/trained_models/" + "Pretrain_" + self.MODEL_TYPE + "_" + self.FILE_NAME + ".h5"

        # DEC

        self.DEC_N_CLUSTERS = 5

        self.DEC_BATCH_SIZE = 256

        self.DEC_LEARNING_RATE = 0.01

        self.DEC_MOMENTUM = 0.9

        self.DEC_TOL = 0.001

        self.DEC_MAXITER = 8000

        self.DEC_UPDATE_INTERVAL = 140

        self.DEC_SAVE_DIR = "/rds/user/mb2315/hpc-work/Data/Saved_Models/" + "DEC_" + self.MODEL_TYPE + "_" + self.FILE_NAME + ".h5"

        # IDEC

        self.IDEC_N_CLUSTERS = 5

        self.IDEC_BATCH_SIZE = 256

        self.IDEC_LEARNING_RATE = 0.1

        self.IDEC_MOMENTUM = 0.99

        self.IDEC_GAMMA = 0.1

        self.IDEC_TOL = 0.001

        self.IDEC_MAXITER = 20000

        self.IDEC_UPDATE_INTERVAL = 140

        self.IDEC_SAVE_DIR = "/rds/user/mb2315/hpc-work/Data/Saved_Models/" + "IDEC_" + self.MODEL_TYPE + "_" + self.FILE_NAME + ".h5"

        # PseudoLabels

        self.PSEUDO_N_CLUSTERS = None

        self.PSEUDO_LABEL_RATIO = None

        self.ITERATIVE_RATIOS = [0.01, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4] #0.01, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4

        self.SAMPLING_METHOD = "weighted"

        self.DENSITY_FUNCTION = "mean"

        self.K_NEAREST_NEIGHBOURS = 0.005 #relative of number of spikes

        self.PSEUDO_EPOCHS = 50

        self.PSEUDO_BATCH_SIZE = 128

        self.CLASSIFICATION_AUGMENTER = {"apply_noise": True,
                                    "max_noise_lvl": 0.1,
                                    "scale": (1.0, 1.0),
                                    "name": "classification_augmenter"}

        self.PSEUDO_SAVE_DIR = "C:/Users/marib/Documents/Github/ML_Spike_Sorting/trained_models/" + "DensityPseudoLabel_" + self.MODEL_TYPE + "_" + self.FILE_NAME + ".h5"




            #"C:/Users/marib/Documents/Github/ML_Spike_Sorting/trained_models/" + "DensityPseudoLabel_" + self.MODEL_TYPE + "_" + self.FILE_NAME + ".h5"


            #"/rds/user/mb2315/hpc-work/Data/Saved_Models/" + "Pretrain_" + self.MODEL_TYPE + "_" + self.FILE_NAME + ".h5"