=====
Usage
=====

To use Nobinobi Daily Follow-Up in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'nobinobi_daily_follow_up.apps.NobinobiDailyFollowUpConfig',
        ...
    )

Add Nobinobi Daily Follow-Up's URL patterns:

.. code-block:: python

    from nobinobi_daily_follow_up import urls as nobinobi_daily_follow_up_urls


    urlpatterns = [
        ...
        url(r'^', include(nobinobi_daily_follow_up_urls)),
        ...
    ]
