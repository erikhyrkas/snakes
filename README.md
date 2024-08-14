# Example of a mamba 2 model

`Why did it have to be snakes?`

This LLM is based on my understanding of Mamba 2 and works with CPU or GPU.

## Dependencies
The model will work on cpu, but is a little slow. 

If you have cuda:
```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

If you don't have cuda:
```
pip install torch torchvision torchaudio
```

## Generate Data

I used ollama with llama 3.1 to generate training data. Because I don't have a fancy streaming training setup, we are constrained by training data that fits into memory. Fortunately for me, I can fit a lot into memory.

You can generate additional data using the command:
```
pip install ollama

python data_generator.py
```

## Train

Depending on how much GPU you have or whether you are using a CPU, you might want to tweak the context length to fit your hardware. Also, you might simply not want to wait for the time it takes to train a 768 token context.

I documented the memory I *observed* being used for a number of settings. Without any model running, I'll often see around 0.6 GB of GPU used. Your vocabulary size will impact this, if you change the tokenizer. I didn't make an effort to be ultimately efficient. Your milage may vary if you have a smaller or larger vocabulary.

I tested a lot with a context size of 20, and it worked surprisingly well. It runs well even if you have a CPU.

If you are looking to just quickly try out the model without needing it to do much, I'd suggest a batch size of 20 and using a limited number of documents to keep your vocab down.

I could have tweaked batch size to utilize less memory, but once I had stable training, I was nervous about toying with it.

Context size and batch size can be changed at the bottom of `train.py`. Vocabulary size depends directly on the documents in `.\training_data\`.  

### Observed GPU Used

| Memory Used | Context Size | Batch Size | Vocabulary Size |
|-------------|--------------|------------|-----------------|
| 1.6 GB      | 5            | 64         | 13,148          |
| 2.0 GB      | 20           | 64         | 13,148          | 
| 5.0 GB      | 128          | 64         | 13,148          |
| 9.1 GB      | 256          | 64         | 13,148          |
| 12.8 GB     | 368          | 64         | 13,148          |
| 17.4 GB     | 512          | 64         | 13,148          |
| 22.5 GB     | 768          | 64         | 13,148          |



Train the model with the command:

```
python train.py
```

NOTE: the current early-stopping settings way over-fit, but I needed to ensure training works. If I was using a much larger
training set, I would tweak my early stopping values. Overfitting means that the results are coherent, but that the model isn't versatile. It's effectively memorizing the trianing data.

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
