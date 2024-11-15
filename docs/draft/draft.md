# 4D-Explorer

4D-Explorer 是一款用于分析四维扫描透射电子显微镜 (4D-STEM) 数据的软件。它可以导入、存储 4D-STEM 数据集及其元数据，校正，并生成在实空间中的重构像。关于 4D-STEM 技术，见综述文章 [Colin Ophus, 2019](https://www.cambridge.org/core/journals/microscopy-and-microanalysis/article/fourdimensional-scanning-transmission-electron-microscopy-4dstem-from-scanning-nanodiffraction-to-ptychography-and-beyond/A7E922A2C5BFD7FD3F208C537B872B7A)

# 安装方法
## 可执行文件安装

在仓库的发布 (Release) 页面，根据操作系统下载包含可执行文件的压缩包。目前仅支持 Windows 及 MacOS。若您使用的是 Linux，请使用 PyPI 安装。下载好压缩包后解压，找到 4D-Explorer.exe 即可运行。

## 使用 PyPI 安装 

推荐使用 Anaconda 来设置 python 的虚拟环境，要求使用 python 3.10 版本：

```
conda update conda
conda create -n FourDExplorerVenv python==3.10
```

创建好名为 FourDExplorerVenv 的虚拟环境后，激活该虚拟环境，然后使用 pip 安装 4D-Explorer：

```
conda activate FourDExplorerVenv
(FourDExplorerVenv) pip install --upgrade FourDExplorer
```

安装好后，启动 python，进入交互式窗口后，输入以下命令启动软件：
``` 
(FourDExplorerVenv) python 
>>> from FourDExplorer import FourDExplorer
>>> FourDExplorer.run()
```

# 测试数据 

我们提供三套测试数据，分别为 gold_nanoparticle_06, gold_nanoparticle_07 和 MoS2_14。三套测试数据的下载地址如下
- [Google Drive: 4D-Explorer Test Dataset](https://drive.google.com/drive/folders/1WaYyQNulZCERJQuW2GMvka0N5DNRpCFz?usp=sharing)
- [百度网盘: 4D-Explorer Test Dataset, 提取码: 64s2](https://pan.baidu.com/s/16G6rZUK95fogkg_GFg14hQ?pwd=64s2)

这三套数据集的参数如下：

## gold_nanoparticle_06

- 扫描点数目：256 x 256 
- 衍射图像尺寸: 128 x 128
- 采集电镜型号: Thermofisher FEI Titan G2 60-300
- 电子相机型号: Thermofisher EMPAD
- 加速电压 (U): 60 kV
- 相机长度 (CL): 576.6 mm 
- 会聚半角 ($\alpha$): 22.5 mrad
- 扫描步长: 1.80 nm
- 离焦量: 正焦
- 备注: 这套数据集是在正焦拍摄下的金纳米颗粒，嵌于 DNA 上。其在采集时预先设置了 30° 的扫描旋转角度，并且具有一定的衍射漂移幅度。这套数据集可以用来演示通过计算 CoM 的旋度的方法来进行扫描旋转校正 (Rotational Offset Correction)，并且通过 FDDNet 来测量各个衍射盘的偏移量以进行衍射漂移合轴校正 (Diffraction Shift Alignment) 的过程。 

> 在 Google Drive 中，这套数据集被分为了多个压缩文件，以 .z01, .z02 等结尾。需要下载全部的压缩文件，然后才能正确解压。

## gold_nanoparticle_07

- 扫描点数目: 128 x 128 
- 衍射图像尺寸: 128 x 128
- 采集电镜型号: Thermofisher FEI Titan G2 60-300
- 电子相机型号: Thermofisher EMPAD
- 加速电压 (U): 60 kV
- 相机长度 (CL): 576.6 mm
- 会聚半角 ($\alpha$): 22.5 mrad
- 扫描步长: 1.31 nm
- 离焦量: -2.11 μm (欠焦)
- 备注: 这套数据集是在欠焦条件下拍摄的金纳米颗粒，嵌于 DNA 上。在这套数据集的每张衍射图像中，可以看见金颗粒的形貌 (即实空间的信息)。其在采集时，通过调节样品台高度来实现欠焦，从而保持了和 gold_particle_06 相同的扫描旋转角度。该数据集适合于演示通过离焦近轴明场像 (Axial BF) 来进行扫描旋转校正的过程。

## MoS2_14

- 扫描点数目: 128 x 128
- 衍射图像尺寸: 128 x 128
- 采集电镜型号: Thermofisher FEI Titan G2 60-300
- 电子相机型号: Thermofisher EMPAD
- 加速电压 (U): 60 kV
- 相机长度 (CL): 286.3 mm
- 会聚半角 ($\alpha$): 22.5 mrad 
- 扫描步长: 0.029 nm
- 离焦量: 正焦
- 备注: 这套数据集是二维材料二硫化钼的原子级别成像，适合于演示不同的重构方法所带来的不同效果。

# 快速上手 

![Main Window](/docs/fig/InitWindow.png)

## 数据管理 

4D-Explorer 基于 [HDF5](https://www.hdfgroup.org/solutions/hdf5/) 文件格式。HDF5 文件由群组 (Groups) 和数据集 (Datasets) 组成，类似于电脑操作系统中的文件夹和文件。群组可以包含其他群组和数据集，形成一个层次结构，便于组织和管理复杂的数据。

要创建一个新的 HDF5 文件，请在主界面的左上角打开 'File' 菜单，然后按下 'New HDF5 File' 按钮，即可打开选择创建 HDF5 文件的名字以及存放路径的对话框。我们将新建的 HDF5 名字设为 4D-Explorer-test-dataset.h5。之后，会自动弹出选择 HDF5 文件的对话框，此时选择刚刚创建的新 HDF5 文件即可打开。

![Create a New File](/docs/fig/CreateH5.png)

在新创建的 HDF5 文件中空无一物，因而在左边控制面板的 File 栏里，只有一个 4D-Explorer-test-dataset.h5 的项，表示刚刚新建的 HDF5 文件。我们先创建一个群组，以放置我们将要导入的数据集。要创建群组，在左边的面板中，右击 4D-Explorer-test-dataset.h5，在弹出的菜单中选择 'New' (带有 + 号的图标)。

![Create a New Group 1](/docs/fig/NewGroup.png)

在打开的创建项 (Create Item) 对话框中，有三个需要填写的地方：
- Location，也就是需要把群组创建在哪个群组下面。默认是 '/'，熟悉 Unix/Linux 的同学应该知道这表示根目录，而在 HDF5 文件中这也表示我们正在创建的项在根目录下，而不隶属于任何群组。点击 Browse... 按钮可以浏览并选择群组，从而把新创建的项放进这个群组中。不过，目前我们的 h5 文件中还没有任何群组，所以只能选择根目录。
- Name，也就是新建群组的名字。默认是 untitled，这里我们把它改成我们想要的名字，比如 gold_nanoparticle。
- Type，这里选 Group，也就是我们需要创建的是群组，而不是数据集 (Dataset)。

![Create a New Group 2](/docs/fig/NewGroup2.png)

如果一切顺利的话，这时在左边控制面板的 File 栏里，应该能看到 4D-Explorer-test-dataset.h5 下面多挂了一个 gold_nanoparticle_06，并且图标是文件夹的项了。这就是我们刚刚创建的群组。

我们提供了三套测试数据集，因此在这里分别创建三个群组，并命名为 gold_nanoparticle_06、gold_nanoparticle_07 以及 MoS2_14

鼠标右击群组，可以看到和刚刚差不多的菜单，里面有对一个群组可以进行的操作，包括：
- 'New' 在该群组下新建一个群组或者数据集。
- 'Import 4D-STEM dataset' 在该群组下导入一个 4D-STEM 数据集
- 'Move/Copy/Rename/Delete' 编辑这个群组(移动、复制、重命名、删除).
- 'Attributes' 查看这个群组的属性.

可以随意增删查改这些群组，只要注意有些操作是不可逆的。

> 在删除某个东西的时候，永远要小心。

## 导入 4D-STEM 数据集 
现在假如说我们已经有了一个二进制的 4D-STEM 数据集文件 (raw 文件) 想要导入到 HDF5 中。选好一个群组 (也可以点到根目录上)，右键，点击 'Import 4D-STEM Dataset'，这就打开了加载 4D-STEM 数据集的对话框。

![Group Context Menu](/docs/fig/Import4DSTEM.png)

对于所提供的测试数据集，选择 'EMPAD v0.51 (for NJU)'，然后点 'browse' 按钮选择我们要导入的 EMPAD 文件 (应当选择数据集文件夹中的 .xml 文件)。

![Import 4D-STEM Dataset](/docs/fig/ImportEMPAD.png)

然后，给我们要导入的数据集起一个名字叫 'gold_nanoparticle_06'。最后，点 OK 按钮。

根据同样的步骤，依次在三个群组中导入测试数据集，并给予其相应的名字。

## 执行任务 
在我们加载数据集的时候，可以在左侧控制面板中的 'Task' 栏中查看进度、任务细节以及历史任务。

![Task Manager](/docs/fig/TaskManager.png)

## 数据集的扩展名
现在我们可以在控制面板中的 'File' 栏里看到一个新的项 'gold_nanoparticle_06.4dstem'，就是我们刚刚导入的 4D-STEM 数据集。它有自己的图标和扩展名 '.4dstem'，4D-Explorer 就是通过这些扩展名来识别数据集的用途的。当然，扩展名不是必须的，就像我们平时在操作系统中识别文件一样。目前 4D-Explorer 可以识别这几种扩展名：
- .4dstem : 4D-STEM 数据集，必须是 4 维数组
- .img : 灰度图像，必须是 2 维数组。不支持 RGB 彩色图像或其他多通道图像。
- .vec : 二维矢量场，具有两个分量。每个分量各自是一张灰度图像。
- .line : 一条线，必须是 1 维的。

## 查看 4D-STEM 数据集 
右键点击 gold_nanoparticle_06.4dstem 数据集，即可打开该数据集的菜单，选择第一个 Open 即可打开。我们可以看到右边打开了一个页面。

![View 4D-STEM Dataset](/docs/fig/Open4DSTEM.png)

> 提示：你可以拖动各个组件之间的边界，免得某些区域太小而显示得不好。也可以再按下最左侧的控制面板按钮，即可隐藏左侧的面板。

页面里面有两个图像，其中中间的是衍射图样，右边的是实空间的重构像。由于我们现在还没有重构，所以右边啥也没有，但我们还是可以点击右边的图像，这样游标就会跟随鼠标移动，左边就会显示不同位置的衍射斑。

## 重构
现在我们赶紧重构一个看看效果。在左侧找到 gold_nanoparticle_06.4dstem 数据集，点右键，然后找到 'Reconstruction' 菜单，选 'Virtual Image'。现在，右边打开了一个新的页面，用于选定 Virtual Image 的参数。现在，我们先重构一个环形暗场像 (ADF) 试试。

![Set Annular Dark Field Region](/docs/fig/SetReconstructionRegion.png)

在这里我们选择环 (Ring) 作为积分区域，然后设置内径为 45 像素，外径为 60 像素。对于积分区域的位置，设置水平偏移为 2，垂直偏移为 -1。选好参数后，点最下面 'START CALCULATION' 那个红色按钮。然后一个新的对话框就会问在哪里存储重构的图像。

> 假如说你没有看到红色的按钮，可以试试把最右边的滚动条往下拉。

![Start Computing ADF](/docs/fig/StartComputingADF.png)

都准备好后就开始计算，和之前加载数据集的时候一样，这种长时间的任务都可以在左边的 'Task' 栏里查看细节。等计算好之后，可以像之前打开 4D-STEM 一样，右键点击 ADF.img，在菜单中选择 'Open'，即可打开查看图像的页面。

![View ADF](/docs/fig/ViewADF.png)

## 使用重构像作为预览

现在我们终于有了一个重构像，可以回到刚才的 4D-STEM 查看的页面了。我们可以点击 'BROWSE PREVIEW' 按钮，然后选刚才我们创建的重构像。

![Browse Prevew](/docs/fig/BrowsePreview.png)

之后，我们就可以在4维相空间里探索该 4D-STEM 数据集了。

> 你可能注意到 gold_nanoparticle_06 群组下多了一个 gold_nanoparticle_06_preview.img 的图像。那是一个空的图像，起到占位作用。现在我们已经将预览图像设置为我们重构的图像了，因此可以删掉这个空的图像。


# 文件与数据操作 

4D-Explorer 以 HDF5 文件为基础，推荐的使用方式是新建立一个 HDF5 文件，然后将本次数据处理所需的数据均放置该 HDF5 文件中。

## HDF5 文件与数据的组织方式

HDF5 (Hierarchical Data Format version 5) 是一种用于存储和组织大量数据的文件格式。它支持复杂的数据结构，包括群组 (Group)、数据集 (Dataset) 以及元数据 (Metadata)，这些结构使得 HDF5 成为科学数据存储的理想选择。

群组 (Group) 是 HDF5 文件中的一个容器，类似于文件系统中的目录。群组可以包含其他群组和数据集。通过使用群组，可以组织和管理复杂的层次结构数据。例如，一个群组可以表示一个实验，而该群组下的子群组可以表示不同的数据集或处理步骤。

数据集 (Dataset) 是 HDF5 文件中存储实际数据的对象。它类似于数组或表格，可以存储多维数据。数据集可以包含任意类型的数据，包括整数、浮点数、字符串等。数据集的维度可以是任意的，从一维到多维都可以。例如，一个 4D-STEM 数据集可以存储为一个四维的 Dataset。

> 在文档中，"数据集 (Dataset)" 和 "4D-STEM 数据集" 指代的物体可能并不相同，请注意根据上下文进行区分。

元数据 (Metadata) 是关于数据的数据，用于描述数据集或群组的属性。元数据可以包含诸如数据集的名称、单位、创建时间、作者等信息。元数据以键值对的形式存储，键是字符串，值可以是任意类型的数据。元数据的使用使得数据的描述和解释更加方便，特别是在科学数据分析中。

使用 HDF5 的好处包括：
- HDF5 支持复杂的层次结构，可以轻松组织和管理大量数据。
- HDF5 使用压缩和分块技术，可以高效地存储和访问大数据集。
- HDF5 文件格式是跨平台的，可以在不同的操作系统和硬件上使用。
- 通过 metadata，可以详细描述数据的属性和背景信息，便于数据的管理和解释。
- 通过延迟读取的方式，降低内存需求。笔记本上也能轻松处理 100 GB 的数据集。
- 与许多开源 4D-STEM 处理软件兼容。
- 方便使用 python、MATLAB 等语言对数据进行进一步处理。

4D-Explorer 默认使用 HDF5 文件来保存数据。在开始任何操作之前，应当先选定一个 HDF5 文件作为存放数据的容器。如果没有 HDF5 文件，则需要创建。要创建一个新的 HDF5 文件，请在主界面的左上角打开 'File' 菜单，然后按下 'New HDF5 File' 按钮，即可选择需要将文件存放在系统的哪个目录之下，并选择文件的名字。之后，会自动弹出选择 HDF5 文件的对话框，此时选择刚刚创建的新 HDF5 文件即可打开该文件。

要想打开已有的 HDF5 文件，请在主界面的左上角打开文件 (File) 菜单，然后选择打开 HDF5 文件 (Open HDF5 File)。之后，即可选择需要打开的 HDF5 文件。

已打开的 HDF5 文件不能通过其他进程 (包括另一个 4D-Explorer 进程或用户编写的脚本) 再次打开。若希望能在其他软件或脚本中打开该文件，需要在当前 4D-Explorer 中关闭该 HDF5 文件。为此，在主界面的左上角打开文件 (File) 菜单，然后选择关闭文件 (Close File) 即可。此时，左侧的 HDF5 文件列表会变回空白。注意，请勿在计算任务进行的途中关闭文件，这通常会导致计算任务的失败。

HDF5 文件中，每个群组和数据集都有自己的名字。在 4D-Explorer 中，会将各个群组和数据集按照树状的形式进行展示，主要的展示界面位于左边控制面板中的文件面板。对于数据集，4D-Explorer 会识别以点号 "." 分割的扩展名，以识别该数据集的用途，并在显示时为其分配直观的图标。目前，4D-Explorer 可以识别这几种扩展名：
- .4dstem : 4D-STEM 数据集，必须是 4 维数组
- .img : 灰度图像，必须是 2 维数组。不支持 RGB 彩色图像或其他多通道图像。
- .vec : 二维矢量场，具有两个分量。每个分量各自是一张灰度图像。
- .line : 一条线，必须是 1 维的。
未来随着应用需要，可能会添加更多扩展名，以区分不同种类、维度、用途的数据集。


> 注意，名字中不能包含斜杠 /、反斜杠 \ 、冒号 : 、星号 * 、问号 ? 、引号 " 、单引号 '、小于号 <、大于号 >、竖线 | 等特殊字符，不能以空格开头或结尾，也不能将点号 . 或者两个点号 .. 作为名字。总之，取名的限制和操作系统中文件名的限制差不多，建议选择不容易出错的取名方式，比如用下划线连接两个单词。


## 导入数据

4D-Explorer 支持导入 4D-STEM 数据集以及二维图像。未来还会支持导入更多种类格式的数据。

### 导入 EMPAD 所采集的 4D-STEM 数据集

在导入数据之前，需要先打开一个 HDF5 文件。在主界面菜单栏的编辑 (Edit) 菜单中，找到导入 4D-STEM 数据集的按钮 (Import 4D-STEM dataset)，点击即可打开导入对话框。或者，可以在主界面左侧的文件栏中，任选一个群组 (Group) 选中，然后点击右键，在菜单中选择 'Import 4D-STEM dataset'。

在弹出的导入数据对话框中，在导入文件类型 (Import File Type) 处选择 EMPAD v1.0，然后在 EMPAD XML file 处点击 'Browse' 按钮，选择需要导入的 EMPAD XML 文件。选择了 XML 文件之后，会自动根据 XML 文件寻找相应的 RAW 文件，并填在下面的 EMPAD RAW file 处。然后，在导入数据集目标位置 (Import Dataset to Location) 处，可以浏览选择导入数据集的 Group，而在下面的名称 (Name) 处则可以填写导入数据集的名称。

> 注意，导入我们提供的测试数据时，应当选择 EMPAD v0.51 (for NJU)。

### 导入 Merlin Medipix 所采集的 4D-STEM 数据集

Merlin Medipix3 所采集的数据集为 .mib 格式，并且一般还会附带 .hdr 文件。

在导入数据之前，需要先打开一个 HDF5 文件。在主界面菜单栏的编辑 (Edit) 菜单中，找到导入 4D-STEM 数据集的按钮 (Import 4D-STEM dataset)，点击即可打开导入对话框。或者，可以在主界面左侧的文件栏中，任选一个群组 (Group) 选中，然后点击右键，在菜单中选择 'Import 4D-STEM dataset'。

在弹出的导入数据对话框中，在导入文件类型 (Import File Type) 处选择 MerlinEM (.mib)。然后，分别在 MerlinEM MIB file 和 MerlinEM HDR file 点击浏览 (Browse) 按钮，选择相应的文件填入。在 .hdr 文件中，会储存扫描坐标相关的信息，当勾选了根据 .hdr 文件设置扫描坐标时，即可读取这些信息。而若是没有提供 .hdr 文件，或者不希望使用 .hdr 文件中内置的扫描坐标信息，那么就不勾选，然后在下面的扫描步数 (Scanning steps) 处填写其扫描坐标的尺寸。

在弹出的导入数据对话框中，在导入文件类型 (Import File Type) 处选择 EMPAD v1.0，然后在 EMPAD XML file 处点击 'Browse' 按钮，选择需要导入的 EMPAD XML 文件。选择了 XML 文件之后，会自动根据 XML 文件寻找相应的 RAW 文件，并填在下面的 EMPAD RAW file 处。然后，在导入数据集目标位置 (Import Dataset to Location) 处，可以浏览选择导入数据集的 Group，而在下面的名称 (Name) 处则可以填写导入数据集的名称。

### 导入保存在一般的二进制文件中的 4D-STEM 数据集

许多 4D-STEM 数据集的格式都是未压缩的二进制文件，其特征是在文件头有一段字节长度可以跳过，而在之后连续存储各个衍射图像。若希望导入的数据集为目前 4D-Explorer 尚未专门适配的格式，那么在已知二进制格式的存储方式的情况下，可以通过这种方式来将其导入到 HDF5 文件中。

在导入数据之前，需要先打开一个 HDF5 文件。在主界面菜单栏的编辑 (Edit) 菜单中，找到导入 4D-STEM 数据集的按钮 (Import 4D-STEM dataset)，点击即可打开导入对话框。或者，可以在主界面左侧的文件栏中，任选一个群组 (Group) 选中，然后点击右键，在菜单中选择 'Import 4D-STEM dataset'。

在弹出的导入数据对话框中，在导入文件类型 (Import File Type) 处选择 General Raw Data (Binary)。然后，在 Raw file 处点击浏览 (Browse) 按钮，以选择需要导入的二进制文件。然后，在下面依次填入如下参数：
- 数据类型 (Scalar Type)，分为无符号整型 (usigned integer)、整型 (integer) 以及浮点数 (float)
- 每个数字的位数 (Scalar Size)，支持 8 bit、16 bit、32 bit、64 bit 等。对于部分 6 bit 的数据集，也选用 8 bit。
- 衍射图像宽度 (Image Width)，即衍射图像的宽所对应的像素数
- 衍射图像高度 (Image Height)，即衍射图像的高所对应的像素数
- 扫描列数 (Number of Scanning Columns, scan_i)
- 扫描行数 (Number of Scanning Columns, scan_j)
- 第一张图的偏移量 (Offset to first image, bytes)，即文件头部分所占用的字节数
- 每两张图之间的间隔 (Gap between Images, bytes)，即两张衍射图像之间需要跳过的字节数
- 是否为小端字节序 (Little-endian byte order)，如果是，请勾选此项

接下来还有两个参数，分别是
- 是否需要翻转衍射图像 (Flip diffraction patterns, exchange i, j coordinates) 如果勾选，那么就会将衍射图像沿着左上到右下的方向进行翻转。
- 衍射图像顺时针旋转 90° 的次数 (Rotate nx90°, clock-wise)，可以选择 1、2、3 次，也就是旋转 90°、180°、270° 等。
这两项主要用于数据集的坐标约定与 4D-Explorer 所采用的坐标约定不同的情形。对于同一种格式的数据集而言，应当采用相同的设置。

最后，在导入数据集目标位置 (Import Dataset to Location) 处，可以浏览选择导入数据集的 Group，而在下面的名称 (Name) 处则可以填写导入数据集的名称。

作为示例，测试数据集可以通过以下参数导入 (在选择文件时，应当选择数据文件夹中的 .raw 文件)：


| 参数名称           | gold_nanoparticle_06 | gold_nanoparticle_07 | MoS2_14 |
|--------------------|----------------------|----------------------|---------|
| 数据类型           | float                | float                | float   |
| 数据位数           | 32 bit               | 32 bit               | 32 bit  |
| 衍射图像宽度       | 256                  | 128                  | 128     |
| 衍射图像高度       | 256                  | 128                  | 128     |
| 扫描列数           | 128                  | 128                  | 128     |
| 扫描行数           | 128                  | 128                  | 128     |
| 第一张图的偏移量   | 0                    | 0                    | 0       |
| 每两张图之间的间隔 | 1024                 | 1024                 | 1024    |
| 小端字节序         | 是                   | 是                   | 是      |
| 翻转衍射图像       | 是                   | 是                   | 是      |
| 旋转 90° 的次数    | 3                    | 3                    | 3       |



通过这种方式导入的数据集缺失了很多实验参数，因此在导入后应尽快手动填写这些实验参数。

## 导出数据

目前 4D-Explorer 只支持以 HDF5 文件为导出目标。未来将会添加导出其他格式数据的方法。

## 4D-Explorer 的元数据管理方式

> 使用 4D-Explorer 测试数据集中的 gold_particle_06 重构出来的环形暗场像作为演示

4D-Explorer 基于 HDF5 所提供的元数据功能来管理实验参数，元数据以键值对的形式存储。进一步地，4D-Explorer 内置了一套元数据规范，规定了对于某种扩展名的数据而言，特定键的用途、单位、描述以及数据类型。这些键都是以斜杠开头的路径风格的字符串，例如：
```
'/Acquisition/Microscope/accelerate_voltage'
```
表示 4D-STEM 的加速电压。前面的 Acquisition 以及 Microscope 则主要起到分组作用，便于显示。

要修改元数据，在左侧数据集列表中，找到对应的数据集，右键打开菜单，点击最底下的属性 (Attributes) 。在弹出的对话框中，可以看到这些元数据都已经按照分组以树状的形式列出来了，其中左侧显示的是元数据名称 (注意，这里的名称是 4D-Explorer 根据内置的元数据规范所提供的，并不等同于键)，右侧显示的是值以及内置的单位。

![View Metadata](/docs/fig/ViewMetadata.png)

在列表中选定某项元数据，右键打开菜单，即可增加、修改或删除元数据。点击修改元数据 (Edit) 后，会打开修改元数据的对话框。里面从上到下依次表示：
- 当前元数据所属的数据集或群组的路径 (Item Path)
- 元数据的键 (Metadata Key)
- 元数据的数据类型 (Value Type)。目前支持整型、浮点型或字符串。可以点击右侧更改数据类型按钮进行更改。
- 值 (Value)。对于字符串而言，值可以任意输入；对于浮点数类型的元数据而言，填写数值的输入框依照科学计数法的约定，分为小数部分和指数部分。在输入框下面还会显示该输入所约定的单位。
- 注意事项 (Note)。对于 4D-Explorer 内置规范中所包含的键，在注意事项中会提示其用途。修改这些元数据的值时也会提出额外警告，以提醒用户小心修改。

![Edit Metadata](/docs/fig/EditMetadata.png)

# 显示数据

> 使用 4D-Explorer 测试数据集中的 gold_particle_06 重构出来的环形暗场像作为演示

目前 4D-Explorer 支持显示 4D-STEM 数据、图像 (单通道二维图像) 以及矢量场 (双通道二维图像，第一个通道为 i 方向的矢量分量，第二个通道为 j 方向的矢量分量)。4D-Explorer 绘图基于 matplotlib 库，matplotlib 是一个用于创建静态、动画和交互式可视化的 Python 库。它提供了广泛的绘图功能，包括线图、散点图、柱状图、直方图、等高线图、3D 图等。通过使用 matplotlib，4D-Explorer 能够以高质量和灵活的方式显示各种类型的数据。

> matplotlib 注重于出版级质量的绘图，其动画性能及效果有一定的局限性。在 4D-Explorer 用鼠标拖拽或者滚轮拖动某些部件可以对图像进行动态调整，但请不要长时间保持动画效果，因为这可能会导致软件不稳定。

## 工具栏

在图像显示的上方，可能会有一行工具栏，其上的按钮可以方便地对图像的效果进行调整。它通常包括 10 个按钮，分别为：
- 返回初始状态 (Home)
- 后退
- 前进
- 缩放 (四个方向的箭头图标)。点击该按钮后，鼠标在绘图区域会变成四个方向箭头的形状。此时，按住鼠标左键并拖拽图像，可以移动视场；按住鼠标右键并向上或向右拖拽，则为放大；按住鼠标右键并向左或向下拖拽，则为缩小。再次点击该按钮可以退出缩放状态。如果拖拽颜色条区域，则可以调整颜色映射范围。
- 放大镜。点击该按钮后，鼠标在绘图区域会变成十字架。此时，按住鼠标左键，从左上往右下区域拖拽，可以设置新视场为拖拽范围。再次点击该按钮可推出放大镜状态。
- 配置子图排版。点击该按钮后，可以调整图像的相对尺寸。其调整逻辑可能并不是很直观，如果不小心调错了，可以按最左边的 Home 按钮返回初始状态。
- 调整子图。点击该按钮后，会弹出配置子图的对话框，里面可以详细调整子图的颜色映射、插值算法、视场范围、值域等参数。
- 保存。点击该按钮后，可以将当前显示的图片以 .png 或 .jpg 等格式保存。注意，这里输出的是渲染后的图像，包含了颜色条、坐标轴等信息，而不是原始的数据。
- 标尺。点击该按钮后可以调整标尺的属性。

![Adjust Viewing Data](/docs/fig/ViewData.png)

> 如果没有显示 10 个按钮，可能是因为可供展示的空间不够宽。尝试最大化软件窗口、隐藏左侧面板或调整页面中间和右边所占的空间比例。

> 如果空间足够宽，那么在按钮的右侧还会显示当前鼠标所对应的坐标位置。

## 显示 4D-STEM 数据

> 使用 4D-Explorer 测试数据集中的 MoS2_14 作为演示

在界面左侧的数据集列表中，找到需要显示的 4D-STEM 数据集 (.4dstem 数据) ，右键点击 Open，即可打开显示该数据集的页面。此时，4D-Explorer 自动创建了一个空的二维图像，叫做 MoS2_14_preview.img。其具有和 4D-STEM 数据集的扫描坐标相同的尺寸，但值为零。其用途是在页面右侧表示扫描坐标。用鼠标左键点击右侧的图像后，即可将扫描点定位到鼠标点击处，从而查看对应扫描位置的衍射图像。

若对该数据集已经重构过相应的图像，可点击浏览预览图 (Browse Preview) 按钮，选择重构的图像放在右侧，代替没有内容的空数据集。这样可以更加直观地展示不同扫描位置与衍射图像之间的对应关系。此时，便可将临时的 MoS2_14_preivew.img 数据集删去。

> 预览图像的尺寸应当和 4D-STEM 数据集的扫描步数相同。

![View 4D-STEM Dataset](/docs/fig/View4DSTEM_MoS2.png)

在页面右侧扫描图像下面有滑动条和选择框，可以调节衍射图像的亮度 (Brightness)、对比度 (Contrast)、数据标度 (Norm, 线性或对数)、颜色映射 (Color map)。

在页面中间衍射图像下面，可以调整当前显示的扫描位置。

## 显示二维图像的数据

> 使用 4D-Explorer 测试数据集中的 gold_particle_06 重构出来的环形暗场像作为演示

在界面左侧的数据集列表中，找到需要显示的二维图像 (.img 数据)，右键点击 Open，即可打开显示该图像的页面。在页面的右边显示的是该图像的直方图。

![Adjust Viewing Data](/docs/fig/ViewData.png)

在页面右侧扫描图像下面有滑动条和选择框，可以调节衍射图像的亮度 (Brightness)、对比度 (Contrast)、数据标度 (Norm, 线性或对数)、颜色映射 (Color map)。在上面的图中我们就调整了亮度、对比度，并修改颜色映射为 plasma。我们还使用缩放按钮，将图像拖动、放大到某个特定的区域。

## 显示矢量场的数据

> 使用 4D-Explorer 测试数据集中的 MoS2_14 重构出来的 iCoM 图像作为演示

在界面左侧的数据集列表中，找到需要显示的矢量场 (.vec 数据)，右键点击 Open，即可打开显示该矢量场的页面。此时，4D-Explorer 自动创建了一个空的二维图像，名字为 {矢量场名字}_bkgrd.img。其具有和矢量场相同的宽度和高度，但值为零。其用途是在页面右侧表示矢量场的背景。

若对该矢量场有在相同空间下的图像 (如，对于 CoM 矢量场，此时已经有 iCoM 图像或者环形暗场图像)，则可以点击浏览背景 (Browse Background) 按钮，选择合适的背景图像，来代替空的图像。这样可以更加直观地展示矢量场各个矢量所对应的位置附近的样品信息。此时，便可将临时创建的空矢量场背景图删去。

若发现矢量场的箭头尺寸不合适 (整体过长、过短、过粗、过细) 或者想更换其颜色，那么可以点击调整箭头图效果 (Adjust Quiver Effects) 按钮来进行调整。

![View Vector Field](/docs/fig/ViewVectorField.png)

> 在调整矢量场效果的对话框中，箭头长度比例 (Arrow Length Scale) 用于调整箭头的长度。和直觉相反，它的值越高，每个箭头的长度越短。

## 标尺

在图像显示的上方，可能会有一行工具栏，其上的按钮可以方便地对图像的效果进行调整。它通常包括 10 个按钮，其中最右边的按钮 (一个直尺) 即为调整标尺的按钮。

点击该按钮，会弹出一个对话框。对于已经校正过实验参数的 4D-STEM 数据集及其导出的图像、矢量场而言，标尺会读取其参数，并自动选择合适的长度及显示单位。在弹出的对话框中，可以自行设置其在给定单位下的长度。

但如果数据集缺乏相关的元数据，标尺则会以像素数 (pix) 作为单位。此时，可以勾选定制化比例尺 (Customize Scale)，然后手动填写每个像素格子的长度以及该长度所对应的单位。

在对话框的顶部还可以选择其他两个面板，分别是标尺的显示效果 (Bar Style) 以及文字的显示效果 (Text Style)，可以对标尺及文字的颜色、大小、方向、透明度、字体等进行调整。


# 校正 4D-STEM 数据集 

对于精确的、定量化的 4D-STEM 成像而言，细致的校正往往是很重要的。目前 4D-Explorer 内置了四个校正 4D-STEM 数据集的步骤，分别是：
- 完善数据集的实验参数
- 去除背景噪声
- 扫描旋转校正
- 衍射合轴

## 完善数据集的实验参数 

> 使用 4D-Explorer 测试数据集中的 gold_particle_06 作为演示

在左侧控制面板中，右键点击对应的 4D-STEM 数据集，在菜单中找到校准 (Calibration)，然后在子菜单中找到编辑 4D-STEM 参数 (Edit 4D-STEM Parameters)，点击即可打开编辑 4D-STEM 实验参数的对话框。在这里，可以根据引导一步步地调整 4D-STEM 数据集的参数，或者说元数据 (metadata)。

在对话框的上方可以看到各个步骤，包括：
- General, 一般的、通用的参数
- Microscope, 透射电镜设备的参数
- Camera, 电子相机的参数
- Space, 对扫描空间以及衍射空间进行定量化的参数
- Low Order Aberration, 低阶像差系数 (离焦量、球差系数等)
- High Order Aberration, 高阶像差系数 (四阶以上的像差)
可以通过按下 "←Back" 按钮回到上一个步骤，也可以按下 "Next→" 按钮前往下一个步骤。

![Edit 4D-STEM Parameters](/docs/fig/Edit4DSTEMParameters.png)

### 通用参数
第一页是 General 通用参数。

首先，我们可以给数据集起一个名字。这里的名字不同于出现在 HDF5 文件中的名字，它仅仅作为标识使用。在 Dataset Title 那里，现在应该显示的是 (None)，表示这个数据集的元数据中并没有存储名字。可以点击对应的编辑 (Edit) 按钮，就打开了一个编辑元数据的对话框。对话框里，在项的路径 (Item Path) 中显示的是数据集的路径，而在元数据键 (Metadata Key) 中，显示的是我们正在编辑的元数据的键，而下面值 (Value) 的部分则是空的。现在，我们在值的部分填写 4D-Explorer Test Dataset 或者其他你喜欢的名字，再点击 OK。此时会弹出一个对话框，提示说这是一个预定义的元数据，让我们谨慎修改，继续点击 OK 即可完成修改。

### 电镜参数
我们可以顺次修改这些元数据。当第一页 General 修改完了之后 (当然，有些元数据留空也没问题)，点击 Next→ 按钮，进入第二页，也就是 Microscope 页面。在这里，可以填写一些关于电镜的一些信息，例如我们将电镜的名字改为 Thermofisher FEI Titan G2 60-300。

接下来则有几个关键的参数，包括电子束流 (Beam Current)、加速电压 (Accelerate Voltage)、相机长度 (Camera Length)、会聚(半) 角 (Convergence Angle, $\alpha$)、停留时间 (Dwell Time) 以及扫描步长 (Step Size)。这些参数决定了数据集的量化分析结果，因此非常重要，需要谨慎修改。其中部分参数，比如相机长度以及会聚角，一般需要使用标准样品进行标定之后才能确定。

![Edit Convergence Angle](/docs/fig/EditConvergenceAngle.png)

在这里，我们编辑会聚角。测试实验数据 gold_nanoparticle_06 的会聚角为 22.5 mard，因此我们在 Value 处用科学计数法填写 2.25 x 10^-2 rad。然后点 OK 按钮，并在弹出的对话框中再次点击 OK 按钮。

### 相机参数
Camera 页的参数则是和相机有关的。其中，像素数目指的是相机的像素数目，这个数值和数据集中衍射图像的尺寸不一定是一致的 (因为我们可以人为地裁剪或者填充衍射图像，但却无法更改作为硬件的相机的底片)，而传感器像素尺寸则指的是相机像素在物理上的尺寸，就是我们可以把相机拆下来放在放大镜下用直尺量出来的那个像素尺寸。

### 空间参数
第四页则是空间 (Space) 有关的参数，实际上主要指的是 4D-STEM 数据集中，每个像素在空间中所对应的尺寸。因此，这一页的参数同样非常重要，决定了数据集的量化分析结果，需要谨慎修改。其中，$\Delta u$ 表示衍射空间的像素尺寸，单位和空间频率一致。它满足
$$ N_{br}\Delta u = \alpha / \lambda $$
其中 $N_{br}$ 是明场衍射盘的半径像素数，$\alpha$ 是会聚半角，$\lambda$ 是电子束的波长。$\Delta u$ 参数和会聚半角、相机长度等参数需要一道通过标准样品标定而来。

$\Delta r$ 表示实空间的像素格子长度，这里的实空间和衍射空间互为倒易关系。它和 $\Delta u$ 之间满足 $\Delta r \Delta u = N$，其中 $N$ 是衍射图像的边像素数。

扫描 $\Delta r_p$ 表示数据集中相邻两张衍射图像所对应采样点的中心距离。$\Delta r_p$ 在绝大多数情况下和电镜参数中的扫描步长是一致的。之所以分成两个键记录，主要是考虑到有时可能会在数据集中丢弃或合并多张衍射图像的情形。在软件中，对 4D-STEM 的定量化计算会以 $\Delta r_p$ 为准。

> 注意，$\Delta r_p$ 和 $\Delta r$ 的单位都是物理长度，但其通常并不相同。对于虚拟成像以及质心成像等应用，所重构出来的样品图像的像素格子长度为 $\Delta r_p$；而对于叠层衍射 (Ptychography) 等应用而言，图像的像素格子长度为 $\Delta r$。

### 像差系数 
最后两页则是和像差有关的参数，具体来说是各阶像差系数，其意义包括：

| 符号 | 描述 |
|------|------|
| `C1` | 离焦 (defocus) |
| `A1` | 二重像散 (two-fold astigmatism) |
| `B2` | 轴向彗差 (axial coma) |
| `A2` | 三重像散 (three-fold astigmatism) |
| `C3` | 球差 (spherical aberration) |
| `S3` | 星形像差 (star aberration) |
| `A3` | 四重像散 (four-fold astigmatism) |
| `B4` | 轴向彗差 (axial coma) |
| `D4` | 三叶像差 (three lobe aberration) |
| `A4` | 五重像散 (five-fold astigmatism) |
| `C5` | 球差 (spherical aberration) |
| `A5` | 六重像散 (sixfold astigmatism) |

这里的像差符号及意义，遵从 
`S. Uhlemann, M. Haider Ultramicroscopy, 78(1999): 1-11` 
所给出的约定。

除了可以设定其像差大小之外，还可以设置各级像差的角度。不过，离焦量和球差都是对称的，所以设置角度不会对它们产生影响。

设置了这些像差之后，可以用于模拟出其电子探针 (Probe) 以及真空衍射斑的形状，并可以计算在当前像差条件下虚拟成像以及质心成像的衬度传递函数。

## 去除背景噪声 

4D-Explorer 提供两种去除背景噪声的办法，分别是减去参考背景图像方法，以及一种基于像素直方图的过滤方法。

在左侧控制面板中，找到想要校正的 4D-STEM 数据集并右键点击，在菜单中找到校准 (Calibration)，然后在子菜单中找到减去背景 (Background Subtraction)，即可打开去除背景噪声的页面。

### 减去参考背景图像法

在打开的页面中，右侧上方初始时是减去参考图像 (Subtract Reference) 的标签。点击 Browse 即可在 HDF5 中寻找扩展名为 .img 的数据集，作为需要减去的背景图像。该图像的尺寸必须和 4D-STEM 数据集的衍射图像尺寸一致。勾选应用减去背景的勾选框 (Apply Background Subtraction)，即可在中间显示减去背景之后的图像效果。完成后，点击页面最下方的开始减去背景的红色按钮，即可打开对话框以设置输出数据集的路径。

### 像素直方图过滤法

如果在打开的页面中，右侧上方点击选择窗口过滤器 (Select Windwo Filter) 的标签，则可以选择使用像素直方图的过滤方法。映入眼帘的是目前中间显示的衍射图像的直方图。通过设置过滤窗口的最小限制和最大限制，可以确保衍射图像中在窗外的值都被过滤掉。过滤规则是：
- 大于最大限制的值的那些像素，会被设置为最大限制值
- 小于最小限制的值的那些像素，会被设置为 0
通过勾选应用过滤窗口 (最小限制) 或者勾选应用过滤窗口 (最大限制)，即可在中间显示过滤后的效果。一般而言，对于去除背景噪声 (特别是 X 射线所造成的底噪) 的需求，可以只设置最小限制。完成后，点击页面最下方的开始减去背景的红色按钮，即可打开对话框以设置输出数据集的路径。

## 扫描旋转校正

我们在进行理论分析以及编程的时候，通常会假定 4D-STEM 的扫描空间轴 (也就是电子束在样品上扫描的路径) 与衍射空间轴 (也就是电子相机像素排列的方向) 具有相同的方向，这样就可以方便地用 $xOy$ 坐标系来描述它们。然而，在实际的实验中，电子相机会被固定在电镜上，而电子束的扫描方式却可以任意指定。最常见的情形，当属电子束用 $Z$ 字形扫描，而方向与电子相机的安装方向相差某个角度。此时，就需要进行扫描旋转校正。4D-Explorer 提供两种校正扫描坐标与衍射坐标之间的旋转角度的方法，分别是质心旋度法和离焦近轴明场像法。

在左侧控制面板中，找到想要校正的 4D-STEM 数据集并右键点击，在菜单中找到校准 (Calibration)，然后在子菜单中找到衍射旋转 (Diffraction Rotation)，即可打开扫描旋转校正的页面。

### 质心旋度法

> 使用 4D-Explorer 测试数据集中的 gold_particle_06 作为演示

4D-STEM 数据集中，每个衍射图像的质心，正比于样品在对应扫描位置处的电场强度 (假定样品不具有磁性)。众所周知，电场强度分布是无旋的，这一点在球体 (金颗粒) 附近特别明显，所有位置的电场矢量都从球体中心向四周发散 (或者汇聚)，而没有任何围绕球体旋转的分量。

因此，如果我们发现数据集所重构出来的质心图像不是无旋的，或者说球体周围的质心矢量出现了围绕球体旋转的分量，就意味着衍射空间和扫描空间的坐标轴之间出现了旋转，以至于每个质心矢量都被转了一个角度。那么，我们可以尝试人为地旋转这些矢量，从而让这些矢量重新回到那种在球体周边发散的情形。此时，矢量场就变回了无旋场，是正确的状态。这样，寻找扫描旋转角度的过程就等效为了让旋度最小的过程，这便是质心旋度法的原理。

在软件左侧控制面板中，找到想要校正的 4D-STEM 数据集并右键点击，在菜单中找到校准 (Calibration)，然后在子菜单中找到衍射旋转 (Diffraction Rotation)，即可打开扫描旋转校正的页面。

在打开的旋转校正页面中，右侧上方初始时就是使用质心旋度法进行扫描旋转校正。首先，可以点击矢量场路径 (Vector Field Path) 所对应的浏览 (Browse) 按钮，来选择当前 4D-STEM 数据集的质心重构矢量场数据集。如果还没有，可以先重构一个看看效果。选定矢量场后，在页面右侧即可显示该矢量场。如果矢量场的显示效果不好，可以点击下面的调整箭头图效果 (Adjust Quiver Effect) 按钮，调整箭头的长度、宽度和颜色等。

![Rotational Offset Correction Using CoM Method](/docs/fig/DiffractionRotation.png)

矢量场的下面有可以调节旋转角度的输入框，输入框右侧有刷新按钮，点击后即可显示当前矢量场中的每个矢量都被旋转一定角度之后的样子。

点击下面的计算旋转角度 (Calculate Rotation Angle) 按钮，可以打开一个对话框，里面显示了各个旋转角度所对应的旋度以及散度的平方和。在曲线的下方会自动填写当前曲线中取得最小旋度的那个角度。点击确认，可以将这个角度应用回页面中矢量场图像，以观察此时的质心分布是否是有源无旋场。

![Minimize Curl of CoM](/docs/fig/MinimizeCurl.png)

确认一个角度后，可以点击页面最下方的应用旋转并开始计算 (Apply Rotation and Start Calculation) 的红色按钮 (如果没有看见这个按钮，它可能被藏在了页面底部，需要鼠标滚动一下或者拖动页面最右边的滚动条)。选择好输出的 4D-STEM 数据集的路径和名字之后，就会将 4D-STEM 中的所有衍射图像都旋转这个角度，并组成新的 4D-STEM 数据集。

> 尽管我们在这里作了样品是非磁性样品的假设，但即使样品具有磁性，其所造成的质心分布依然是无旋的。毕竟，磁感应强度的分布是有旋而无源的，因而我们可以想象一个围绕着某个点环绕一圈的磁场。电子束受到磁场洛伦兹力的影响，其偏转方向是垂直于磁感应强度的，这就相当于将每个箭头都旋转了 90°，自然就将有旋无源场转换成了有源无旋场，得到了和电场影响类似的质心矢量分布。这一事实带来的好处是，我们对磁性样品的数据集，同样可以用质心旋度最小的准则来判断扫描旋转角度。但坏处是，我们没有办法通过场的散度和旋度的性质来分离样品中的电场与磁场了。

### 离焦近轴明场像法

> 使用 4D-Explorer 测试数据集中的 gold_particle_07 作为演示

另一种测量扫描旋转角度的方法，需要在实验中采集离焦的数据集，并且需要在衍射图像中能看见样品的形貌 (从而方便判断方向)。

在扫描透射电子显微镜 (STEM) 中，如果我们使用点状的探测器，那么此时的光路就和使用平行电子束的传统 (TEM) 完全相反了。在这个光路中，点状的探测器对应于 TEM 的点光源，而会聚镜对应于 TEM 中的物镜。既然如此，这种使用点状探测器所获得的成像就具有和 TEM 成像类似的性质，尤其是具有相同形式的衬度传递函数。

这有什么用呢？TEM 成像一般具有比较大的景深，意味着我们即使用了比较大的离焦量，也足以在成像中看见物体的大致形貌 (尽管此时分辨率会比正焦或者略微欠焦时要低一些)。因此，当我们采集了离焦的 4D-STEM 数据集，且离焦量大到能在衍射图像中能看见物体形貌时，就可以用这种点状的探测器来进行虚拟成像重构。虚拟成像模式所用的几种虚拟探测器中，只有点状探测器能在这种情况下重构出比较清晰的图像，而像明场像、环形明场像、环形暗场像等模式，景深都很小，只能产生一片模糊。

我们将用这种点状探测器得到的重构像叫做近轴明场像。既然同样可以看见样品的形貌，它就可以拿来和衍射图像中的形貌进行比对。如果它们中间相差了一定的角度，就说明衍射坐标和扫描坐标之间有相对旋转。毕竟，衍射图像中的形貌是单个扫描点拍摄下来的，体现的是衍射坐标；而重构图像的每个像素则对应于每个扫描点，因此其几何位置体现的是扫描坐标。

在软件左侧控制面板中，找到想要校正的 4D-STEM 数据集并右键点击，在菜单中找到校准 (Calibration)，然后在子菜单中找到衍射旋转 (Diffraction Rotation)，即可打开扫描旋转校正的页面。

在打开的旋转校正页面中，右侧上方可以选择近轴明场像法 (Axial BF Method)，即可打开相应的操作面板。点击右侧上方对应于近轴明场像路径 (Axial BF Path) 的浏览 (Browse) 按钮，即可进入选择这套数据集对应的重构像的页面。如果还没有，可以先在虚拟成像中重构一个看看效果，记得在虚拟成像页面中选用点状的探测器，也就是把明场探测器的半径缩小到1个像素左右。

![Rotational Offset Correction Using Defocused Axial BF Image](/docs/fig/RotationWithAxialBF.png)

选好近轴明场像后，即可显示近轴明场像。通过调整旋转角度 (Rotation Angle) 所对应的输入框，可以查看页面中间衍射图像旋转后的效果。当衍射图像旋转后与右边近轴明场像平行，就意味着找到了扫描坐标与衍射坐标之间的旋转角度。

![Rotate Diffraction Pattern](/docs/fig/RotationWithAxialBF2.png)

确认一个角度后，可以点击页面最下方的应用旋转并开始计算 (Apply Rotation and Start Calculation) 的红色按钮 (如果没有看见这个按钮，它可能被藏在了页面底部，需要鼠标滚动一下或者拖动页面最右边的滚动条)。选择好输出的 4D-STEM 数据集的路径和名字之后，就会将 4D-STEM 中的所有衍射图像都旋转这个角度，并组成新的 4D-STEM 数据集。

> 当旋转到正确的角度时，通过调整页面中间下方扫描位置的输入框，可以观察到随着扫描位置的移动，衍射图像中的样品形貌也有所移动。当调整 i 方向的扫描位置时，衍射图像中的样品形貌会沿着 i 方向，也就是上下移动；当调整 j 方向的扫描位置时，衍射图像中的形状则会左右移动。用鼠标滚轮调整输入框时，这个现象会更加明显而直观。

### 衍射图像额外旋转 180° 

通过扫描旋转校正找到的角度，可能和真实角度之间相差了 180°。无论是质心旋度法还是离焦近轴明场像法都无法判断是否有这额外的 180°，但如果不确定的话，所得到的电场方向就有可能和真实电场是相反的，并且 dCoM、iCoM 这些成像模式也有可能获得相反的衬度。

有种实用的方法来判断是否需要额外旋转 180°。我们可以先在虚拟成像中重构出环形暗场像，在这里亮的 (数值较高的) 就是样品电势高的区域，而暗的就是样品电势低的区域。然后，我们可以在质心成像中，勾选上 "使用投影电场映射" (Use projected electric field mapping) 的选项，并重构出积分质心 (iCoM) 像以及微分质心 (dCoM) 像。然后将 iCoM/dCoM 像和环形暗场像进行比对 (可以将图像放大一些，比对一个较小区域)。如果发现这些图像中较亮的区域是一致的，那么就不需要额外旋转 180°；如果发现环形暗场像的衬度与 iCoM/dCoM 像是相反的，那么就需要额外旋转 180°。

### 坐标轴翻转

坐标轴翻转 (flip) 指的是扫描坐标轴和衍射坐标轴遵循不同的手性约定。不论是 xOy 坐标系还是在 4D-Explorer 中采用的 ij 坐标系，都是右手系，只不过相差了 90° 的旋转。但假如拍摄的衍射图像或扫描坐标轴有一个是左手系，就会导致无论我们怎么进行扫描旋转校正，都无法得到正确的坐标系，也无法重构出正确的质心矢量场。

同一台电镜、相机所采集的数据集中都会使用同一套坐标轴手性的约定。因此，如果是第一次使用来自某台设备的数据，在读取 4D-STEM 数据集时，需要仔细选取是否需要对衍射图像进行翻转。

## 衍射合轴

在理论分析中，一般假定光轴，也就是明场衍射盘的中心，与相机的中心 (或者说像素网格的中心) 是完全重合的。但在实际的实验过程中，很难确保明场衍射盘正好对准了图像的中心，一般都会有一定的偏移，叫做衍射偏移 (Diffraction Shift)。

当出现衍射偏移时，质心成像的质量会受到严重影响，毕竟衍射盘整体的偏移会直接影响质心的值。要知道，在质心成像中，要想获取薄样品的局部电场的分布，我们需要测量的是衍射盘内部的亮度分布不均所导致的质心偏移，而不是衍射盘整体的偏移。因此，我们应当尽可能避免出现衍射偏移的现象。

更糟糕的情况是，偏移量还有可能随着扫描位置的不同而不一样，也叫做衍射摆动 (Diffraction Wobble)。这个现象一般在扫描范围比较大的时候出现，毕竟扫描的位置越偏，离光轴就越远。此时，我们光给衍射图像整体进行平移还不够，还得对每张衍射图像都进行细致的平移。然而一套典型的 4D-STEM 数据集有数万张衍射图像，纯靠人力显然无法完成这等艰巨的任务。

幸运的是，摆动的幅度随着扫描位置的变化可以近似为线性的，所以只需要测量一部分衍射盘的偏移，然后用线性拟合就可以得到 4D-STEM 数据集中每个衍射盘的偏移分布。有了偏移分布，自然就可以将其应用到整个数据集上进行平移。

于是问题归结为如何测量明场衍射盘的偏移。4D-Explorer 提供三种方法：
- 手动测量偏移量
- 使用真空条件下拍摄的参考数据集。参考数据集的质心分布就是偏移量。
- 用深度神经网络模型 (FDDNet) 来测量

### 手动测量衍射盘偏移量

> 使用 4D-Explorer 测试数据集中的 gold_particle_06 作为演示

在左侧面板中找到想要校正的 4D-STEM 数据集并右键点击，在打开的菜单中选择校正 (Calibration) -> 衍射合轴 (Diffraction Alignment)。在打开的页面中，默认即为手动法进行测量。

在手动测量前，可以先进行一些准备工作。在页面右边的顶部，可以切换到显示效果 (Displaying Effects) 栏，在辅助圆 (Auxiliary Circle) 部分，可以调整圆的半径以及中心位置。建议可以将圆的半径调整到和明场衍射盘同等大小。注意在下方要勾选显示辅助圆 (Show auxiliary circle)。

![Diffraction Shift Alignment Manually](/docs/fig/DiffractionAlignmentManual.png)

然后，在右边顶部切换回衍射漂移校正 (Diffraction Shift Alignment) 栏。首先，对于 (0, 0) 的扫描位置，设置 i 方向的平移为 1，j 方向的平移为 -2.7，即可让衍射盘移动到图像的正中心。此时，在右边下半部分，有一个列表，可以记录下我们在不同位置处所测量的偏移值。表格上方有四个按钮，从左到右分别表示添加、删除、修改和导入。这里，我们点击添加按钮，表格中即添加了一行记录，Location 为 (0,0)，而 Shift 为 (-1.0, 2.7)。

> 当平移量设置为带有小数部分，衍射图像可能会看起来变模糊一些，这是因为进行亚像素的平移时需要进行插值。尽管看上去衍射盘变模糊了，但插值在大多数情况下不会对最终的重构结果造成严重影响。

接下来，移动到扫描范围的四个角落，即 (255, 0), (0, 255), (255, 255)，分别重复上面的操作，我们就可以得到了四条记录。对于 (255, 255)，我们发现衍射图像的多重散射效应严重，不适合测量，那么也可以用附近的扫描位置，比如 (253, 254) 来代替。此外，也可以再多选几个扫描点，特别是在扫描范围内均匀分布的点，测量相应的明场衍射盘偏移量。

![Generate Shift Alignment Manually](/docs/fig/DiffractionAlignmentManual2.png)

测量完成后，点击下面的生成偏移分布 (Generate Shift Mapping) 按钮，则可以打开一个对话框，里面需要选择一种生成偏移分布的拟合办法。这里我们选择线性回归 (Linear Regression)。点击确认，然后再选择需要保存的数据集的路径和名字即可。

生成偏移分布后，可以在右边顶部选择显示效果 (Displaying Effects) 栏，在偏移分布路径 (Shift Mapping Path) 部分，就可以选择刚刚生成的偏移分布。此时，在辅助圆部分，下面的设置圆中心至偏移矢量指向的位置 (Set circle to where the shift vector point to) 变得可选。我们勾选这个选项，就可以看到圆心位置被设置为测量得到的偏移分布所指向的位置了。当我们调整扫描位置时，可以观察到辅助圆随着衍射盘的位置变化而发生位置变化，从而检验测量得到的偏移分布是否正确。在使用滚轮调整扫描位置时，这种效果会更加明显。

![View Shift Mapping](/docs/fig/DiffractionAlignmentManual3.png)

> 查看用辅助圆来查看偏移分布的效果时，记得先回到 Diffraction Alignment 界面，取消勾选 Display shifted diffraction image，让衍射盘回到未经过手动平移的原始状态。 

在图中，衍射盘明显偏移了图像的中心，而辅助圆根据刚刚手动生成的平移分布设置圆心位置，使得圆心也偏离了图像的中心，并与衍射盘的中心重合。

当确认偏移分布无误之后，即可点击页面下方开始应用合轴 (Start to apply alignment) 的红色按钮。选择输出数据集的路径并填好名称后，点 OK 即可。

### 使用参考数据集

这种方法需要在实验中采集一套真空下的 4D-STEM 数据集，并且其光路参数应当和带有样品的数据集所对应的光路参数保持一致。

在左侧面板中找到想要校正的 4D-STEM 数据集并右键点击，在打开的菜单中选择校正 (Calibration) -> 衍射合轴 (Diffraction Alignment)。在打开的页面中，右侧上部的合轴方法 (Alignment Method) 选择框中选择使用参考数据集 (Use Reference Dataset)，即使用参考数据集来进行测量。

首先，在参考 4D-STEM 数据集的路径框右边，点击浏览 (Browse) 按钮，即可选择参考的 4D-STEM 数据集。然后，可以勾选显示平移后的衍射图像 (Display shifted diffraction image)，中间就显示的是根据参考图像的质心平移后的衍射图像。调整扫描位置时，可以观察到明场衍射盘是否维持在图像中心。点击生成平移分布 (Generate Shift Mapping) 的按钮，即可生成平移分布。

生成偏移分布后，可以在右边顶部选择显示效果 (Displaying Effects) 栏，在偏移分布路径 (Shift Mapping Path) 部分，就可以选择刚刚生成的偏移分布。此时，在辅助圆部分，下面的设置圆中心至偏移矢量指向的位置 (Set circle to where the shift vector point to) 变得可选。我们勾选这个选项，就可以看到圆心位置被设置为测量得到的偏移分布所指向的位置了。当我们调整扫描位置时，可以观察到辅助圆随着衍射盘的位置变化而发生位置变化，从而检验测量得到的偏移分布是否正确。在使用滚轮调整扫描位置时，这种效果会更加明显。

当确认偏移分布无误之后，即可点击页面下方开始应用合轴 (Start to apply alignment) 的红色按钮。选择输出数据集的路径并填好名称后，点 OK 即可。

### 使用 FDDNet 模型测量衍射盘偏移量 

> 使用 4D-Explorer 测试数据集中的 gold_particle_06 作为演示

FDDNet 是一个基于深度学习的衍射明场衍射盘轮廓估计模型，可以用于测量衍射盘的平移量。

首先，在左侧面板中找到想要校正的 4D-STEM 数据集并右键点击，在打开的菜单中选择校正 (Calibration) -> 衍射合轴 (Diffraction Alignment)。在打开的页面中，右侧上部的合轴方法 (Alignment Method) 选择框中选择使用 FDDNet 模型 (Use FDDNet)，即使用 FDDNet 模型来进行测量。

可以勾选上显示平移后的衍射图像 (Display shifted diffraction image)，从而自动根据 FDDNet 的测量结果将当前的衍射图像平移到中心位置。这样，当我们调整扫描位置时，若观察到衍射盘总是在中心位置，就说明 FDDNet 准确测量出了衍射盘的偏移量。 

也可以勾选上显示测量椭圆 (Show the measured ellipse)，从而自动根据 FDDNet 的测量结果，并在中间画出椭圆来表示测量结果。这样，当我们调整扫描位置时，若椭圆总是与明场衍射盘的边界重合，就说明 FDDNet 准确测量出了明场衍射盘的轮廓。

> 不建议同时勾选显示平移后的衍射图像以及显示测量椭圆。这会使得 FDDNet 测量出来的椭圆边无法与明场衍射盘的边缘重合，让人难以判断 FDDNet 的测量结果是否准确。

如果觉得椭圆的显示效果不好 (例如太粗或太细，颜色不喜欢等)，可以点击调整椭圆效果 (Adjust Ellipse Effects) 按钮进行调整。

![Diffraction Shift Alignment Using FDDNet](/docs/fig/DiffractionAlignmentFDDNet.png)

之后，可以点击生成偏移分布 (Generate Shift Mapping) 即可生成偏移分布。对于一般规模的 4D-STEM 数据集，这个过程所需的时间可能会稍长一点，因为这会对每一张衍射图像都应用 FDDNet 模型进行推理。可以在左边切换到任务面板，即可查看处理的进度条。

生成偏移分布后，可以在右边顶部选择显示效果 (Displaying Effects) 栏，在偏移分布路径 (Shift Mapping Path) 部分，就可以选择刚刚生成的偏移分布。此时，在辅助圆部分，下面的设置圆中心至偏移矢量指向的位置 (Set circle to where the shift vector point to) 变得可选。我们勾选这个选项，就可以看到圆心位置被设置为测量得到的偏移分布所指向的位置了。当我们调整扫描位置时，可以观察到辅助圆随着衍射盘的位置变化而发生位置变化，从而检验测量得到的偏移分布是否正确。在使用滚轮调整扫描位置时，这种效果会更加明显。

![View Shift Mapping from FDDNet](/docs/fig/DiffractionAlignmentFDDNet2.png)

当确认偏移分布无误之后，即可点击页面下方开始应用合轴 (Start to apply alignment) 的红色按钮。选择输出数据集的路径并填好名称后，点 OK 即可。


# 重构图像

有多种从 4D-STEM 数据集中重构出样品的图像的方法。目前 4D-Explorer 支持虚拟成像以及质心成像。

## 虚拟成像

> 使用 4D-Explorer 测试数据集中的 MoS2 作为演示

虚拟成像 (Virtual Imaging) 是一种从 4D-STEM 数据集中重构出样品图像的方法。其原理是通过在衍射空间中选择一个特定的区域（例如可以选择一个环形区域，即为环形暗场像，ADF），然后对每个扫描位置的衍射图像进行积分，得到一个二维的样品图像。这个过程模拟了在传统透射电子显微镜中使用环形暗场探测器获取图像的方式。虚拟成像的优势在于可以灵活地选择不同的散射角度范围，从而得到不同衬度传递函数和分辨率的样品图像。此外，由于是在软件中进行处理，可以方便地进行参数调整和优化。

在左侧面板中找到想要重构的 4D-STEM 数据集并右键点击，在打开的菜单中选择重构 (Reconstruction) -> 虚拟成像 (Virtual Imaging)。在右上角的区域类型选择框 (Domain Shape) 中可以选择重构所需的区域类型，例如圆形区域 (可以用来计算近轴明场像 Axial BF 和明场像 BF)、环形区域 (可以用来计算环形明场像 ABF 和环形暗场像 ADF)、扇形区域等等。选择好区域类型后，可以在下面调整区域的参数，如圆形的半径以及圆心坐标等。

![Adjust Displaying Style of Integral Regions](/docs/fig/AdjustReconstructionEffects.png)

如果不喜欢区域的显示效果 (如颜色、透明度等)，可以点击调整效果... (Adjust Effects...) 按钮，在打开的对话框中可以调整积分区域的透明度 (Alpha)、边缘颜色 (Edge Color)、内部颜色 (Face Color)、填充纹理 (Hatch)、边的线型 (Line Style)、线宽 (Line Width) 等，还可以选择是否需要填充区域。

选择好积分区域后，点击页面下方的开始计算 (Start Calculation) 红色按钮，即选择输出图像的路径并填好名称后，点 OK 即可开始计算。

## 质心成像

> 使用 4D-Explorer 测试数据集中的 MoS2 作为演示

质心成像 (CoM, Center of Mass Imaging) 是一种从 4D-STEM 数据集中重构出样品图像的方法。其科学原理是基于样品电场对电子束的偏转作用。当电子束穿过样品时，样品的电场会使电子束发生偏转，这种偏转作用可以通过计算衍射图像的质心来量化。质心即为样品投影电场分布的反映。具体来说，质心成像通过计算每个扫描位置的衍射图像的质心（即重心），然后将这些质心位置映射到样品空间中，从而得到一个二维的样品图像。质心成像对于弱散射信号具有较高的灵敏度。此外，还可以计算 iCoM (Integrated CoM) 和 dCoM (Differential CoM)，分别对应于样品的电势和电荷密度。iCoM 是通过积分衍射图像的质心来获取样品的电势分布，而 dCoM 是通过微分衍射图像的质心来获取样品的电荷密度分布。

在左侧面板中找到想要重构的 4D-STEM 数据集并右键点击，在打开的菜单中选择重构 (Reconstruction) -> 质心成像 (Center of Mass Imaging)。在右上角的区域类型选择框 (Domain Shape) 中可以选择参与计算质心的图像区域形状，例如圆形区域、环形区域等。选择好区域类型后，可以在下面调整区域的参数，如圆形的半径以及圆心坐标等。当然，对于质心成像而言，圆形区域一般至少要覆盖明场衍射盘，或者也可以将区域半径设得很大以覆盖整个衍射图像。

如果不喜欢区域的显示效果 (如颜色、透明度等)，可以点击调整效果... (Adjust Effects...) 按钮，在打开的对话框中可以调整积分区域的透明度 (Alpha)、边缘颜色 (Edge Color)、内部颜色 (Face Color)、填充纹理 (Hatch)、边的线型 (Line Style)、线宽 (Line Width) 等，还可以选择是否需要填充区域。

![Start Computing CoM](/docs/fig/StartComputingCoM.png)

选择好积分区域后，点击页面下方的开始计算 (Start Calculation) 红色按钮，即选择输出图像的路径并填好名称。注意，这里可以一次性生成多种图像，包括 CoM 矢量场、两个方向的分量 (作为二维图片)、iCoM 以及 dCoM 等等。每个图像类型右边的框中表示希望输出的这张图像的名字。对话框的顶部可以设置这些图像输出在哪个 群组 (Group) 下面。而在对话框的下面可以勾选使用质心映射 (Use Center of Mass mapping) 还是使用投影电场映射 (Use projected electric field mapping)。这两者之间相差一个符号，对于投影电场映射来说，矢量场从高电势的地方指向低电势的方向，和我们印象中的电场强度一致。还可以勾选归一化，即设置平均场强为零，以避免出现均匀的、具有一定方向的电场背景，从而影响 iCoM 的成像效果。将这些设置好后，点 OK 即可开始计算。


