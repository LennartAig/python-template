from pathlib import Path
import random


class example_dataset:

    def __init__(self, img_dir: str = './'):
        self.img_dir = img_dir
        self.annotations = ['test1', 'test2', 'test3']

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, i: int):
        return self.annotations[i]


def example_dataloader(dataset: example_dataset, random_order: bool = False):
    return_idxs = random.sample(range(len(dataset)), len(dataset)) if random_order else range(
        len(dataset))
    for i in return_idxs:
        yield dataset[i]


if __name__ == "__main__":
    dataset = example_dataset()
    dataloader = example_dataloader(dataset, random_order=True)
    for data in dataloader:
        print(data)