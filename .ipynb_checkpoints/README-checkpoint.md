# CS435 Quantum Programming 1

Welcome to CS435 Quantum Programming 1. 

This course combines theoretical foundations of quantum computing with practical implementation using IBM’s Qiskit SDK  based on the Python programming language.

The material is based on QWorld’s educational notebooks: [bronze-qiskit](https://gitlab.com/qworld/bronze-qiskit/) (beginner), [nickel](https://gitlab.com/qworld/silver/) (intermediate), and [silver](https://gitlab.com/qworld/silver/) (intermediate), primarily developed by [Dr. Abuzer Yakaryılmaz](http://abu.lu.lv) (University of Latvia) and Dr. Özlem Salehi Köken.

## Installation

In order to work with these jupyter notebooks, you need a number of packages. The following instructions ensure that the python verson and package versions are consistent and work with the notebooks.

1. Download this repository and extract it somewhere.

Then either use Conda, venv or virtualenv as follows.

### Conda (Recommended)

The following two steps are for installing the required packages.

1. Open a terminal or command prompt at the directory where you extracted the files.
2. Run the following command to create a new Conda environment and install all necessary packages.

```bash
conda env create -f environment.yml
```

The following steps should be followed every time you want to work on the notebooks.

1. Activate the Conda environment.

```bash
conda activate cs435
```

After activation, your command prompt or terminal prompt should change to indicate that you are now working within the virtual environment. 

2. You can now launch jupyter notebook.

```bash
jupyter notebook
```

3. Deactivate the Conda environment when you're done.

```bash
conda deactivate
```


### Using venv or virtualenv

1. Make sure you are using Python 3.10.8.
2. Open a terminal or command prompt at the directory where you extracted the files.
3. Run one of the following commands (depending on whether you want to use venv or virtualenv) to create a virtual environment.

```bash
# create environment using venv
python -m venv cs435venv
# OR create environment using virtualenv
pip install virtualenv
virtualenv cs435venv
```

4. Activate the virtual environment.

On Windows
```bash
cs435venv\Scripts\activate
```

On macOS or Linux:
```bash
source cs435venv/bin/activate
```

After activation, your command prompt or terminal prompt should change to indicate that you are now working within the virtual environment.

5. Install packages using pip. 

```bash
pip install -r requirements.txt
```

If you are a Mac OS user you might need to install the qiskit[visualization] in the following way
```bash
pip install 'qiskit[visualization]'
```

6. You can now launch jupyter notebook.

```bash
jupyter notebook
```

7. Deactivate the Conda environment when you're done.

```bash
conda deactivate
```

Every time you work on the notebooks, you should reexecute steps 4, 6 and 7, remembering to switch to the directory where you created the virtual environment.


## Credits

Please check [credits](credits.ipynb).


## License

The code of this project is licensed under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

The text and figures of this work is licensed under a Creative Commons Attribution 4.0 International License, available at [https://creativecommons.org/licenses/by/4.0/legalcode](https://creativecommons.org/licenses/by/4.0/legalcode).

