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
from mfit.cf import fit_parallel
```

## API

### `mfit.cf`

Optimization-based model fitting utilities with closed-form likelihoods.

- **`mfit.cf.fit`**: single-fit optimization (`"Nelder-Mead"`, `"BFGS"`, `"bads"`: [Acerbi & Ma, 2017](https://doi.org/10.48550/arXiv.1705.04405))
- **`mfit.cf.fit_parallel`**: parallel multi-start wrapper around `fit`
- **`mfit.cf.fit_hier`**: hierarchical EM fitting ([Huys et al., 2011](https://doi.org/10.1371/journal.pcbi.1002028))
- **`mfit.cf.fit_bms`**: group Bayesian model selection ([Stephan et al., 2009](https://doi.org/10.1016/j.neuroimage.2009.03.025); [Rigoux et al., 2014](https://doi.org/10.1016/j.neuroimage.2013.08.065))

### `mfit.ibs`

Sampling-based model fitting utilities with likelihoods estimated via inverse binomial sampling .

- **`mfit.ibs.ibs_ll`**: unbiased log-likelihood estimation via IBS [van Opheusden et al., 2020](https://doi.org/10.1371/journal.pcbi.1008483)
