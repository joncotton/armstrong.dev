CHANGES
=======

2.0 (unreleased)
------------------

- **Backward incompatible:** ``env_settings.py`` is required and contains
  the settings that ``fabfile.py`` used to have. It is written in the normal
  Django settings.py style of variable assignments.

- **Backward incompatible:** ``tasks.py`` is required and replaces the
  previously required ``fabfile.py``. It no longer defines Django settings
  (now handled in ``env_settings.py``).

- **Backward incompatible:** switched from Fabric to Invoke, so the ``fab``
  command is replaced with ``invoke``.

- **Backward incompatible:** Lettuce testing support is gone.

- **Backward incompatible:** the Sphinx documentation command ``docs`` is gone.

- **Backward incompatible:** remove ``assertInContext``, ``assertNone``,
  ``assertIsA`` and ``assertDoesNotHave``. Some of these duplicated native
  Python methods and the potential confusion was greater than the benefit.

- **Backward incompatible:** individual components need to specify the
  ``fudge`` requirement if they need it.

- **Backward incompatible:** Fix ``generate_random_users()`` and turn it 
  into a generator.

- **Backward incompatible:** remove ``concrete`` decorators. The Armstrong
  standard practice is to use "support" models when necessary in testing,
  which are much easier to use and understand.

- Setuptools is explictly used. This is not a backwards incompatible change
  because anything installed with Pip was automatically and transparently
  using Setuptools/Distribute *anyway*. We rely on setup kwargs that Distutils
  doesn't support and that only worked because of Pip's behind the scenes swap.
  This allowed us to remove boilerplate and better prepares us for Python 3
  and perhaps even more simplifying refactors. Functionally though, this
  doesn't change anything.

- Drop the atypical VirtualDjango in favor of the ``settings.configure()``
  Django bootstrapping method.

- Bare minimum package requirements for as-fast-as-possible virtualenv
  creation. Even Invoke is optional when running tests. Individual tasks
  can specify package requirements and will nicely message their needs if
  the package is not installed.

- Run any Django ``manage.py`` command from import or the CLI with
  component-specific settings bootstrapped in.

- Run tests with arguments. Use any args that ``manage.py test`` accepts
  to run only specific test cases, change output verbosity, etc.

- Coverage testing is ready for multiple environments at once (like with Tox).

- Use (and backport) the Django 1.6 test runner. This standardizes testing
  in favor of the newest method so we don't need to be cognisant of the current
  Django version as we test across multiple versions. Bonus: because the new
  runner is explicit about test discovery, drop the ``TESTED_APP`` code.

- New ``remove_armstrong`` task command to uninstall every Armstrong component
  (except for ArmDev).