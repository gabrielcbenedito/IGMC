# Dockerfile structure

- install apt dependencies
- install miniconda
- install python
- install pytorch
  - Prerequisites
    - glic >= v2.17
    - Ubuntu >= 13.04
    - Python >= 3.6
    - anaconda or pip
  - CUDA 9.2
    - conda install pytorch==1.4.0 torchvision==0.5.0 cudatoolkit=9.2 -c pytorch
  - CUDA 10.1
    - conda install pytorch==1.4.0 torchvision==0.5.0 cudatoolkit=10.1 -c pytorch
  - CPU Only
    - conda install pytorch==1.4.0 torchvision==0.5.0 cpuonly -c pytorch
- install pytorch geometric
