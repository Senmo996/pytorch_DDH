#选择需要的dataset
DATASET_NAME = 'youtubeface'
# DATASET_NAME = 'facescrub'

if DATASET_NAME == 'youtubeface':
	TRAIN_SET_PATH = 'data/youtubeface_train_set'
	TEST_SET_PATH = 'data/youtubeface_test_set'
	NB_CLASSES = 1595
else:
    TRAIN_SET_PATH = 'data/facescrub_train_set'
    TEST_SET_PATH = 'data/facescrub_test_set'
    NB_CLASSES = 530

WEIGHTS_SAVE_PATH = 'weights'
WEIGHTS_FILE_NAME = 'best/weights/dir/to/load'

NB_EPOCHS = 200
HASH_NUM = 48
SPLIT_NUM = 4
TOP_K = 50
IMAGE_WIDTH = 32
IMAGE_HEIGHT = 32
LOSS_01_LAYER_PARAMS = 0.01
REGULARIZER_PARAMS = 0.0001
