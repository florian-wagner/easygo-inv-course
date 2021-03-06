# EASYGO Training Week: Inversion tutorial and the open-source geoscientific Python stack

<div width="50%">
<img src="https://easygo-itn.eu/wp-content/uploads/2021/04/logo.png" width=40%>
</div>

| **Time**      | **Content**                                      | **Instructor(s)**                                                           |
|---------------|--------------------------------------------------|-----------------------------------------------------------------------------|
| 10:00 - 11:00 | Introduction to research by RWTH PIs             | Florian Wellmann, Florian Wagner, Florian Amann, Peter Kukla                |
| 11:00 - 12:30   | Inverse theory - The deterministic perspective | Florian Wagner                                                              |
| _12:30 - 14:00_ | _Lunch break_                                  | -                                                                           |
| 14:00 - 15:30   | Inverse theory - The probabilistic perspective | Florian Wellmann                                                            |
| _15:30 - 16:00_ | _Break_                                        | -                                                                           |
| 16:00 - 18:00   | The open-source geoscience software stack      | Jan Niederau, Alex Juestel, Nils Chudalla, Florian Wellmann, Florian Wagner |

## Setup instructions

> ### Quick setup for experienced users
>
> If you are working on Mac or Linux and have worked with conda and have git installed, you can copy & paste these lines separately. For all others, we recommend to carefully read the descriptions of individual steps below.
>
> ```bash
> git clone https://github.com/florian-wagner/easygo-inv-course
> cd easygo-inv-course
> conda install -c conda-forge mamba
> mamba env create
> conda activate easygo
> python3 test_installation.py
> ```

To start the tutorial setup, please follow the next steps:

### Step 1: Prerequisites

There are a few things you'll need to follow the tutorial:

1. A working Python installation (Anaconda or Miniconda). For details on how to install Anaconda, we refer to: <https://docs.anaconda.com/anaconda/install/>
2. A modern web browser that works with JupyterLab or Jupyter Notebook (Internet explorer will not work)
3. Intermediate experience in Python programming (Python, numpy, matplotlib, jupyter)

### Step 2: Download material for the tutorial

- Windows: [Download the course material](https://github.com/florian-wagner/easygo-inv-course/archive/refs/heads/main.zip) and unzip it a folder of your choice.
- Mac/Linux: You can do the same as above, or alternatively open a terminal, navigate to a folder of your choice, and execute `git clone https://github.com/florian-wagner/easygo-inv-course`.

### Step 3: Install the tutorial environment

1. Open a terminal (Linux & Mac) or the Anaconda Powershell Prompt (Windows). Navigate to the folder from step 2 (using the `cd` command) and type:

```
conda install -c conda-forge mamba
mamba env create
```

2. Activate the environment in the terminal by typing:

```
conda activate easygo
```

3. To test if everything works correctly you can do the following:

```
python3 test_installation.py
```

### Step 4: Start JupyterLab

1. **Windows users:** Make sure you set a default browser that is **not Internet Explorer**.
2. Activate the conda environment: `conda activate easygo`
3. Start JupyterLab: `jupyter lab`
4. Jupyter should open in your default web browser.
