# CFD科研绘图工具

## 1. 介绍
    该工具是为了方便CFD后处理而开发的，主要包括以下几个功能：
    1.绘制Cf曲线图
    2.绘制简易云图
    3.残差图

## 2. 使用方法
    在Utilities/目录下，运行setup.py文件，将脚本路径注册到bashrc中，每次打开终端时，都会自动加载该脚本。

    1.绘制Cf曲线图
        在OpenFOAM的case目录下，创建yml文件，具体格式如下：
        ```
        transform:
  U0: 5.4
  nu: 1.5e-5

files:
  - path: "path/to/your/rawfile1.raw"
    label: "case1"
    skiprows: 1
    type: "line" # 可选，默认为 'line'
    marker: "o" # 可选
    markerevery: 100 # 可选
    
  - path: "path/to/your/rawfile2.raw"
    label: "case2"
    skiprows: 1
    type: "scatter" # 可选，默认为 'line'
    marker: "x" # 可选
    markerevery: 100 # 可选

exp_files: # (可选)
  - path: "path/to/your/experiment_file.raw"
    label: "Experiment"
    skiprows: 1
    type: "scatter" # 可选，默认为 'line'
    marker: "+" # 可选

plot:
  title: "Plot Title"
  xlabel: "X Axis Label"
  ylabel: "Y Axis Label"
  xlim: [xmin, xmax] # (可选)
  ylim: [ymin, ymax] # (可选)
  figsize: [12, 6]
  '''
        然后在终端中输入：
        ```
        createSDict (anyname) <patchName> <FieldName>

        sampleOnce (openfoam时间步: 例如1000)

        plot_cf (yml文件名)
        ```
        即可绘制Cf曲线图。

    2.绘制简易云图
        在OpenFOAM的case目录下，创建yml文件，具体格式如下：
        ```
        
    vtkFilePath: 'path/to/vtk/gamma.vtk'
    field: 'gamma'
    plot:
        title: 'Gamma Distribution in XY Plane'
        xlabel: 'X'
        ylabel: 'Y'
        colorMap: 'jet'
        xlim: [0, 3]    # 可选
        ylim: [0, 0.01]    # 可选
        resolution:
            x: 400
            y: 200
        savePath: 'gamma.png'
    transform(optional):
        enable: True
        x: 0.5

        ```
        然后在终端中输入：
        ```
        foamToVTK -times yourTimeStep -fields '(yourField)'

        plotSimContour (yml文件名)
        ```

    3.绘制残差图
        目前仅支持绘制dafoam的残差图，直接在case目录下运行：
        ```
        plotres
        ```