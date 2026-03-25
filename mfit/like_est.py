"""
Inverse binomial sampling (IBS) for log-likelihood estimation.


"""

from __future__ import annotations

from typing import Any, Callable, Optional, Sequence, Union

import numpy as np
from scipy.special import psi


def ibs_ll(
    sample_fn: Callable,
    params: np.ndarray,
    responses: np.ndarray,
    design: Optional[np.ndarray] = None,
    num_reps: int = 1,
    max_iter: int = 2000,
    nll_threshold: float = np.inf,
) -> float:
    """
    Unbiased estimate of total log-likelihood via inverse binomial sampling.

    For each trial, we repeatedly draw from the simulator until it matches
    the observed response. The number of draws K is used to estimate the
    per-trial log-probability via the digamma identity:

        log p_hat = psi(1) - psi(K)

    which is O(1) per trial (vs. the naive O(K) harmonic sum).

    Args:
        sample_fn: callable(params, design_row) -> simulated response.
        params: parameter vector passed to sample_fn.
        responses: observed response matrix (n_trials, ...).
        design: stimulus/design matrix (n_trials, ...); if None, passes
                None to sample_fn for every trial.
        num_reps: number of independent IBS estimates to average.
        max_iter: cap on samples per trial (safety against near-zero
                  probability events); when hit, K is clamped here.
                  Default value is 2000, p = 0.00028
        nll_threshold: if the running NLL exceeds this value mid-trial,
                       abort the current rep early and return. During
                       optimization, pass your current-best NLL here to
                       skip obviously bad parameter points fast.

    Returns:
        Estimated log-likelihood (scalar).

    ----------------------------------------------------------------
    References:
    van Opheusden*, B., Acerbi*, L., & Ma, W. J. (2020).
    Unbiased and efficient log-likelihood estimation with inverse binomial sampling.
    PLoS Computational Biology, 16(12): e1008483.
    ----------------------------------------------------------------
    Based on: https://github.com/acerbilab/pyibs

    @ZF 
    """
    n_trials = len(responses)
    psi_1 = float(psi(1))
    ll_reps = np.zeros(num_reps)

    for rep in range(num_reps):
        ll = 0.0
        for t in range(n_trials):
            s_t = design[t] if design is not None else None
            K = 1
            while not np.array_equal(sample_fn(params, s_t), responses[t]):
                K += 1
                if K >= max_iter:
                    break
            ll += psi_1 - float(psi(K))
            if -ll > nll_threshold:
                break
        ll_reps[rep] = ll

    return float(np.mean(ll_reps))
