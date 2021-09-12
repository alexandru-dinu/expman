from torch.utils.data import DataLoader, Dataset
from torch.utils.data._utils.collate import default_collate


class CustomDataset(Dataset):
    def __init__(self, *args, **kwargs):
        # data init
        ...

    def __getitem__(self, i):
        try:
            # unreliable data source
            # processing
            ...
            return self.data[i]
        except (FileNotFoundError, ...):
            return None

    def __len__(self):
        return len(self.data)

    @staticmethod
    def collate(xs):
        good = [x for x in xs if x is not None]

        if len(good) == 0:
            return None

        return default_collate(good)


dataset = CustomDataset(...)
dataloader = DataLoader(dataset, collate_fn=CustomDataset.collate)


for idx, batch in enumerate(dataloader):
    if batch is None:
        continue
    # unpack batch
    x, y, z = batch
    ...
