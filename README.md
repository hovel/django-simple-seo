# Django SimpleSEO

## Features

This app provides two ways of adding SEO metadata to your django site:

- Absolute paths
- Model instances

It's fully integrated with the admin site including inline forms for models.
It also includes support for multiple languages and localized URLs.

## Requirements

    Django >= 1.7.0

## Installation

The Git repository can be cloned with this command:

    git clone https://github.com/Glamping-Hub/django-simple-seo.git

The `simpleseo` package included in the distribution should be placed on the `PYTHONPATH`. Add `simpleseo` to the `INSTALLED_APPS` in your *settings.py*. Run `migrate` command to create the needed tables.

## Registering Models

To create synced SEO metadata for model instances you have to define the `SEO_MODELS` variable in your *settings.py* like this:

    SEO_MODELS = [
        ('myapp', 'mymodel'),
        ('myapp', 'mymodel'),
    ]

After registering the models, you can add the inline form to the admin instance for each model:

    from simpleseo.admin import SeoMetadataInline

    class MyModelAdmin(admin.ModelAdmin):
        inlines = [SeoMetadataInline, ]

Now every time you save a model instance through the admin site the SEO metadata will be updated automatically.

## SEO Output

As simple as loading the `seo` template library and using the `get_seo_*` (title, description, keywords, text) template tags like this:

    {% load seo %}

    <head>
        <title>{% get_seo_title 'Default title' %}</title>
    </head>

## Settings

SimpleSEO also uses 4 configuration variables for defining the default
information that will be displayed if the URL has no SEO metadata related
(priority: settings < templates < models).
You have to add them to your *settings.py*:

    SEO_DEFAULT_TITLE = 'default'
    SEO_DEFAULT_DESCRIPTION = 'default'
    SEO_DEFAULT_KEYWORDS = 'default'
    SEO_DEFAULT_TEXT = 'default'
