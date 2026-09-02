# zenpy-release-poc

> ⚠️ **This is NOT a real package. Do not `pip install` it.** It is a
> throwaway proof-of-concept published to real PyPI only to test a release
> automation workflow. It does nothing useful and will not be maintained or
> updated for actual use.

Minimal proof-of-concept for the release-automation approach proposed for
[facetoe/zenpy#692](https://github.com/facetoe/zenpy/pull/692#issuecomment-5451069842):
a GitHub Actions workflow that publishes to PyPI via Trusted Publishing
(OIDC) whenever a GitHub Release is published.

Not a real package - just enough source (`zenpy_release_poc/`, a `setup.py`
build like zenpy's, and one CLI entry point) to exercise the workflow.

**Note:** this targets *production* PyPI, not Test PyPI. A successful run
permanently claims the `zenpy-release-poc` project name and publishes real,
unremovable files (PyPI does not allow re-uploading or deleting individual
release files, only yanking a version). Test PyPI's publishing settings
page was unreliable when this was tried, hence the switch - re-point
`publish.yml`'s pending-publisher target back to test.pypi.org and add
`repository-url: https://test.pypi.org/legacy/` to the publish step if you
want to retry there instead.

## Try it

1. Push this repo to `hassaku63/zenpy-release-poc` on GitHub.
2. On PyPI, add a pending publisher at
   https://pypi.org/manage/account/publishing/ :
   - PyPI project name: `zenpy-release-poc`
   - Owner: `hassaku63`
   - Repository: `zenpy-release-poc`
   - Workflow: `publish.yml`
   - Environment: (leave blank)
3. Tag the commit `0.1.0` (must match `zenpy_release_poc/__version__`) and
   push the tag.
4. Create a GitHub Release from that tag and publish it.
5. Watch the Actions run - it should build and upload to
   https://pypi.org/project/zenpy-release-poc/ with no secrets stored in
   the repo.

## Local sanity check

```
pip install -e .
zenpy-release-poc --version
zenpy-release-poc
```
