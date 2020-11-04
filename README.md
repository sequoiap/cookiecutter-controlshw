# cookiecutter-controlshw
A cookiecutter template for all the Controls Homework problems.


# Getting Started
We'll use Anaconda for our Python environments. You can download it [here]().

Within the Anaconda Prompt (search "Anaconda Prompt" in Windows), we'll create a new environment using the command:

```
conda create -n <you-pick-a-reasonable-name> python
```

I would recommend a short, all-lowercase, no-symbol name (e.g., `controls`). After that's been created, activate it with the command shown in the terminal:

```
conda activae <the-environment-name-you-chose>
```

Note you'll have to activate your environment every time you start Anaconda Prompt in order to access your installed Python packages.

Install the following packages by using these commands in the prompt:

```
conda install -c conda-forge cookiecutter
conda install -c anaconda make
```
