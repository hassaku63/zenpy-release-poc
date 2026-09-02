# zenpy-release-poc

Minimal proof-of-concept for the release-automation approach proposed for
[facetoe/zenpy#692](https://github.com/facetoe/zenpy/pull/692#issuecomment-5451069842):
a GitHub Actions workflow that publishes to PyPI (here: Test PyPI) via
Trusted Publishing (OIDC) whenever a GitHub Release is published.

Not a real package - just enough source (`zenpy_release_poc/`, a `setup.py`
build like zenpy's, and one CLI entry point) to exercise the workflow.

## Try it

1. Push this repo to `hassaku63/zenpy-release-poc` on GitHub.
2. On Test PyPI, add a pending publisher at
   https://test.pypi.org/manage/account/publishing/ :
   - PyPI project name: `zenpy-release-poc`
   - Owner: `hassaku63`
   - Repository: `zenpy-release-poc`
   - Workflow: `publish.yml`
   - Environment: (leave blank)
3. Tag the commit `0.1.0` (must match `zenpy_release_poc/__version__`) and
   push the tag.
4. Create a GitHub Release from that tag and publish it.
5. Watch the Actions run - it should build and upload to
   https://test.pypi.org/project/zenpy-release-poc/ with no secrets stored
   in the repo.

## Local sanity check

```
pip install -e .
zenpy-release-poc --version
zenpy-release-poc
```
