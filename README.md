# mfit

Local-installable model fitting utilities.

## Install(from git)

### Regular install

```bash
pip install "git+https://github.com/fangzefunny/mfit.git"
```
### Upgrade the package

```bash
pip install --upgrade "git+https://github.com/fangzefunny/mfit.git"
```

## Quickstart

```python
from mfit.fit import fit_parallel
```

## API

### `mfit.fit`

Optimization-based model fitting utilities with closed-form likelihoods.

- **`mfit.fit.fit_single`**: given a likelihood, fit parameters (`"Nelder-Mead"`, `"BFGS"`, `"bads"`: [Acerbi & Ma, 2017](https://doi.org/10.48550/arXiv.1705.04405))
- **`mfit.fit.fit_parallel`**: parallel multi-start wrapper around `fit_single`
- **`mfit.fit.fit_hier`**: hierarchical EM fitting ([Huys et al., 2011](https://doi.org/10.1371/journal.pcbi.1002028))
- **`mfit.fit.fit_bms`**: group Bayesian model selection ([Stephan et al., 2009](https://doi.org/10.1016/j.neuroimage.2009.03.025); [Rigoux et al., 2014](https://doi.org/10.1016/j.neuroimage.2013.08.065))

### `mfit.like_est`

Likelihood estimation for simulator models (generators).

- **`mfit.like_est.ibs_ll`**: estimate log-likelihood via inverse binomial sampling (IBS) ([van Opheusden et al., 2020](https://doi.org/10.1371/journal.pcbi.1008483))
