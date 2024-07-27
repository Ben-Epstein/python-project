# python-project
A clean, extensible, python project template, build using [Makefile](https://www.gnu.org/software/make/manual/make.html), [ruff](https://github.com/astral-sh/ruff), and [uv](https://github.com/astral-sh/uv).

## Why?
Python tooling moves really fast, and python package management is notoriously difficult. How do you resolve dependencies, do you need a lockfile, how can you quickly test your configurations and ensure everything works as expected locally and in production?

There's no definitive answer to this, but I like the idea of a system that is lightweight and lets you move really quickly.

## Why not Poetry?
I'm not a fan of theoretical arguments for or against some piece of technology. I like to think about tooling with regards to how quickly and easily it allows you to do the thing it claims to enable. In that light, poetry, in my opinion, has 2 flaws that make it unusable for larger-scale projects:
1. It is [_slow_](https://github.com/python-poetry/poetry/issues/2094). Way too slow. I've used poetry for large scale production projects in the past, and have had to wait over 700 seconds for a `poetry lock --no-update` to complete. This is too slow, and can completely break the flow of a project. Adding a new dependency to a project, or updating an existing one, should take less than 10 seconds. 
2. Poetry is too rigid, leading to [unresolvable dependency conflicts](https://github.com/python-poetry/poetry/issues/697#issuecomment-1807062324). Poetry doesn't let you override conflicting dependencies. This, in theory, makes sense, but in practice is untenable. If any downstream dependency of any of my dependencies, accidentally has `tqdm==4.65.0` specified, no other dependency can be installed that conflicts. If another downstream repo somewhere has `tqdm >= 4.66`, your entire tree breaks. This is silly. People building projects will not always list dependencies perfectly, and we need a system that can handle these imperfections.

## Setup

There are many kinds of python-based repos, but two pretty common ones are:
1. an SDK (ie installed by others)
2. an API/Servie/Pipeline (internal, only installed by the creators).

### SDK
An SDK needs to be as flexible as reasonable with their dependencies. Lots of people (hopefully) will be building with their repo, so the repo should have as loose of dependencies as can reasonably be tested. In this case, in my opinion, a lockfile is not required, and testing as wide a range of dependencies is suggested (ie testing your code with lower and upper bounds of each dependency).

For this, we have the CI run tests for 2 cases:
1. Installing all dependencies at the low-end of their pins
2. Installing all dependencies at the high-end of their pins

This ensures everything is as compatible as we can reasonably confirm

### API
An API/Internal repo, that's perhaps built into a docker image and deployed, is in some ways the opposite. You don't need wide ranges, because no one else is installing it. In this case, a lockfile is critical, ensuring that the code you write and test in dev is identical to the code you run in prod. 

For this, we have a lockfile that we validate on every PR to main, ensuring that no new packages have been added to the `pyproject.toml`, making the lockfile out of date.

## Tools

We try to keep the tools to a minimum, with exceptions for massively increasing speed or quality of life.
* Makefile: A ubiquitous tool, default installed on most systems, to ensure that everyone can run the identical commands and get set up as easily as possible
* ruff: An awesome linter, written in rust, that is [so fast that you think it's lying](https://x.com/tiangolo/status/1591912354882764802)
* uv: A python package manager, also built in rust (by the same amazing folks at [@astral-sh](https://github.com/astral-sh), which makes managing python dependencies pretty easy and insanely fast. It's a rapidly growing project, moving very quickly. So it's possible that by the time you see this, they support something that would make this setup even easier.
* mypy: Standard type-safety checking for python.
* github actions: all CI/CD

There's no `cd.yaml` workflow, which could either
* deploy an image
* deploy a package to pypi
* deploy a cloud function
* ...

Because those are pretty easy to find on the internet, and not specifically releavant to this repo.

## Setting up the automated comment for invalid lockfiles
This is a few steps, so if you're interested, screenshots are here 

See the readme in [src](./src) for usage details.

You can see an example of a PR that adds a package but doesn't update the lockfile, which causes a failed PR test and an automated comment to the PR telling the author to run `make lock`