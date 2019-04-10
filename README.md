# Temporal Relation Networks

See Temporal Relation Networks](http://relation.csail.mit.edu/), built on top of the [TSN-pytorch codebase](https://github.com/yjxiong/temporal-segment-networks).


## How to use
Run fps_dem_trn.py




### Reference:
B. Zhou, A. Andonian, and A. Torralba. Temporal Relational Reasoning in Videos. European Conference on Computer Vision (ECCV), 2018. [PDF](https://arxiv.org/pdf/1711.08496.pdf)
```
@article{zhou2017temporalrelation,
    title = {Temporal Relational Reasoning in Videos},
    author = {Zhou, Bolei and Andonian, Alex and Oliva, Aude and Torralba, Antonio},
    journal={European Conference on Computer Vision},
    year={2018}
}
```

### Acknowledgement
Our temporal relation network is plug-and-play on top of the [TSN-Pytorch](https://github.com/yjxiong/temporal-segment-networks), but it could be extended to other network architectures easily. We thank Yuanjun Xiong for releasing TSN-Pytorch codebase. Something-something dataset and Jester dataset are from [TwentyBN](https://www.twentybn.com/), we really appreciate their effort to build such nice video datasets. Please refer to [their dataset website](https://www.twentybn.com/datasets/something-something) for the proper usage of the data.
