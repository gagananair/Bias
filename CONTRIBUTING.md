# Contributing to Bias

Thanks for your interest in this project! This is an active research repo studying caste bias in LLMs, and contributions are welcome.

## Ways to contribute

- **Extend model coverage** — add support for additional models (e.g. Mistral, Qwen) in `verify_caste_bias_2b.py`
- **Expand the name/surname set** — the current surname list is a small illustrative sample; broader, well-sourced lists improve statistical validity
- **Improve classification** — the current `classify()` function uses simple keyword matching; smarter classification (e.g. embedding similarity) would reduce misclassification
- **Add visualizations** — new ways to slice/plot the bias data beyond the current heatmap
- **Documentation** — clarify methodology, add citations to relevant bias/interpretability literature

## Getting started

```bash
git clone https://github.com/GAGANANAIR/Bias.git
cd Bias
pip install -r requirements.txt
```

You'll need a [Neuronpedia](https://neuronpedia.org) API key to run the probing script.

## Submitting changes

1. Fork the repo and create a branch for your change
2. Keep changes focused — one improvement per PR is easier to review
3. Open a pull request describing what you changed and why

## A note on sensitivity

This research deals with caste bias, a sensitive social topic. Please keep discussion, code comments, and test data respectful and focused on the research goal of identifying and understanding bias — not reproducing or amplifying it.
