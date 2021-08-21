# -*- coding utf-8 -*-

'''
*--------------------------------- BasicIO.py ---------------------------------*
对 HDF5 文件进行读取与写入的操作。

4dExplorer 软件默认使用 HDF5 进行四维数据及其元数据的管理。对于其他格式的文件，例如由
EMPAD 所产生的数据，4dExplorer 将其转换为hdf5进行管理并生成临时文件，用户可自行决定是
否要保存该临时文件为 HDF5 数据集。出于对内存空间资源节约的考虑，所有有关四维数据的计算
都是基于硬盘 IO 的，而在代码层面上不会将数据一次性全部读入内存中(尽管操作系统会尝试这样
做，但即使是内存空间不足，也无需担心会对性能造成影响。)

这样，对于由仪器采集而来的数据，使用 4dExplorer 软件进行数据读取的步骤就是：
     - 在某个文件夹内创建临时 HDF5 数据文件，该文件的主要部分是原四维数据的副本；
     - 根据 HDF5 的特性进行内存映射；
     - 校正与分析，结果都将存储于 HDF5 文件中；
     - 输出分析结果；
     - 保存或删除 HDF5 文件。

在这样的工作流程中，将四维数据复制一份的时间代价较大。为节约后续分析的时间，可以保存 HDF5 
文件，后续重新打开该数据集时可直接建立内存映射，省下加载四维数据的时间开销。在后续打开时，
就将直接调用 BasicIO.py 中的代码。


作者：          胡一鸣
创建时间：      2021年8月21日

Basic IO operation of HDF5 files.

By default, the 4dExplorer software uses HDF5 to manage 4d data and metadata. 
For other files, such as the data generated by EMPAD, 4dExplorer converts them 
to HDF5 for management and generates temporary files. Users can decide whether 
to save the temporary files as HDF5 data sets or not. In order to save memory 
resources, all computation of the four-dimensional data is based on disk IO, a-
nd the data is not read into memory all at once at the code level (although the 
operating system will try to do this, there is no need to worry about the perf-
ormance impact of running out of memory).

In this way, for the data collected by the specific instrument, the steps of u-
sing 4dExplorer software to read the data are as follows:
      - Create a temporary HDF5 data file in some folder, the main part of whi-
        ch is a copy of the original 4-dimensional data;
      - Memory mapping based on HDF5 features;
      - Calibration and analysis, the results will be stored in the HDF5 file;
      - Output the analysis result;
      - save or delete the HDF5 file.

In such a workflow, the time cost of making a copy of the four-dimensional data 
is large. In order to save the time of subsequent analysis, the HDF5 file can 
be saved, and the memory mapping can be directly established when the data set 
is reopened, saving the time cost of loading the four-dimensional data. On sub-
sequent opens, the code in basicio.py is called directly.

author:             Hu Yiming
date:               Aug 21, 2021

All rights reserved.
                                                                               

*--------------------------------- BasicIO.py ---------------------------------*
'''


class DataUtil(object):
     pass

