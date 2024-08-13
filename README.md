# Example of a mamba 2 model

`Why did it have to be snakes?`

This is an example of a mamba 2 llm that works with CPU or GPU.

## Dependencies
The model will work on cpu, but is a little slow. The linear version of the model (mamba 1) is much easier to run on cpu, but not as good.

If you have cuda:
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

If you don't have cuda:
```
pip install torch torchvision torchaudio
```


## Train

Train the model with the command:

```
python train.py
```

NOTE: the current training settings way over-fit, but I needed to ensure training works. If I was using a much larger
training set, I would tweak my training values.

Example training:
![img_1.png](img_1.png)

## Run

Run the model with the command:

```
python run.py
```

This enters a cli mode where you give text, and it completes the text. Nothing fancy.

Example usage:
![img.png](img.png)

## Related Details

Mamba 2 paper: https://arxiv.org/pdf/2405.21060
HiPPO initialization paper: https://arxiv.org/pdf/2206.12037
Blog on Mamba 2:

* https://tridao.me/blog/2024/mamba2-part1-model/
* https://tridao.me/blog/2024/mamba2-part2-theory/
* https://tridao.me/blog/2024/mamba2-part3-algorithm/
* https://tridao.me/blog/2024/mamba2-part4-systems/