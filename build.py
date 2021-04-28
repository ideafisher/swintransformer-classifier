import torchvision
import torchvision.transforms as tf
from torch.utils.data import DataLoader
from timm.data import create_transform


def build_loader(cfg):
    if cfg.DATA.DATASET == 'cifar10':
        transform = []
        for tf_key in cfg.AUG:
            if type(cfg.AUG[tf_key]) is int:
                transform.append(eval('tf.' + tf_key + '(' + str(cfg.AUG[tf_key]) + ')'))
            elif type(cfg.AUG[tf_key]) is str:
                transform.append(eval('tf.' + tf_key + '(' + cfg.AUG[tf_key] + ')'))
            else:
                raise Exception('Unsupported augmentation type')
        transform = tf.Compose(
            transform.extend([
                tf.ToTensor(),tf.Normalize((0.49, 0.48, 0.45), (0.25, 0.24, 0.26))
                ])
            )
        dataset = torchvision.datasets.CIFAR10(root=cfg.DATA.DATA_PATH,
                                               train=(not cfg.EVAL_MODE),
                                               download=True,
                                               transform=transform)
        dataloader = DataLoader(dataset, )