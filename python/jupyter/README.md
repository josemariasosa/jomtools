# Jupyter

## Install jupyter

```bash
pip3 install --upgrade pip
pip3 install jupyter
```

## Add Virtual Environment to Jupyter Notebook

I assume that you are a tidy person: you have all your work sorted out in folders; one of these folders contains your very important project and it looks like this:

```bash
$ ls

project/
├── data
├── docs
├── src
└── test
```

Inside this folder create a new virtual environment:

```bash
python -m venv projectname
```

Then activate it:

```bash
source projectname/bin/activate
```

Now, from inside the environment install ipykernel using pip:

```bash
pip install ipykernel
```

And now install a new kernel:

```bash
ipython kernel install --user --name=projectname
```

At this point, you can start jupyter, create a new notebook and select the kernel that lives inside your environment.

## Remove Virtual Environment from Jupyter Notebook

After you deleted your virtual environment, you’ll want to remove it also from Jupyter. Let’s first see which kernels are available. You can list them with:

```bash
jupyter kernelspec list
```

This should return something like:

```bash
Available kernels:
  myenv      /home/user/.local/share/jupyter/kernels/myenv
  python3    /usr/local/share/jupyter/kernels/python3
```

Now, to uninstall the kernel, you can type:

```bash
jupyter kernelspec uninstall myenv
```

References:
- https://janakiev.com/blog/jupyter-virtual-envs/
- https://anbasile.github.io/programming/2017/06/25/jupyter-venv/